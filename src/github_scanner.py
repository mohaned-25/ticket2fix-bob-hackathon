import re
import requests


def parse_github_url(repo_url):
    pattern = r"github\.com[:/](?P<owner>[^/]+)/(?P<repo>[^/.]+)"
    match = re.search(pattern, repo_url)

    if not match:
        return None, None

    return match.group("owner"), match.group("repo")


def fetch_repo_files(repo_url):
    owner, repo = parse_github_url(repo_url)

    if not owner or not repo:
        return []

    branches = ["main", "master"]

    for branch in branches:
        api_url = f"https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1"

        try:
            response = requests.get(api_url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                files = [
                    item["path"]
                    for item in data.get("tree", [])
                    if item.get("type") == "blob"
                ]
                return files

        except requests.RequestException:
            return []

    return []


def find_relevant_files(ticket_text, files):
    ticket = ticket_text.lower()

    keyword_map = {
        "auth": ["auth", "login", "password", "reset", "session", "token", "user"],
        "payment": ["payment", "checkout", "stripe", "order", "invoice"],
        "profile": ["profile", "account", "settings", "user"],
        "frontend": ["login", "form", "page", "component", "tsx", "jsx"],
        "api": ["api", "route", "controller", "service"]
    }

    matched_files = []

    for file in files:
        file_lower = file.lower()

        for keywords in keyword_map.values():
            if any(word in ticket for word in keywords) and any(word in file_lower for word in keywords):
                matched_files.append(file)
                break

    return matched_files[:10]