# Class Decisions

This file keeps important course decisions in Git so they travel between the Windows and Ubuntu copies of `coding-year-one`. Obsidian contains the detailed learning system; this file contains concise decisions that affect the course or repository.

## 2026-07-22 - Automatic record reporting and weekly reviews

- During active tutoring, meaningful evidence is stored automatically in the appropriate Obsidian record and in the repository when a Git-tracked record is useful.
- After meaningful record changes, tell Baran what was recorded, where it was stored, whether any status changed, what remains unknown, and the exact next action.
- Never invent hours, test results, GitHub status, grades, or understanding merely to fill a template.
- Templates are blueprints, not live records. Real weekly reviews live inside their active week folders and are updated during the week, then finalized only when the week closes.
- Historical imported daily/weekly templates were removed from the active Spaced Repetition queue; they remain labeled as archived references.
- Week 1 now has a completed weekly review. Week 2 has an in-progress living review and is not scheduled for spaced review until completion.
- Current lesson remains Week 2 reassignment; no mastery status or grade changed.

## 2026-07-22 - Obsidian learning plugins configured

- Baran explicitly installed Homepage, Omnisearch, Smart Connections, and Spaced Repetition.
- Homepage now opens the learning dashboard in Reading view while retaining working tabs.
- Omnisearch now favors readable headings and downranks archives, attachments, and imported raw material.
- Smart Connections remains local-model based and excludes templates, imported raw material, archives, attachments, and the obsolete Welcome note from semantic indexing.
- The review system contains only demonstrated Week 1 material plus the Week 2 assignment explanation Baran already gave correctly. The active reassignment answer remains excluded.
- Spaced-repetition ratings are practice evidence only; they do not automatically change a grade or mastery status.
- Added `Ctrl+Shift+H` for Home and `Ctrl+Shift+O` for Omnisearch. Review commands remain discoverable through `Ctrl+P` to avoid introducing too many shortcuts at once.
- Full usage guidance is in Obsidian's `03 Knowledge Base/Review/Review Hub.md`.
- Current lesson remains Week 2 reassignment; no mastery status or grade changed.

## 2026-07-22 - Minimal Obsidian plugin roadmap

- Keep the community-plugin set small and install one plugin at a time after backing up the vault.
- Recommended first: **Homepage** for reliable access to the learning dashboard and **Omnisearch** for relevance-ranked, typo-tolerant text search.
- Recommended after the normal workflow is comfortable: **Smart Connections** for local, meaning-based discovery across notes.
- Consider **Spaced Repetition** later for selected verified concepts, commands, terminology, networking facts, and security fundamentals.
- Do not add Dataview, Templater, QuickAdd, Obsidian Git, task systems, cosmetic bundles, or autonomous AI agents yet; current built-in features and tutoring workflows already cover those needs with less complexity.
- No community plugin is installed without Baran's explicit approval. Plugin changes do not automatically sync the vault to GitHub or Ubuntu.
- Current lesson remains Week 2 reassignment; no mastery status or grade changed.

## 2026-07-22 - Obsidian AI plugin policy

- Keep lessons and natural-language questions in Codex; Codex can already read and update the local Obsidian vault during active tutoring.
- Keep Obsidian as the organized learning memory rather than creating a second, competing tutor chat by default.
- If meaning-based discovery is wanted, **Smart Connections** is the preferred first optional plugin because it can provide local semantic connections without requiring an API key for its core feature.
- **Copilot for Obsidian** may be evaluated later for chat inside the vault, after reviewing provider settings, data handling, separate API costs, and backups.
- Do not install low-trust or agentic read/write plugins merely for convenience. Community plugins execute third-party code and require explicit approval before installation.
- Never place employer/production OT data, passwords, tokens, or API keys in the vault, prompts, or Git. A ChatGPT subscription does not include OpenAI API usage.
- Current lesson remains Week 2 reassignment; no mastery status or grade changed.

## 2026-07-22 — Obsidian daily-use workflow clarified

- Obsidian is the course's organized learning memory and navigation system; program code remains in the repository and VS Code.
- Lesson answers, teach-backs, questions, and tutor feedback happen in the Codex chat. Current Focus stores the instruction; it is not an answer form.
- The main hub is `C:\Dev\Obsidian DEV\00 Dashboard\Home.md`, and the exact next action is in `Current Focus.md`.
- Use `Ctrl+O` to open a note by name and `Ctrl+Shift+F` to search the text of all notes.
- Obsidian is not an AI prompt box by default. Natural-language questions can be asked in the tutor chat, which can inspect and update the organized vault.
- The old `AppData\Local\Temp` Odin ZIP path is not the current vault; the correct vault is `C:\Dev\Obsidian DEV`.
- Baran does not need to spend lessons manually organizing everything. The tutor updates meaningful evidence and decisions during active tutoring.

## 2026-07-22 — Primary career destination: secure industrial systems

- Primary long-term target: OT/ICS cybersecurity and secure industrial systems, including industrial software/product security, monitoring/resilience, and secure industrial AI integration.
- Software engineering remains the foundation and strongest entry bridge; cybersecurity is not treated as a beginner shortcut.
- AI literacy includes both building bounded AI features and securing/evaluating AI-enabled systems.
- The 12-month schedule is a flexible Year 1 planning window. Mastery, workload, portfolio evidence, and market data control pace and future sequence.
- Months 1–10 build trustworthy programming, software/supply-chain integrity, application/AI security, Linux/network defense, and OT architecture.
- Month 11 now adds asset/trust-zone mapping, monitoring, incident response/recovery, tested backup/restore, and safe advisory AI triage over invented events.
- Month 12 capstone now proves industrial software, defensive security, recovery, and AI assurance together.
- Certification selection is deferred until Week 39 and must be justified by demonstrated skill plus current target postings.
- Current lesson remains Week 2 reassignment; no grade or mastery status changed.

## 2026-07-22 — Market-aware curriculum and candidate strategy

- Keep the 12-month curriculum's core direction; do not rewrite it or rush Week 2 because of market anxiety.
- Position Baran as an industrial-domain software/systems candidate, not a generic junior coder.
- Run a monthly labor/AI/industrial market pulse and deep reviews at Weeks 13, 26, 39, and 52.
- Deep reviews sample 20–30 relevant postings and compare recurring requirements with the curriculum and portfolio.
- Curriculum changes require at least two credible sources plus a posting-sample gap; a major rewrite normally requires the signal to persist across two deep reviews.
- Add earlier evidence: Month 3 portfolio README/postmortem, Month 5 issues/PR-style review/CI, Month 8 reliability case study, Month 9 troubleshooting story, Month 11 runbook/observability, and Month 12 role-specific case study/resume bullets.
- Pace changes follow mastery evidence: accelerate after independent explanation/transfer/debugging; slow down when prerequisites are weak.
- A monthly Codex automation now maintains the market review in `C:\Dev`; it must not change grades/mastery and must not commit or push automatically.
- Detailed strategy: `notes/career-market-strategy.md` and the Obsidian Job Market folder.
- Current lesson remains Week 2 reassignment; no mastery status or grade changed.

## 2026-07-22 — Automatic documentation

- Coding/class decisions, accepted ideas, curriculum changes, mastery evidence, meaningful errors, grades, and exact next steps should be summarized automatically during active tutoring sessions.
- Update Obsidian for the connected learning record.
- Update this repository when a Git-tracked decision, note, design, test, or source-code change is useful.
- Do not paste full chat transcripts. Record the decision, evidence, status, and next action cleanly.
- Windows and Ubuntu remain separate copies; save, commit, push, and pull before switching.

## 2026-07-22 — AI integration added to the curriculum

- AI application integration is now a required provider-neutral thread in Months 4–12.
- Formal AI API implementation begins in Month 7 after Python, Git, SQL, HTTP, JSON, and ordinary API foundations.
- Topics include structured output, tool/function calling boundaries, fake providers, evaluation sets, retrieval/citations, secrets, cost/latency, rate limits, fallbacks, prompt injection, data risks, and cloud/local tradeoffs.
- The Month 12 capstone includes an evaluated advisory AI maintenance-summary component over sanitized simulated data.
- Deterministic code retains calculations, alarms, interlocks, and safety/control decisions.
- AI never directly controls equipment or connects experimental code to an employer or production OT network.
- Current lesson remains Week 2 reassignment; no mastery status changed.

## 2026-07-22 — GitHub visibility and synchronization

- Updating a file locally does not automatically update GitHub.
- GitHub sees progress only after the relevant files are saved, staged, committed, and pushed successfully.
- The Obsidian vault at `C:\Dev\Obsidian DEV` is outside this repository, so it is not published by pushes from `coding-year-one`.
- Automatic tutoring updates may change local Obsidian or repository files, but commits and pushes remain intentional checkpoints so unfinished, incorrect, secret, or unrelated files are not published accidentally.
- At the end of a study session, review `git status`, commit the intended learning evidence, push it, and confirm success before switching systems.
