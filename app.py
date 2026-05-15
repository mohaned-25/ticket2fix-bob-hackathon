import json
import time
import streamlit as st

from src.ticket_analyzer import analyze_ticket, estimate_severity
from src.repo_context import find_code_context
from src.task_generator import generate_developer_task
from src.test_generator import generate_test_plan


st.set_page_config(
    page_title="Ticket2Fix",
    page_icon="🛠️",
    layout="wide"
)

SAMPLE_TICKETS = {
    "Password Reset Login Issue": """After resetting password, users cannot log in.
The page refreshes but does not show an error message.
This happens only after using the reset password link.""",

    "Checkout Payment Failure": """Customers cannot complete checkout.
The payment button keeps loading and no confirmation appears.
Some users report being charged twice.""",

    "Profile Update Error": """Users cannot update their profile information.
After clicking save, the page reloads but the new information is not stored."""
}

st.markdown("""
<style>
.hero {
    padding: 2rem;
    border-radius: 20px;
    background: linear-gradient(135deg, #020617, #2563eb);
    color: white;
    margin-bottom: 1.5rem;
}
.card {
    padding: 1.2rem;
    border-radius: 16px;
    background: #f8fafc;
    border: 1px solid #e5e7eb;
    margin-bottom: 1rem;
}
.badge {
    padding: 0.35rem 0.7rem;
    border-radius: 999px;
    font-weight: 700;
    display: inline-block;
}
.high { background: #ffedd5; color: #9a3412; }
.medium { background: #fef9c3; color: #854d0e; }
.low { background: #dcfce7; color: #166534; }
</style>
""", unsafe_allow_html=True)


if "history" not in st.session_state:
    st.session_state.history = []

if "last_result" not in st.session_state:
    st.session_state.last_result = None


def get_category(ticket):
    text = ticket.lower()

    if "password" in text or "login" in text or "log in" in text:
        return "Authentication"
    if "payment" in text or "checkout" in text:
        return "Payment"
    if "profile" in text or "account" in text:
        return "User Account"

    return "General Application Issue"


def get_confidence(ticket):
    text = ticket.lower()
    keywords = ["password", "login", "auth", "checkout", "payment", "profile", "account"]
    matched = [word for word in keywords if word in text]

    if len(matched) >= 3:
        return 0.95, matched
    if len(matched) == 2:
        return 0.85, matched
    if len(matched) == 1:
        return 0.75, matched

    return 0.60, matched


def severity_badge(severity):
    level = severity.split("—")[0].strip()

    if level == "High":
        return f'<span class="badge high">🟠 {severity}</span>'
    if level == "Medium":
        return f'<span class="badge medium">🟡 {severity}</span>'

    return f'<span class="badge low">🟢 {severity}</span>'


st.markdown("""
<div class="hero">
    <h1>🛠️ Ticket2Fix</h1>
    <h3>IBM Bob-assisted Support-to-Code Assistant</h3>
    <p>
    Ticket2Fix converts unclear support tickets into developer-ready tasks,
    likely affected files, debugging checklists, and test plans.
    </p>
</div>
""", unsafe_allow_html=True)


with st.sidebar:
    st.header("📌 Demo Guide")
    st.write("1. Choose a sample ticket or write your own.")
    st.write("2. Add a GitHub repository URL.")
    st.write("3. Paste IBM Bob repository notes if available.")
    st.write("4. Click Analyze Ticket.")
    st.write("5. Export the result.")

    st.divider()

    if st.session_state.history:
        st.subheader("📜 Recent Analyses")
        for item in st.session_state.history:
            st.caption(f"{item['time']} — {item['category']} — {item['severity']}")


st.subheader("🎫 Support Ticket Input")

with st.expander("👀 Preview Sample Tickets"):
    for name, content in SAMPLE_TICKETS.items():
        st.markdown(f"**{name}**")
        st.caption(content[:130] + "...")
        st.divider()


selected_sample = st.selectbox(
    "Choose a sample ticket",
    ["Write my own"] + list(SAMPLE_TICKETS.keys())
)

default_ticket = ""
if selected_sample != "Write my own":
    default_ticket = SAMPLE_TICKETS[selected_sample]

repo_url = st.text_input(
    "GitHub Repository URL",
    placeholder="https://github.com/username/project-repo"
)

bob_notes = st.text_area(
    "IBM Bob Repository Notes / Exported Bob Analysis",
    height=120,
    placeholder="Paste IBM Bob's repository explanation, affected files, architecture notes, or exported Bob report summary here..."
)

ticket_text = st.text_area(
    "Support Ticket / Bug Report",
    value=default_ticket,
    height=180,
    placeholder="Paste the support ticket here..."
)

ticket_length = len(ticket_text)

if ticket_length == 0:
    st.caption(":red[0 characters — please enter a ticket]")
elif ticket_length < 50:
    st.caption(f":orange[{ticket_length} characters — add more details if possible]")
else:
    st.caption(f":green[{ticket_length} characters — good ticket length]")


if st.button("🚀 Analyze Ticket", use_container_width=True):
    if not ticket_text.strip():
        st.error("Please enter a support ticket before analyzing.")
    else:
        with st.status("Analyzing ticket with Ticket2Fix...", expanded=True) as status:
            st.write("🔍 Classifying issue type...")
            time.sleep(0.3)
            category = get_category(ticket_text)

            st.write("📊 Estimating severity...")
            time.sleep(0.3)
            severity = estimate_severity(ticket_text)

            st.write("🧠 Finding repository context...")
            time.sleep(0.3)
            repo_analysis = find_code_context(ticket_text, repo_url, bob_notes)

            st.write("📝 Generating developer task...")
            time.sleep(0.3)
            ticket_analysis = analyze_ticket(ticket_text)
            developer_task = generate_developer_task(
                ticket_text,
                ticket_analysis,
                repo_analysis
            )

            st.write("🧪 Generating test plan...")
            time.sleep(0.3)
            test_plan = generate_test_plan(ticket_text, repo_analysis)

            confidence, detected_keywords = get_confidence(ticket_text)

            status.update(
                label="Analysis complete!",
                state="complete",
                expanded=False
            )

        st.session_state.last_result = {
            "ticket": ticket_text,
            "repo_url": repo_url,
            "bob_notes": bob_notes,
            "category": category,
            "severity": severity,
            "confidence": confidence,
            "detected_keywords": detected_keywords,
            "ticket_analysis": ticket_analysis,
            "repo_analysis": repo_analysis,
            "developer_task": developer_task,
            "test_plan": test_plan
        }

        st.session_state.history.insert(0, {
            "time": time.strftime("%H:%M:%S"),
            "category": category,
            "severity": severity,
            "ticket": ticket_text[:60] + "..."
        })

        st.session_state.history = st.session_state.history[:3]

        st.success("✨ Developer-ready task generated successfully!")
        st.balloons()


result = st.session_state.last_result

if result:
    st.divider()
    st.subheader("📊 Analysis Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Issue Category", result["category"])

    with col2:
        st.markdown(severity_badge(result["severity"]), unsafe_allow_html=True)

    with col3:
        confidence_percent = int(result["confidence"] * 100)
        st.metric("Confidence", f"{confidence_percent}%")
        st.progress(result["confidence"])

    with st.expander("🤔 Why this classification?"):
        if result["detected_keywords"]:
            st.write("Detected keywords:")
            st.code(", ".join(result["detected_keywords"]))
        else:
            st.write("No strong keyword match found.")

        st.write(
            "Ticket2Fix uses the ticket content and repository context to identify the likely workflow. "
            "IBM Bob notes can be added to improve repository-aware reasoning."
        )

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🧾 Ticket Analysis",
        "🧠 Repo Context",
        "👨‍💻 Developer Task",
        "🧪 Test Plan",
        "📦 Export"
    ])

    with tab1:
        st.markdown(result["ticket_analysis"])
        st.code(result["ticket_analysis"], language="markdown")

    with tab2:
        st.markdown(result["repo_analysis"])
        st.code(result["repo_analysis"], language="markdown")

    with tab3:
        st.markdown(result["developer_task"])
        st.code(result["developer_task"], language="markdown")

    with tab4:
        st.markdown(result["test_plan"])
        st.code(result["test_plan"], language="markdown")

    with tab5:
        st.subheader("Export Analysis")

        export_format = st.radio(
            "Choose export format",
            ["Markdown", "JSON", "Plain Text"],
            horizontal=True
        )

        markdown_export = f"""
# Ticket2Fix Analysis Report

## Repository
{result["repo_url"] or "No repository URL provided"}

## Category
{result["category"]}

## Severity
{result["severity"]}

## Confidence
{int(result["confidence"] * 100)}%

---

{result["ticket_analysis"]}

---

{result["repo_analysis"]}

---

{result["developer_task"]}

---

{result["test_plan"]}

---

## IBM Bob Usage

IBM Bob supports this workflow by helping developers understand repository structure,
reason about likely affected files, generate documentation, and suggest relevant tests.
"""

        json_export = json.dumps(result, indent=2)

        plain_text_export = markdown_export.replace("#", "").replace("*", "")

        if export_format == "Markdown":
            export_data = markdown_export
            file_name = "ticket2fix-analysis.md"
            mime_type = "text/markdown"
        elif export_format == "JSON":
            export_data = json_export
            file_name = "ticket2fix-analysis.json"
            mime_type = "application/json"
        else:
            export_data = plain_text_export
            file_name = "ticket2fix-analysis.txt"
            mime_type = "text/plain"

        st.download_button(
            label=f"📥 Download {export_format}",
            data=export_data,
            file_name=file_name,
            mime=mime_type,
            use_container_width=True
        )


st.divider()

st.subheader("🤖 IBM Bob Usage Section")

st.markdown("""
Ticket2Fix is designed to demonstrate how IBM Bob supports software development workflows.

IBM Bob helps with:

- Understanding repository structure
- Locating likely affected files
- Explaining application logic
- Generating developer-ready tasks
- Suggesting debugging steps
- Producing documentation and test plans
- Reducing repetitive work between support and engineering teams

**Core message:** Ticket2Fix solves the communication gap before coding starts — the gap between support tickets and developer action.
""")