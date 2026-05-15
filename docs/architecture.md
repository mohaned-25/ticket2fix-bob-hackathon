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
