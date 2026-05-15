import streamlit as st
import time

st.set_page_config(
    page_title="Ticket2Fix | IBM Bob Hackathon",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# Custom Professional CSS
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(37, 99, 235, 0.18), transparent 32%),
            radial-gradient(circle at top right, rgba(14, 165, 233, 0.16), transparent 30%),
            linear-gradient(180deg, #f8fafc 0%, #eef2ff 100%);
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #020617 0%, #0f172a 55%, #111827 100%);
    }

    section[data-testid="stSidebar"] * {
        color: #e5e7eb !important;
    }

    .hero-container {
        position: relative;
        overflow: hidden;
        background: linear-gradient(135deg, #020617 0%, #1e3a8a 45%, #2563eb 100%);
        padding: 2.5rem 2.5rem;
        border-radius: 26px;
        color: white;
        box-shadow: 0 25px 60px rgba(15, 23, 42, 0.28);
        margin-bottom: 1.5rem;
        min-height: 245px;
    }

    .hero-container::before {
        content: "";
        position: absolute;
        width: 420px;
        height: 420px;
        border-radius: 999px;
        background: rgba(255,255,255,0.08);
        top: -170px;
        right: -120px;
    }

    .hero-container::after {
        content: "";
        position: absolute;
        width: 280px;
        height: 280px;
        border-radius: 999px;
        background: rgba(59,130,246,0.3);
        bottom: -120px;
        left: 40%;
    }

    .hero-content {
        position: relative;
        z-index: 5;
        max-width: 900px;
    }

    .hero-badge {
        display: inline-block;
        background: rgba(255,255,255,0.16);
        border: 1px solid rgba(255,255,255,0.22);
        padding: 0.45rem 0.85rem;
        border-radius: 999px;
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: 0.03em;
        margin-bottom: 1rem;
    }

    .hero-title {
        font-size: 3.4rem;
        line-height: 1.04;
        font-weight: 900;
        margin-bottom: 0.7rem;
        letter-spacing: -0.05em;
    }

    .hero-subtitle {
        font-size: 1.18rem;
        line-height: 1.7;
        color: #dbeafe;
        max-width: 780px;
    }

    .floating-icon {
        position: absolute;
        font-size: 2rem;
        opacity: 0.7;
        animation: float 4.5s ease-in-out infinite;
        z-index: 4;
    }

    .icon-one {
        top: 28px;
        right: 70px;
        animation-delay: 0s;
    }

    .icon-two {
        top: 125px;
        right: 180px;
        animation-delay: 1s;
    }

    .icon-three {
        bottom: 35px;
        right: 90px;
        animation-delay: 2s;
    }

    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-14px) rotate(4deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }

    .glass-card {
        background: rgba(255,255,255,0.86);
        backdrop-filter: blur(16px);
        padding: 1.35rem;
        border-radius: 22px;
        border: 1px solid rgba(226,232,240,0.95);
        box-shadow: 0 14px 35px rgba(15, 23, 42, 0.08);
        margin-bottom: 1rem;
    }

    .feature-card {
        background: white;
        padding: 1.35rem;
        border-radius: 20px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 10px 25px rgba(15, 23, 42, 0.06);
        min-height: 150px;
        transition: 0.25s ease;
    }

    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 18px 40px rgba(37, 99, 235, 0.16);
        border-color: #bfdbfe;
    }

    .feature-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }

    .feature-title {
        font-size: 1.05rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 0.35rem;
    }

    .feature-text {
        font-size: 0.92rem;
        color: #475569;
        line-height: 1.55;
    }

    .section-title {
        font-size: 1.45rem;
        font-weight: 850;
        color: #0f172a;
        margin-bottom: 0.4rem;
    }

    .section-subtitle {
        color: #64748b;
        font-size: 0.95rem;
        margin-bottom: 1rem;
    }

    .pill {
        display: inline-block;
        padding: 0.35rem 0.7rem;
        border-radius: 999px;
        font-size: 0.78rem;
        font-weight: 700;
        margin-right: 0.35rem;
        margin-bottom: 0.35rem;
        background: #dbeafe;
        color: #1e40af;
        border: 1px solid #bfdbfe;
    }

    .pill-green {
        background: #dcfce7;
        color: #166534;
        border: 1px solid #bbf7d0;
    }

    .pill-purple {
        background: #ede9fe;
        color: #5b21b6;
        border: 1px solid #ddd6fe;
    }

    .pill-orange {
        background: #ffedd5;
        color: #9a3412;
        border: 1px solid #fed7aa;
    }

    .output-box {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 1.3rem;
        box-shadow: 0 10px 25px rgba(15, 23, 42, 0.06);
    }

    .mini-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        color: #64748b;
        font-weight: 800;
        letter-spacing: 0.08em;
        margin-bottom: 0.3rem;
    }

    .footer {
        text-align: center;
        color: #64748b;
        font-size: 0.9rem;
        margin-top: 2rem;
        padding: 1.2rem;
    }

    .sidebar-title {
        font-size: 1.55rem;
        font-weight: 900;
        color: white;
        margin-bottom: 0.3rem;
    }

    .sidebar-subtitle {
        font-size: 0.9rem;
        color: #cbd5e1;
        line-height: 1.5;
    }

    .sidebar-box {
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 16px;
        padding: 1rem;
        margin-bottom: 1rem;
    }

    div[data-testid="stMetric"] {
        background: white;
        padding: 1rem;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 8px 20px rgba(15, 23, 42, 0.05);
    }

    .stButton > button {
        border-radius: 14px !important;
        font-weight: 800 !important;
        padding: 0.75rem 1rem !important;
        background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
        border: none !important;
        color: white !important;
        box-shadow: 0 12px 25px rgba(37, 99, 235, 0.25);
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #1d4ed8, #1e40af) !important;
        transform: translateY(-1px);
    }

    .stDownloadButton > button {
        border-radius: 14px !important;
        font-weight: 800 !important;
        padding: 0.7rem 1rem !important;
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# Sample Tickets
# ---------------------------------------------------------
SAMPLE_TICKETS = {
    "Authentication issue": """After resetting password, users cannot log in.
The page refreshes but does not show an error message.
This happens only after using the reset password link.""",

    "Payment issue": """Users are charged twice when clicking the checkout button multiple times.
The order is created only once, but two payment transactions appear.""",

    "Upload issue": """Users cannot upload profile pictures larger than 2MB.
The upload fails silently without showing any message.""",

    "Dashboard issue": """The analytics dashboard does not load for some users.
The loading spinner keeps running forever.
Refreshing the page sometimes fixes the issue."""
}


# ---------------------------------------------------------
# Analysis Logic
# ---------------------------------------------------------
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
        business_impact = "Users may be blocked from accessing the product after resetting their password."
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
        business_impact = "Duplicate charges can create financial risk, refund workload, and customer trust issues."
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
        business_impact = "Users may fail to complete profile setup or content submission due to unclear upload errors."
        tests = [
            "Files smaller than the limit upload successfully.",
            "Files larger than the limit show a clear error.",
            "Unsupported file formats are rejected.",
            "Upload progress and failure states are displayed.",
            "Backend returns correct validation errors."
        ]

    elif "dashboard" in ticket_lower or "analytics" in ticket_lower or "spinner" in ticket_lower:
        likely_areas = [
            "Dashboard component",
            "Analytics API endpoint",
            "Frontend loading state",
            "Data fetching hook",
            "Error boundary or fallback UI"
        ]
        severity = "Medium — visibility issue affecting user access to analytics."
        category = "Dashboard / Data Loading"
        business_impact = "Users may lose access to key reporting information and decision-making dashboards."
        tests = [
            "Dashboard loads successfully for valid users.",
            "API timeout shows a friendly error message.",
            "Loading spinner stops after failed requests.",
            "Retry behavior works correctly.",
            "Empty data state is displayed clearly."
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
        business_impact = "The issue may disrupt user workflow and requires engineering triage."
        tests = [
            "Reported issue can be reproduced.",
            "Expected behavior is restored.",
            "Error states are handled clearly.",
            "Relevant backend response codes are validated.",
            "Regression test is added."
        ]

    analysis = f"""
# Developer-Ready Analysis

## 1. Clean Bug Summary

The reported issue indicates that users are experiencing a problem that blocks or disrupts an expected workflow.

**Original ticket:**

> {ticket}

## 2. Issue Category

**{category}**

## 3. Severity / Priority

**{severity}**

## 4. Business Impact

{business_impact}

## 5. Missing Information

The support ticket should be improved by collecting:

- Browser and device details
- User role or account type
- Exact timestamp of the issue
- Screenshots or screen recording
- Backend logs
- Network response status codes
- Whether the issue happens for all users or only specific users

## 6. Reproduction Steps

1. Open the affected feature in the application.
2. Follow the user workflow described in the support ticket.
3. Perform the action that triggers the issue.
4. Observe the application response.
5. Compare the actual result with the expected behavior.

## 7. Expected Behavior

The application should complete the user workflow successfully and provide clear feedback.

## 8. Actual Behavior

The user workflow fails or behaves unexpectedly, and the support ticket suggests that feedback may be missing or unclear.

## 9. Likely Affected Areas

{chr(10).join([f"- {area}" for area in likely_areas])}

## 10. Developer-Ready Task

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

## 11. Debugging Checklist

- Confirm the issue can be reproduced.
- Check browser console errors.
- Inspect network requests and API responses.
- Review backend logs.
- Verify validation rules.
- Confirm database or state changes.
- Check whether errors are displayed to users.
- Add logging if the failure is silent.

## 12. Suggested Tests

{chr(10).join([f"- {test}" for test in tests])}

## 13. Acceptance Criteria

- The issue is reproducible before the fix.
- The issue is resolved after the fix.
- The user receives clear feedback.
- Related tests are added.
- No regression is introduced in nearby functionality.

## 14. IBM Bob Usage

IBM Bob is used as the AI development partner to understand repository context, review workflows, suggest likely affected areas, improve documentation, generate testing ideas, and reduce repetitive triage work.
"""

    return analysis, category, severity, business_impact, likely_areas, tests


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("""
    <div class="sidebar-title">🛠️ Ticket2Fix</div>
    <div class="sidebar-subtitle">
        AI Support-to-Code Assistant<br>
        powered by <b>IBM Bob</b>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.markdown("""
    <div class="sidebar-box">
        <b>🚀 Demo Flow</b><br><br>
        1. Select a sample ticket<br>
        2. Add repository context<br>
        3. Generate developer task<br>
        4. Review tests and checklist<br>
        5. Download Markdown output
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-box">
        <b>🏆 Hackathon Focus</b><br><br>
        Developer productivity<br>
        Support-to-engineering workflow<br>
        Repository-aware AI usage<br>
        Testing and documentation
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-box">
        <b>✅ Best Demo Input</b><br><br>
        Use <b>Authentication issue</b> for the final video demo.
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.caption("Built for IBM Bob Hackathon")

# ---------------------------------------------------------
# Hero
# ---------------------------------------------------------
st.markdown("""
<div class="hero-container">
    <div class="floating-icon icon-one">🤖</div>
    <div class="floating-icon icon-two">🧠</div>
    <div class="floating-icon icon-three">⚙️</div>

    <div class="hero-content">
        <div class="hero-badge">IBM Bob Hackathon · Developer Productivity · AI Workflow</div>
        <div class="hero-title">Ticket2Fix</div>
        <div class="hero-subtitle">
            Transform vague support tickets into clear, testable, developer-ready engineering tasks.
            Designed to reduce the communication gap between support teams and software developers.
        </div>
        <br>
        <span class="pill">🛠️ Developer Tools</span>
        <span class="pill pill-green">✅ Test Planning</span>
        <span class="pill pill-purple">🤖 IBM Bob</span>
        <span class="pill pill-orange">⚡ Faster Triage</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# Product Value Cards
# ---------------------------------------------------------
st.markdown('<div class="section-title">Built for real software teams</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Ticket2Fix helps support, engineering, and QA teams move from issue report to fix plan faster.</div>', unsafe_allow_html=True)

card1, card2, card3, card4 = st.columns(4)

with card1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎧</div>
        <div class="feature-title">Support Teams</div>
        <div class="feature-text">
            Turn unclear user complaints into structured engineering tickets.
        </div>
    </div>
    """, unsafe_allow_html=True)

with card2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">👨‍💻</div>
        <div class="feature-title">Developers</div>
        <div class="feature-text">
            Get likely affected areas, reproduction steps, and debugging checklists.
        </div>
    </div>
    """, unsafe_allow_html=True)

with card3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🧪</div>
        <div class="feature-title">QA Teams</div>
        <div class="feature-text">
            Generate test ideas, regression checks, and acceptance criteria.
        </div>
    </div>
    """, unsafe_allow_html=True)

with card4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📚</div>
        <div class="feature-title">Documentation</div>
        <div class="feature-text">
            Export consistent Markdown summaries for GitHub, Jira, or internal docs.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()


# ---------------------------------------------------------
# Main Workspace
# ---------------------------------------------------------
left_col, right_col = st.columns([0.9, 1.1], gap="large")

with left_col:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.markdown('<div class="section-title">🎫 Ticket Input</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">Choose a sample issue or paste your own support ticket.</div>', unsafe_allow_html=True)

    sample_choice = st.selectbox(
        "Sample ticket",
        ["Custom ticket"] + list(SAMPLE_TICKETS.keys())
    )

    default_ticket = ""
    if sample_choice != "Custom ticket":
        default_ticket = SAMPLE_TICKETS[sample_choice]

    ticket = st.text_area(
        "Support ticket / bug report",
        value=default_ticket,
        height=220,
        placeholder="Example: User cannot log in after resetting password..."
    )

    default_context = ""
    if sample_choice == "Authentication issue":
        default_context = "React frontend, Node.js backend, authentication service, password reset controller, login form component, session token generation, frontend error handling."
    elif sample_choice == "Payment issue":
        default_context = "React checkout page, Node.js API, payment provider integration, order service, webhook handler, transaction deduplication."
    elif sample_choice == "Upload issue":
        default_context = "Frontend upload component, Python backend API, file size validation, storage service, user profile module."
    elif sample_choice == "Dashboard issue":
        default_context = "React analytics dashboard, REST API, data fetching hook, loading state, error boundary, reporting service."

    project_context = st.text_area(
        "Repository / project context",
        value=default_context,
        height=145,
        placeholder="Example: React frontend, Node.js backend, authentication module, password reset flow..."
    )

    generate = st.button("✨ Generate Developer-Ready Task", type="primary", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <div class="section-title">🤖 IBM Bob Role</div>
        <div class="section-subtitle">
            IBM Bob supports repository understanding, workflow review, documentation, test planning,
            and development acceleration.
        </div>
        <span class="pill">Repo Context</span>
        <span class="pill pill-green">Code Review</span>
        <span class="pill pill-purple">Docs</span>
        <span class="pill pill-orange">Tests</span>
    </div>
    """, unsafe_allow_html=True)


with right_col:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)

    st.markdown('<div class="section-title">📌 Generated Engineering Output</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-subtitle">The generated result is structured for developers, QA, and support teams.</div>', unsafe_allow_html=True)

    if generate:
        if not ticket.strip():
            st.warning("Please enter a support ticket first.")
        else:
            with st.spinner("Analyzing ticket and preparing developer-ready output..."):
                time.sleep(0.8)

            analysis, category, severity, business_impact, likely_areas, tests = analyze_ticket(ticket, project_context)

            st.success("Developer-ready task generated successfully.")

            metric1, metric2, metric3 = st.columns(3)
            with metric1:
                st.metric("Category", category)
            with metric2:
                st.metric("Affected Areas", len(likely_areas))
            with metric3:
                st.metric("Suggested Tests", len(tests))

            tab1, tab2, tab3, tab4 = st.tabs([
                "📄 Summary",
                "🧭 Debug Plan",
                "🧪 Tests",
                "📥 Full Export"
            ])

            with tab1:
                st.markdown("### Clean Bug Summary")
                st.markdown("The reported issue indicates that users are experiencing a problem that blocks or disrupts an expected workflow.")

                st.markdown("### Severity / Priority")
                st.info(severity)

                st.markdown("### Business Impact")
                st.warning(business_impact)

                st.markdown("### Likely Affected Areas")
                for area in likely_areas:
                    st.markdown(f"- `{area}`")

            with tab2:
                st.markdown("### Reproduction Steps")
                st.markdown("""
                1. Open the affected feature in the application.
                2. Follow the user workflow described in the support ticket.
                3. Perform the action that triggers the issue.
                4. Observe the application response.
                5. Compare the actual result with the expected behavior.
                """)

                st.markdown("### Debugging Checklist")
                st.markdown("""
                - Confirm the issue can be reproduced.
                - Check browser console errors.
                - Inspect network requests and API responses.
                - Review backend logs.
                - Verify validation rules.
                - Confirm database or state changes.
                - Check whether errors are displayed to users.
                - Add logging if the failure is silent.
                """)

            with tab3:
                st.markdown("### Suggested Tests")
                for test in tests:
                    st.markdown(f"- ✅ {test}")

                st.markdown("### Acceptance Criteria")
                st.markdown("""
                - The issue is reproducible before the fix.
                - The issue is resolved after the fix.
                - The user receives clear feedback.
                - Related tests are added.
                - No regression is introduced in nearby functionality.
                """)

            with tab4:
                st.markdown("### Full Markdown Output")
                st.markdown(analysis)

                st.download_button(
                    label="📥 Download Analysis as Markdown",
                    data=analysis,
                    file_name="ticket2fix-analysis.md",
                    mime="text/markdown",
                    use_container_width=True
                )

    else:
        st.info("Choose a sample ticket or paste your own ticket, then click Generate Developer-Ready Task.")

        st.markdown("""
        <div class="output-box">
            <div class="mini-label">Preview</div>
            <b>Generated output will include:</b><br><br>
            ✅ Clean bug summary<br>
            ✅ Severity and business impact<br>
            ✅ Missing information checklist<br>
            ✅ Reproduction steps<br>
            ✅ Likely affected areas<br>
            ✅ Debugging checklist<br>
            ✅ Suggested tests<br>
            ✅ Acceptance criteria<br>
            ✅ Markdown export
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------------
# Workflow Section
# ---------------------------------------------------------
st.divider()

st.markdown('<div class="section-title">How the workflow works</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">A simple but practical flow from vague report to developer action.</div>', unsafe_allow_html=True)

flow1, flow2, flow3, flow4, flow5 = st.columns(5)

with flow1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🎫</div>
        <div class="feature-title">1. Ticket</div>
        <div class="feature-text">Paste an unclear support ticket or bug report.</div>
    </div>
    """, unsafe_allow_html=True)

with flow2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🧠</div>
        <div class="feature-title">2. Context</div>
        <div class="feature-text">Add project or repository context for better analysis.</div>
    </div>
    """, unsafe_allow_html=True)

with flow3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🤖</div>
        <div class="feature-title">3. IBM Bob</div>
        <div class="feature-text">Use IBM Bob to support repo understanding and workflow review.</div>
    </div>
    """, unsafe_allow_html=True)

with flow4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🛠️</div>
        <div class="feature-title">4. Dev Task</div>
        <div class="feature-text">Generate a clear engineering task and debugging plan.</div>
    </div>
    """, unsafe_allow_html=True)

with flow5:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🧪</div>
        <div class="feature-title">5. Tests</div>
        <div class="feature-text">Create acceptance criteria and regression test ideas.</div>
    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------------
# Business Value Section
# ---------------------------------------------------------
st.divider()

value_col1, value_col2 = st.columns([1, 1], gap="large")

with value_col1:
    st.markdown("""
    <div class="glass-card">
        <div class="section-title">📈 Business Value</div>
        <div class="section-subtitle">
            Ticket2Fix reduces friction between support and engineering.
        </div>
        <ul>
            <li>Reduces back-and-forth between support and developers</li>
            <li>Improves bug report quality</li>
            <li>Speeds up engineering triage</li>
            <li>Helps junior developers understand issues faster</li>
            <li>Encourages consistent testing and acceptance criteria</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with value_col2:
    st.markdown("""
    <div class="glass-card">
        <div class="section-title">🏆 Hackathon Alignment</div>
        <div class="section-subtitle">
            The project demonstrates how IBM Bob can support real developer workflows.
        </div>
        <ul>
            <li>Improves how software is built</li>
            <li>Uses repository-aware AI development assistance</li>
            <li>Reduces repetitive triage work</li>
            <li>Supports documentation and test planning</li>
            <li>Creates practical value for real software teams</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.markdown("""
<div class="footer">
    <b>Ticket2Fix</b> · AI Support-to-Code Assistant · Built for the IBM Bob Hackathon<br>
    Turning messy support tickets into developer-ready engineering tasks.
</div>
""", unsafe_allow_html=True)
