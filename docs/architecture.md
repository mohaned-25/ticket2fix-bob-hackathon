# Architecture

Ticket2Fix uses a simple single-page workflow.

## Input

The user provides:

- Support ticket or bug report
- Optional repository or project context

## Processing

The application analyzes the support ticket and generates a structured developer task.

## Output

Ticket2Fix generates:

- Clean bug summary
- Severity
- Missing information
- Reproduction steps
- Expected behavior
- Actual behavior
- Likely affected areas
- Debugging checklist
- Suggested tests
- Acceptance criteria

## IBM Bob Role

IBM Bob is used to understand the project repository, review the workflow, suggest improvements, generate documentation, and support test planning.
# Ticket2Fix Architecture Analysis & Improvement Plan

## Executive Summary

Ticket2Fix is a Streamlit-based web application that converts vague support tickets into structured, developer-ready tasks. The current implementation uses rule-based text analysis with hardcoded templates, making it suitable for a hackathon MVP but with significant room for enhancement.

---

## Current Architecture

### System Overview

```
┌─────────────────┐
│   User Input    │
│  - Ticket Text  │
│  - Project Ctx  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   app.py        │
│  (Streamlit UI) │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────┐
│     analyze_ticket()                │
│  Orchestrates analysis pipeline     │
└────────┬────────────────────────────┘
         │
         ├──────────────┬──────────────┬──────────────┐
         ▼              ▼              ▼              ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ticket_       │ │repo_         │ │task_         │ │test_         │
│analyzer.py   │ │context.py    │ │generator.py  │ │generator.py  │
│              │ │              │ │              │ │              │
│- Severity    │ │- Affected    │ │- Dev Task    │ │- Test Plan   │
│- Summary     │ │  Areas       │ │- Debugging   │ │- Test Cases  │
│              │ │- Files       │ │- Criteria    │ │              │
└──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘
         │              │              │              │
         └──────────────┴──────────────┴──────────────┘
                        │
                        ▼
                ┌──────────────┐
                │   Markdown   │
                │    Output    │
                └──────────────┘
```

### Component Breakdown

#### 1. **[`app.py`](app.py)** - Main Application (256 lines)
- **Purpose**: Streamlit UI and orchestration
- **Key Functions**:
  - [`analyze_ticket(ticket, project_context)`](app.py:22-185) - Main orchestration function
  - UI layout with two-column design
  - Sample ticket selection
  - Markdown download functionality

#### 2. **[`src/ticket_analyzer.py`](src/ticket_analyzer.py)** - Ticket Analysis
- **Purpose**: Extract severity and structure ticket information
- **Key Functions**:
  - [`estimate_severity(ticket_text)`](src/ticket_analyzer.py:1-22) - Rule-based severity detection
  - [`analyze_ticket(ticket_text)`](src/ticket_analyzer.py:25-69) - Generate bug summary

#### 3. **[`src/repo_context.py`](src/repo_context.py)** - Repository Context
- **Purpose**: Identify affected code areas and files
- **Key Functions**:
  - [`find_code_context(ticket_text, repo_url)`](src/repo_context.py:1-100) - Keyword-based file mapping

#### 4. **[`src/task_generator.py`](src/task_generator.py)** - Task Generation
- **Purpose**: Create developer-ready task descriptions
- **Key Functions**:
  - [`generate_developer_task(ticket_text, ticket_analysis, repo_analysis)`](src/task_generator.py:1-56) - Template-based task generation

#### 5. **[`src/test_generator.py`](src/test_generator.py)** - Test Planning
- **Purpose**: Generate test plans and test cases
- **Key Functions**:
  - [`generate_test_plan(ticket_text, repo_analysis)`](src/test_generator.py:1-56) - Template-based test generation

---

## Data Flow Analysis

### Input Processing
1. User enters support ticket text (required)
2. User optionally provides project context
3. User clicks "Generate Developer Task" button

### Analysis Pipeline
1. **Ticket Analysis** → Severity estimation via keyword matching
2. **Repository Context** → Affected areas identified via keyword patterns
3. **Task Generation** → Hardcoded template with placeholders
4. **Test Generation** → Hardcoded test scenarios based on keywords

### Output Generation
- Markdown-formatted comprehensive analysis
- Downloadable `.md` file
- Displayed in Streamlit UI

---

## Current Strengths

### ✅ What Works Well

1. **Simple & Fast**: No external API dependencies, instant results
2. **Clear UX**: Two-column layout with sample tickets for easy testing
3. **Comprehensive Output**: Covers all essential aspects (severity, debugging, tests, acceptance criteria)
4. **Hackathon-Ready**: Functional demo with minimal setup
5. **Modular Design**: Separated concerns across multiple files
6. **Download Feature**: Users can export analysis as markdown

---

## Critical Weaknesses

### ❌ Major Limitations

#### 1. **No AI Integration**
- **Issue**: Despite being marketed as "AI-powered", uses only keyword matching
- **Impact**: Cannot understand context, nuance, or complex scenarios
- **Evidence**: All functions use simple `text.lower()` and `if word in text` checks

#### 2. **Hardcoded Templates**
- **Issue**: All outputs are static templates with minimal customization
- **Impact**: Generic, repetitive responses regardless of ticket content
- **Example**: [`task_generator.py`](src/task_generator.py:2-56) returns same structure for all tickets

#### 3. **No Real Repository Analysis**
- **Issue**: [`repo_context.py`](src/repo_context.py) doesn't actually analyze repositories
- **Impact**: Cannot provide accurate file paths or code context
- **Evidence**: Hardcoded file suggestions like `auth_service.py`, `login_controller.py`

#### 4. **Limited Severity Detection**
- **Issue**: Only 3 severity levels with basic keyword matching
- **Impact**: Cannot distinguish between critical production issues and minor bugs
- **Code**: [`estimate_severity()`](src/ticket_analyzer.py:1-22) uses 6 keywords total

#### 5. **No Validation or Error Handling**
- **Issue**: No input validation, error handling, or edge case management
- **Impact**: Could break with unexpected inputs

#### 6. **Static Test Generation**
- **Issue**: Test plans are generic templates, not ticket-specific
- **Impact**: Developers get boilerplate instead of actionable test cases

---

## 48-Hour Hackathon MVP Improvements

### Priority 1: Critical (Must-Have) - 8 hours

#### 1.1 Add Real AI Integration (4 hours)
**Goal**: Replace keyword matching with actual AI analysis

**Implementation**:
- Integrate OpenAI API or Anthropic Claude
- Create prompt templates for each analysis type
- Add API key configuration via environment variables
- Implement error handling for API failures

**Files to Modify**:
- [`src/ticket_analyzer.py`](src/ticket_analyzer.py) - Replace [`estimate_severity()`](src/ticket_analyzer.py:1-22)
- [`src/repo_context.py`](src/repo_context.py) - Replace [`find_code_context()`](src/repo_context.py:1-100)
- [`src/task_generator.py`](src/task_generator.py) - Dynamic generation
- [`src/test_generator.py`](src/test_generator.py) - Context-aware tests

**Expected Outcome**: Intelligent, context-aware analysis instead of templates

#### 1.2 Improve UI/UX (2 hours)
**Goal**: Make the demo more impressive and user-friendly

**Enhancements**:
- Add loading spinner during analysis
- Show progress indicators for each analysis step
- Add success/error notifications
- Improve visual hierarchy with better styling
- Add copy-to-clipboard buttons for each section

**Files to Modify**:
- [`app.py`](app.py) - UI enhancements

#### 1.3 Add Input Validation (1 hour)
**Goal**: Prevent errors and improve reliability

**Implementation**:
- Validate ticket text (min length, not empty)
- Sanitize inputs to prevent injection
- Add helpful error messages
- Handle edge cases gracefully

**Files to Modify**:
- [`app.py`](app.py:213-218) - Add validation before analysis

#### 1.4 Enhanced Sample Tickets (1 hour)
**Goal**: Better demonstrate capabilities

**Implementation**:
- Add 5-7 diverse, realistic sample tickets
- Include different severity levels
- Cover various domains (auth, payments, uploads, performance, security)
- Add edge cases to showcase AI capabilities

**Files to Modify**:
- [`app.py`](app.py:9-19) - Expand SAMPLE_TICKETS

---

### Priority 2: High-Value (Should-Have) - 6 hours

#### 2.1 GitHub Integration (3 hours)
**Goal**: Actually analyze real repositories

**Implementation**:
- Add GitHub API integration
- Fetch repository structure and README
- Analyze file patterns and naming conventions
- Suggest actual file paths based on repo structure

**New Files**:
- `src/github_analyzer.py` - GitHub API integration

**Files to Modify**:
- [`src/repo_context.py`](src/repo_context.py) - Use real repo data
- [`app.py`](app.py:220-224) - Add GitHub URL input field

#### 2.2 Ticket History & Comparison (2 hours)
**Goal**: Allow users to compare multiple analyses

**Implementation**:
- Store analysis history in session state
- Add sidebar with previous analyses
- Allow side-by-side comparison
- Export multiple analyses as batch

**Files to Modify**:
- [`app.py`](app.py) - Add session state management

#### 2.3 Customizable Output Templates (1 hour)
**Goal**: Let users choose output format

**Implementation**:
- Add template selection (Jira, GitHub Issues, Linear, Plain)
- Allow custom field selection
- Export in different formats (Markdown, JSON, HTML)

**Files to Modify**:
- [`app.py`](app.py) - Add template selector
- All generator files - Support multiple formats

---

### Priority 3: Nice-to-Have (Could-Have) - 4 hours

#### 3.1 Analytics Dashboard (2 hours)
**Goal**: Show insights about ticket patterns

**Implementation**:
- Track severity distribution
- Show most common affected areas
- Display average analysis time
- Visualize trends with charts

**New Files**:
- `src/analytics.py` - Analytics tracking

#### 3.2 Batch Processing (1 hour)
**Goal**: Analyze multiple tickets at once

**Implementation**:
- Upload CSV of tickets
- Process in parallel
- Export batch results
- Show summary statistics

**Files to Modify**:
- [`app.py`](app.py) - Add file upload

#### 3.3 AI Model Selection (1 hour)
**Goal**: Let users choose AI provider

**Implementation**:
- Support multiple AI providers (OpenAI, Anthropic, local models)
- Add model selection dropdown
- Show cost estimates
- Compare model performance

**Files to Modify**:
- [`app.py`](app.py) - Add model selector
- All analysis files - Support multiple providers

---

## Recommended Architecture for Enhanced Version

```
┌─────────────────────────────────────────────────────────┐
│                    Streamlit UI Layer                    │
│  - Input Forms  - Progress Indicators  - Results Display │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│              Orchestration Layer (app.py)                │
│  - Request Validation  - Session Management  - Caching   │
└────────────────────────┬────────────────────────────────┘
                         │
         ┌───────────────┼───────────────┐
         ▼               ▼               ▼
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│   AI Layer  │  │  GitHub API │  │  Analytics  │
│             │  │             │  │             │
│ - OpenAI    │  │ - Repo Data │  │ - Tracking  │
│ - Anthropic │  │ - File Tree │  │ - Metrics   │
│ - Prompts   │  │ - README    │  │ - Insights  │
└──────┬──────┘  └──────┬──────┘  └──────┬──────┘
       │                │                │
       └────────────────┼────────────────┘
                        │
         ┌──────────────┼──────────────┐
         ▼              ▼              ▼
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│  Analyzer   │  │  Generator  │  │   Exporter  │
│             │  │             │  │             │
│ - Severity  │  │ - Tasks     │  │ - Markdown  │
│ - Context   │  │ - Tests     │  │ - JSON      │
│ - Patterns  │  │ - Criteria  │  │ - HTML      │
└─────────────┘  └─────────────┘  └─────────────┘
```

---

## Implementation Roadmap

### Phase 1: Foundation (Hours 0-8)
- [ ] Set up AI API integration
- [ ] Replace keyword matching with AI calls
- [ ] Add input validation
- [ ] Improve UI with loading states
- [ ] Expand sample tickets

### Phase 2: Enhancement (Hours 8-14)
- [ ] Integrate GitHub API
- [ ] Add ticket history
- [ ] Implement customizable templates
- [ ] Add error handling

### Phase 3: Polish (Hours 14-18)
- [ ] Add analytics dashboard
- [ ] Implement batch processing
- [ ] Add model selection
- [ ] Final testing and bug fixes

### Phase 4: Demo Prep (Hours 18-20)
- [ ] Create compelling demo script
- [ ] Prepare diverse test cases
- [ ] Record demo video
- [ ] Update documentation

---

## Technical Debt & Future Considerations

### Immediate Technical Debt
1. **No Testing**: Zero unit tests or integration tests
2. **No Logging**: No error tracking or debugging logs
3. **No Configuration**: Hardcoded values throughout
4. **No Database**: No persistence layer for history
5. **No Authentication**: No user management or API security

### Post-Hackathon Improvements
1. Add comprehensive test suite
2. Implement proper logging and monitoring
3. Add database for ticket history
4. Create REST API for programmatic access
5. Add user authentication and team features
6. Implement rate limiting and caching
7. Add webhook support for ticket systems
8. Create browser extension for one-click analysis

---

## Cost & Resource Estimates

### AI API Costs (Estimated)
- OpenAI GPT-4: ~$0.03-0.06 per ticket analysis
- Anthropic Claude: ~$0.02-0.04 per ticket analysis
- Monthly (100 tickets): $2-6

### Development Time
- **Priority 1 (Critical)**: 8 hours
- **Priority 2 (High-Value)**: 6 hours
- **Priority 3 (Nice-to-Have)**: 4 hours
- **Testing & Polish**: 2 hours
- **Total**: 20 hours (fits within 48-hour hackathon with buffer)

---

## Success Metrics for MVP

### Demo Success Criteria
1. ✅ AI generates unique, context-aware analysis (not templates)
2. ✅ GitHub integration shows real repository insights
3. ✅ UI is polished with smooth loading states
4. ✅ 5+ diverse sample tickets demonstrate capabilities
5. ✅ Zero crashes during demo
6. ✅ Export functionality works flawlessly

### Technical Success Criteria
1. ✅ <3 second response time for analysis
2. ✅ 95%+ uptime during demo period
3. ✅ Handles edge cases gracefully
4. ✅ Clear error messages for failures
5. ✅ Mobile-responsive design

---

## Competitive Advantages

### What Makes Ticket2Fix Unique
1. **IBM Bob Integration**: Leverages repository-aware AI
2. **Comprehensive Output**: Not just summaries, but full dev workflow
3. **Zero Setup**: No installation, runs in browser
4. **Instant Results**: No waiting for background processing
5. **Export-Ready**: Markdown output works with any ticket system

### Differentiation from Alternatives
- **vs. Manual Triage**: 10x faster, more consistent
- **vs. Generic AI**: Context-aware, developer-focused
- **vs. Ticket Systems**: Augments existing tools, doesn't replace

---

## Conclusion

Ticket2Fix has a solid foundation for a hackathon MVP but requires AI integration to deliver on its promise. The recommended improvements focus on:

1. **Authenticity**: Replace templates with real AI
2. **Polish**: Improve UX for impressive demos
3. **Functionality**: Add GitHub integration for real value
4. **Reliability**: Validate inputs and handle errors

With 18-20 hours of focused development, Ticket2Fix can transform from a template-based tool into a genuinely useful AI-powered assistant that demonstrates the power of IBM Bob for developer workflows.

The architecture is simple enough to implement quickly but extensible enough to grow into a production tool post-hackathon.