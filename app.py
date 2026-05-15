import streamlit as st

st.set_page_config(
    page_title="Ticket2Fix",
    page_icon="🛠️",
    layout="wide"
)

SAMPLE_TICKETS = {
    "Authentication issue": """After resetting password, users cannot log in.
The page refreshes but does not show an error message.
This happens only after using the reset password link.""",

    "Payment issue": """Users are charged twice when clicking the checkout button multiple times.
The order is created only once, but two payment transactions appear.""",

    "Upload issue": """Users cannot upload profile pictures larger than 2MB.
The upload fails silently without showing any message."""
}


def analyze_ticket(ticket, project_context):
    ticket_lower = ticket.lower()

    if "password" in ticket_lower or "login" in ticket_lower or "auth" in ticket_lower:
        likely_areas = [
            "Authentication service",
            "Password reset controller",
            "Login form component",
            "Session or token generation logic",
            "Frontend error handling"
        ]
        severity = "High — authentication issue affecting user access."
        tests = [
            "Login succeeds after password reset.",
            "Login fails with the old password.",
            "Invalid reset token shows a clear error message.",
            "Expired reset token shows a clear error message.",
            "Empty password field displays validation feedback."
        ]

    elif "payment" in ticket_lower or "checkout" in ticket_lower or "charged" in ticket_lower:
        likely_areas = [
            "Checkout button component",
            "Payment processing service",
            "Order creation logic",
            "Transaction deduplication logic",
            "Backend payment webhook handler"
        ]
        severity = "Critical — payment issue that may cause financial impact."
        tests = [
            "Multiple checkout clicks do not create duplicate payments.",
            "Payment request is disabled after first submission.",
            "Order is created only once.",
            "Duplicate payment webhook events are ignored.",
            "User receives clear payment confirmation."
        ]

    elif "upload" in ticket_lower or "file" in ticket_lower or "picture" in ticket_lower:
        likely_areas = [
            "File upload component",
            "File size validation logic",
            "Backend upload endpoint",
            "Error message handling",
            "Storage service integration"
        ]
        severity = "Medium — user-facing feature issue with poor feedback."
        tests = [
            "Files smaller than the limit upload successfully.",
            "Files larger than the limit show a clear error.",
            "Unsupported file formats are rejected.",
            "Upload progress and failure states are displayed.",
            "Backend returns correct validation errors."
        ]

    else:
        likely_areas = [
            "Frontend component related to the reported feature",
            "Backend API endpoint",
            "Validation logic",
            "Error handling flow",
            "Data persistence layer"
        ]
        severity = "Medium — requires investigation."
        tests = [
            "Reported issue can be reproduced.",
            "Expected behavior is restored.",
            "Error states are handled clearly.",
            "Relevant backend response codes are validated.",
            "Regression test is added."
        ]

    result = f"""
## 1. Clean Bug Summary

The reported issue indicates that users are experiencing a problem that blocks or disrupts an expected workflow.

Original ticket:

> {ticket}

## 2. Severity / Priority

**{severity}**

## 3. Missing Information

The support ticket should be improved by collecting:

- Browser and device details
- User role or account type
- Exact timestamp of the issue
- Screenshots or screen recording
- Backend logs
- Network response status codes
- Whether the issue happens for all users or only specific users

## 4. Reproduction Steps

1. Open the affected feature in the application.
2. Follow the user workflow described in the support ticket.
3. Perform the action that triggers the issue.
4. Observe the application response.
5. Compare the actual result with the expected behavior.

## 5. Expected Behavior

The application should complete the user workflow successfully and provide clear feedback.

## 6. Actual Behavior

The user workflow fails or behaves unexpectedly, and the support ticket suggests that feedback may be missing or unclear.

## 7. Likely Affected Areas

{chr(10).join([f"- {area}" for area in likely_areas])}

## 8. Developer-Ready Task

### Problem

A user-facing issue was reported and needs developer investigation.

### Technical Context

{project_context if project_context else "No repository context was provided. Developer should inspect the related frontend, backend, validation, and error handling logic."}

### Suggested Fix Plan

1. Reproduce the issue locally.
2. Inspect the likely affected modules.
3. Check frontend validation and error states.
4. Check backend API responses and logs.
5. Implement the fix.
6. Add tests to prevent regression.
7. Update documentation if needed.

## 9. Debugging Checklist

- Confirm the issue can be reproduced.
- Check browser console errors.
- Inspect network requests and API responses.
- Review backend logs.
- Verify validation rules.
- Confirm database or state changes.
- Check whether errors are displayed to users.
- Add logging if the failure is silent.

## 10. Suggested Tests

{chr(10).join([f"- {test}" for test in tests])}

## 11. Acceptance Criteria

- The issue is reproducible before the fix.
- The issue is resolved after the fix.
- The user receives clear feedback.
- Related tests are added.
- No regression is introduced in nearby functionality.

## 12. IBM Bob Usage

IBM Bob is used as the AI development partner to understand the repository, review the workflow, suggest likely affected areas, improve documentation, generate testing ideas, and reduce repetitive triage work.
"""
    return result


st.title("🛠️ Ticket2Fix")
st.subheader("AI Support-to-Code Assistant powered by IBM Bob")

st.markdown("""
Ticket2Fix converts vague support tickets into developer-ready tasks, debugging steps, acceptance criteria, and test plans.

The project is designed for the IBM Bob Hackathon to demonstrate how repository-aware AI can improve the software development workflow.
""")

st.divider()

col1, col2 = st.columns([1, 1])

with col1:
    st.header("Input")

    sample_choice = st.selectbox(
        "Choose a sample ticket or write your own:",
        ["Custom ticket"] + list(SAMPLE_TICKETS.keys())
    )

    default_ticket = ""
    if sample_choice != "Custom ticket":
        default_ticket = SAMPLE_TICKETS[sample_choice]

    ticket = st.text_area(
        "Support ticket / bug report",
        value=default_ticket,
        height=220,
        placeholder="Paste a vague support ticket here..."
    )

    project_context = st.text_area(
        "Repository or project context",
        height=140,
        placeholder="Example: React frontend, Node.js backend, authentication module, password reset flow..."
    )

    generate = st.button("Generate Developer Task", type="primary")

with col2:
    st.header("Output")

    if generate:
        if not ticket.strip():
            st.warning("Please enter a support ticket first.")
        else:
            analysis = analyze_ticket(ticket, project_context)
            st.markdown(analysis)
            st.download_button(
                label="Download Analysis as Markdown",
                data=analysis,
                file_name="ticket2fix-analysis.md",
                mime="text/markdown"
            )
    else:
        st.info("Enter a support ticket and click Generate Developer Task.")

st.divider()

st.markdown("""
### Why Ticket2Fix matters

Support tickets are often incomplete and hard for developers to act on. Ticket2Fix reduces the communication gap between support and engineering by turning messy tickets into clear, structured, developer-ready tasks.

### Built with IBM Bob

IBM Bob supports the project by helping understand repository context, improve the workflow, generate documentation, suggest test cases, and reduce repetitive development work.
""")
