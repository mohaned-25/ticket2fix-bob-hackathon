def find_code_context(ticket_text, repo_url=""):
    text = ticket_text.lower()

    affected_areas = []
    files_to_inspect = []

    if "password" in text or "login" in text or "log in" in text:
        affected_areas.extend([
            "Authentication service",
            "Password reset controller",
            "Login UI component",
            "Session/token generation logic",
            "Frontend error handling"
        ])

        files_to_inspect.extend([
            "backend/auth.service.js",
            "backend/passwordReset.controller.js",
            "backend/routes/auth.routes.js",
            "frontend/LoginForm.tsx",
            "frontend/ResetPassword.tsx",
            "frontend/api/authClient.ts"
        ])

    elif "payment" in text or "checkout" in text:
        affected_areas.extend([
            "Payment service",
            "Checkout controller",
            "Order processing module",
            "Payment gateway integration",
            "Transaction logging"
        ])

        files_to_inspect.extend([
            "backend/payment.service.js",
            "backend/checkout.controller.js",
            "backend/routes/payment.routes.js",
            "frontend/CheckoutPage.tsx",
            "frontend/PaymentForm.tsx"
        ])

    elif "profile" in text or "account" in text:
        affected_areas.extend([
            "User profile service",
            "Account settings page",
            "User update endpoint",
            "Database user model"
        ])

        files_to_inspect.extend([
            "backend/user.service.js",
            "backend/profile.controller.js",
            "frontend/ProfilePage.tsx",
            "frontend/AccountSettings.tsx"
        ])

    else:
        affected_areas.extend([
            "Main application logic",
            "API routes",
            "Frontend component related to the issue",
            "Error handling layer",
            "Database interaction layer"
        ])

        files_to_inspect.extend([
            "backend/app.js",
            "backend/routes/index.js",
            "frontend/App.tsx",
            "frontend/api/client.ts"
        ])

    affected_areas_markdown = "\n".join([f"- {area}" for area in affected_areas])
    files_markdown = "\n".join([f"- `{file}`" for file in files_to_inspect])

    repo_display = repo_url if repo_url else "No repository URL provided"

    return f"""
## Repository Context

Repository:

`{repo_display}`

## Likely Affected Areas

{affected_areas_markdown}

## Files to Inspect

{files_markdown}

## IBM Bob Usage

IBM Bob can support this step by helping developers understand the repository structure, locate related files, explain code relationships, and reason about where the bug may exist.

## Developer Insight

The issue should first be investigated around the modules responsible for user authentication, state management, API response handling, and frontend error display.
"""