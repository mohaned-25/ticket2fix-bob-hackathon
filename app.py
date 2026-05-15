import streamlit as st

st.set_page_config(
    page_title="Ticket2Fix | IBM Bob Hackathon",
    page_icon="🛠️",
    layout="wide"
)

# -----------------------------
# Custom Styling
# -----------------------------
st.markdown("""
<style>
    .main {
        background-color: #f8fafc;
    }

    .hero-box {
        background: linear-gradient(135deg, #0f172a, #1e40af);
        padding: 2rem;
        border-radius: 18px;
        color: white;
        margin-bottom: 1.5rem;
    }

    .hero-title {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }

    .hero-subtitle {
        font-size: 1.1rem;
        color: #dbeafe;
    }

    .info-card {
        background-color: white;
        padding: 1.3rem;
        border-radius: 14px;
        border: 1px solid #e5e7eb;
        box-shadow: 0px 2px 8px rgba(15, 23, 42, 0.06);
        margin-bottom: 1rem;
    }

    .metric-card {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 14px;
        border-left: 5px solid #2563eb;
        box-shadow: 0px 2px 8px rgba(15, 23, 42, 0.06);
    }

    .footer {
        text-align: center;
        color: #64748b;
        font-size: 0.9rem;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)


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
        category = "Authentication / Access"
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
        category = "Payments / Checkout"
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
        category = "File Upload / Validation"
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
        category = "General Application Issue"
        tests = [
            "Reported issue can be reproduced.",
            "Expected behavior is restored.",
            "Error states are handled clearly.",
            "Relevant backend response codes are validated.",
            "Regression test is added."
        ]

    result = f"""
# Developer-Ready Analysis

## 1. Clean Bug Summary

The reported issue indicates that users are experiencing a problem that blocks or disrupts an expected workflow.

**Original ticket:**

> {ticket}

## 2. Issue Category

**{category}**

## 3. Severity / Priority

**{severity}**

## 4. Missing Information

The support ticket should be improved by collecting:

- Browser and device details
- User role or account type
- Exact timestamp of the issue
- Screenshots or screen recording
- Backend logs
- Network response status codes
- Whether the issue happens for all users or only specific users

## 5. Reproduction Steps

1. Open the affected feature in the application.
2. Follow the user workflow described in the support ticket.
3. Perform the action that triggers the issue.
4. Observe the application response.
5. Compare the actual result with the expected behavior.

## 6. Expected Behavior

The application should complete the user workflow successfully and provide clear feedback.

## 7. Actual Behavior

The user workflow fails or behaves unexpectedly, and the support ticket suggests that feedback may be missing or unclear.

## 8. Likely Affected Areas

{chr(10).join([f"- {area}" for area in likely_areas])}

## 9. Developer-Ready Task

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

## 10. Debugging Checklist

- Confirm the issue can be reproduced.
- Check browser console errors.
- Inspect network requests and API responses.
- Review backend logs.
- Verify validation rules.
- Confirm database or state changes.
- Check whether errors are displayed to users.
- Add logging if the failure is silent.

## 11. Suggested Tests

{chr(10).join([f"- {test}" for test in tests])}

## 12. Acceptance Criteria

- The issue is reproducible before the fix.
- The issue is resolved after the fix.
- The user receives clear feedback.
- Related tests are added.
- No regression is introduced in nearby functionality.

## 13. IBM Bob Usage

IBM Bob is used as the AI development partner to understand repository context, review workflows, suggest likely affected areas, improve documentation, generate testing ideas, and reduce repetitive triage work.
"""
    return result, category, severity, likely_areas, tests


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.title("🛠️ Ticket2Fix")

    st.markdown("""
    **AI Support-to-Code Assistant**  
    powered by **IBM Bob**
    """)

    st.divider()

    st.subheader("Demo Steps")
    st.markdown("""
    1. Choose a sample ticket  
    2. Add project context  
    3. Generate developer task  
    4. Review debugging checklist  
    5. Download Markdown output  
    """)

    st.divider()

    st.subheader("Best Demo Input")
    st.info("Use the Authentication issue for the final hackathon demo.")

    st.divider()

    st.markdown("""
    **Hackathon:** IBM Bob Hackathon  
    **Stack:** Python + Streamlit  
    **Focus:** Developer productivity
    """)


# -----------------------------
# Hero Section
# -----------------------------
st.markdown("""
<div class="hero-box">
    <div class="hero-title">Ticket2Fix</div>
    <div class="hero-subtitle">
        Turn vague support tickets into developer-ready engineering tasks with IBM Bob.
    </div>
</div>
""", unsafe_allow_html=True)


# -----------------------------
# Value Cards
# -----------------------------
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.markdown("""
    <div class="metric-card">
        <h4>Support Teams</h4>
        <p>Convert unclear reports into structured tickets.</p>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("""
    <div class="metric-card">
        <h4>Developers</h4>
        <p>Get reproduction steps, debugging checklist, and affected areas.</p>
    </div>
    """, unsafe_allow_html=True)

with col_c:
    st.markdown("""
    <div class="metric-card">
        <h4>QA Teams</h4>
        <p>Generate acceptance criteria and suggested regression tests.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()


# -----------------------------
# Main App Layout
# -----------------------------
left_col, right_col = st.columns([0.95, 1.05])

with left_col:
    st.markdown('<div class="info-card">', unsafe_allow_html=True)

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
        value="React frontend, Node.js backend, authentication service, password reset controller, login form component, session token generation, frontend error handling." if sample_choice == "Authentication issue" else "",
        height=140,
        placeholder="Example: React frontend, Node.js backend, authentication module, password reset flow..."
    )

    generate = st.button("Generate Developer Task", type="primary", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)


with right_col:
    st.markdown('<div class="info-card">', unsafe_allow_html=True)

    st.header("Output")

    if generate:
        if not ticket.strip():
            st.warning("Please enter a support ticket first.")
        else:
            analysis, category, severity, likely_areas, tests = analyze_ticket(ticket, project_context)

            st.success("Developer-ready task generated successfully.")

            metric_1, metric_2 = st.columns(2)
            with metric_1:
                st.metric("Issue Category", category)
            with metric_2:
                st.metric("Likely Areas", len(likely_areas))

            st.markdown(analysis)

            st.download_button(
                label="Download Analysis as Markdown",
                data=analysis,
                file_name="ticket2fix-analysis.md",
                mime="text/markdown",
                use_container_width=True
            )
    else:
        st.info("Enter a support ticket and click Generate Developer Task.")

    st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------
# About Section
# -----------------------------
st.divider()

st.markdown("""
## Why Ticket2Fix matters

Support tickets are often incomplete, vague, and difficult for developers to act on. Ticket2Fix reduces the communication gap between support and engineering by turning messy tickets into clear, structured, developer-ready tasks.

## How IBM Bob supports the workflow

IBM Bob supports the project by helping understand repository context, improve the workflow, generate documentation, suggest test cases, and reduce repetitive development work.
""")

st.markdown("""
<div class="footer">
Built for the IBM Bob Hackathon | Ticket2Fix | AI Support-to-Code Assistant
</div>
""", unsafe_allow_html=True)
