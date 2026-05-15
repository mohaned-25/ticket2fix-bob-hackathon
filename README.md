# Ticket2Fix — AI Support-to-Code Assistant powered by IBM Bob

## 🚀 Overview

Ticket2Fix is an AI-powered developer workflow assistant that converts unclear support tickets and bug reports into developer-ready tasks.

Support tickets are often incomplete, vague, and difficult for developers to act on. Ticket2Fix helps bridge the gap between support teams and engineering teams by transforming messy user issues into structured bug summaries, reproduction steps, likely affected code areas, debugging checklists, acceptance criteria, and test plans.

This project was built for the IBM Bob Hackathon, where the goal is to build solutions that improve how software is built using IBM Bob as an AI development partner. IBM Bob supports repository-aware development workflows, helping developers understand codebases, reason through logic, generate documentation, and reduce repetitive work.

## 🎯 Problem

In many software teams, support tickets arrive like this:

> "User cannot log in after resetting password. Page reloads but no error is shown."

This type of ticket is difficult for developers because it usually lacks:

- Clear reproduction steps
- Expected vs actual behavior
- Technical context
- Possible affected files
- Debugging checklist
- Test requirements
- Acceptance criteria

As a result, developers spend unnecessary time investigating, asking for clarification, and manually translating user reports into actionable engineering tasks.

## 💡 Solution

Ticket2Fix solves this by converting a support ticket into a complete developer-ready issue.

The user provides:

1. A support ticket or bug report
2. A GitHub repository URL or project context

Ticket2Fix then generates:

- Clean bug summary
- Severity and priority estimation
- Missing information checklist
- Reproduction steps
- Expected behavior
- Actual behavior
- Likely affected modules
- Suggested files to inspect
- Debugging checklist
- Developer-ready task
- Acceptance criteria
- Suggested test cases

## 🤖 How IBM Bob Is Used

IBM Bob is used as the AI development partner throughout this project.

IBM Bob helps with:

- Understanding the repository structure
- Explaining the project architecture
- Identifying likely affected files and modules
- Assisting with backend and frontend implementation
- Generating documentation
- Suggesting test scenarios
- Improving the developer workflow
- Reducing repetitive manual work

The hackathon requires projects to clearly demonstrate meaningful use of IBM Bob, and submissions should include a public GitHub repository with an exported IBM Bob report. This repository includes documentation describing how IBM Bob was used during the project. 

## ✨ Key Features

### 1. Ticket Analyzer

Converts unclear support tickets into structured issue summaries.

Example input:

```text
After resetting password, users cannot log in.
The page reloads but does not show an error message.
This happens only after using the reset password link.
