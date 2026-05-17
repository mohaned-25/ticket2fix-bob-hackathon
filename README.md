# 🎫 Ticket2Fix — AI Support-to-Code Assistant powered by IBM Bob

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Hackathon](https://img.shields.io/badge/Hackathon-IBM%20Bob%20Hackathon-blue)
![Built with](https://img.shields.io/badge/Built%20with-IBM%20Bob-purple)
![App](https://img.shields.io/badge/Demo-Streamlit-red)

## 🚀 Overview

**Ticket2Fix** is an AI-powered workflow assistant that converts unclear support tickets and bug reports into **developer-ready engineering tasks**.

Support tickets are often vague, incomplete, and difficult for developers to act on. Ticket2Fix bridges the gap between **support teams** and **engineering teams** by transforming messy user reports into structured bug summaries, reproduction steps, likely affected code areas, debugging checklists, acceptance criteria, and suggested test plans.

This project was built for the **IBM Bob Hackathon** using **IBM Bob as an AI development partner**.

---

## 🔗 Project Links

- 🌐 **Live Demo:** https://ticket2fix-bob-hackathon-mg9zabsxrm3vkwn5fg8a2s.streamlit.app/
- 💻 **GitHub Repository:** https://github.com/mohaned-25/ticket2fix-bob-hackathon
- 🎥 **Demo Video:** [Watch Demo Video](./Demo%20Video/Demo%20Video.mp4)
- 📊 **Slide Deck:** [ticket2fix.pdf](./ticket2fix.pdf)
- 📄 **IBM Bob Report:** `docs/ibm-bob-report.pdf`
- 🧠 **IBM Bob Usage Summary:** `docs/bob-usage-summary.md`

---

## 🎯 Problem

In real software teams, support tickets often arrive like this:

> “Several users report that their payment fails during checkout.  
> The card is charged, but the order is not created.  
> Users see a generic message saying ‘Something went wrong’.”

This type of ticket creates friction because it often lacks:

- Clear reproduction steps
- Expected vs actual behavior
- Technical context
- Possible affected files
- Debugging checklist
- Test requirements
- Acceptance criteria
- Severity and business impact

As a result, developers spend extra time investigating, asking for clarification, and manually translating user-reported issues into actionable engineering tasks.

---

## 💡 Solution

**Ticket2Fix** converts vague support tickets into structured developer-ready tasks.

The user provides:

1. 📝 A support ticket or bug report  
2. 🧩 Repository or project context  

Ticket2Fix generates:

- ✅ Clean bug summary
- 🚨 Severity estimation
- ❓ Missing information checklist
- 🔁 Reproduction steps
- 🎯 Expected behavior
- 🐞 Actual behavior
- 🧱 Likely affected modules
- 📂 Suggested files to inspect
- 🛠️ Debugging checklist
- 👨‍💻 Developer-ready task
- 📌 Acceptance criteria
- 🧪 Suggested test cases

---

## 🤖 How IBM Bob Is Used

IBM Bob was used as the AI development partner throughout this project.

IBM Bob helped with:

- Understanding the repository structure
- Explaining the application architecture
- Planning the support-to-development workflow
- Identifying likely affected files and modules
- Improving frontend and backend implementation
- Generating documentation
- Suggesting test scenarios
- Refining the debugging checklist
- Reducing repetitive manual development work

This project demonstrates how IBM Bob can support repository-aware software development by helping transform unclear support issues into structured engineering workflows.

---

## ✨ Key Features

### 🎫 1. Ticket Analyzer

Converts unclear support tickets into structured issue summaries.

**Example input:**

```text
Several users report that their payment fails during checkout.
The card is charged, but the order is not created in the system.
Users see a generic message saying "Something went wrong".
This started happening after the latest deployment.
