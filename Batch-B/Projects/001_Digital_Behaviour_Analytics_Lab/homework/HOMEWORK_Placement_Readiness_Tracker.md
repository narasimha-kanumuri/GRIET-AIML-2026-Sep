- [Homework — Placement Readiness Tracker](#homework--placement-readiness-tracker)
  - [The situation](#the-situation)
  - [Your data](#your-data)
  - [Same workflow, new domain](#same-workflow-new-domain)
  - [Part 1 — NumPy](#part-1--numpy)
  - [Part 2 — Pandas](#part-2--pandas)
  - [Part 3 — Create new knowledge](#part-3--create-new-knowledge)
  - [Part 4 — Classification](#part-4--classification)
  - [Part 5 — Charts](#part-5--charts)
  - [Part 6 — The report](#part-6--the-report)
  - [What to submit](#what-to-submit)
  - [Marking](#marking)
  - [Rules](#rules)
  - [Why this project matters more than it looks](#why-this-project-matters-more-than-it-looks)

# Homework — Placement Readiness Tracker

> ## **KEY: Data = Career GPS**

A GPS does not judge you.
It tells you where you are, and how far you still have to go.

---

## The situation

A placement coordinator has skill scores for a batch of students.
Every score is out of 100.

Companies will shortlist candidates soon.

The coordinator cannot manually study every student. They need answers:

1. Who is ready right now?
2. Who is close and just needs a push?
3. Which skill is weakest across the whole batch?
4. Which single training session would help the most people?

---

## Your data

Run the generator you will be given:

```
python generate_placement_data.py
```

You get `placement_readiness.csv` with these columns:

| Column | Meaning |
|---|---|
| `Student_ID` | Anonymous ID |
| `Branch` | CSE / ECE / IT / MECH |
| `Python_Score` | Out of 100 |
| `SQL_Score` | Out of 100 |
| `Aptitude_Score` | Out of 100 |
| `Communication_Score` | Out of 100 |
| `Projects_Completed` | Count |
| `Mock_Interviews_Attended` | Count |

**This is simulated data. It is not real students.**
Never do this analysis on real classmates.

---

## Same workflow, new domain

You are repeating exactly what you did in class — nothing new is required.

| Class (Digital Behaviour) | Homework (Placement) |
|---|---|
| Instagram minutes | Python score |
| Total screen time | Total skill score |
| Digital Balance | Readiness Score |
| Heavy / Normal day | Ready / Almost / Not Ready |
| Time by app | Average by skill |
| Screen time by day chart | Skill comparison chart |

---

## Part 1 — NumPy

Work with the score columns as arrays.

1. Average Python score across the batch
2. Highest and lowest Aptitude score
3. How many students scored above 70 in Communication
4. For every student, the gap between their best and worst skill

---

## Part 2 — Pandas

1. Load the CSV and inspect it (head, shape, columns, describe)
2. Show only students with Python above 75
3. Sort the table by Aptitude, highest first
4. Show the top 10 students by Python score
5. Show students who are strong in Python **but** weak in Communication

---

## Part 3 — Create new knowledge

Add these columns:

| Column | How to build it |
|---|---|
| `Total_Score` | Sum of the four skill scores |
| `Average_Score` | Total ÷ 4 |
| `Weakest_Skill_Score` | The lowest of the four |
| `Readiness_Score` | Average, plus 2 points per project, plus 1 per mock interview, capped at 100 |

---

## Part 4 — Classification

Add a column `Readiness_Band`:

| Condition | Band |
|---|---|
| Readiness Score ≥ 75 | Ready |
| 60 to 74 | Almost Ready |
| Below 60 | Needs Work |

Then answer:
- How many students fall in each band?
- Which band is the largest?

---

## Part 5 — Charts

1. Bar chart: average score for each of the four skills
2. Bar chart: how many students are in each readiness band
3. Line or bar chart: average readiness score by branch

Every chart must have a title and labelled axes.

---

## Part 6 — The report

Write **six sentences**. No code, no jargon.

1. The weakest skill across the batch is ______ because ______.
2. ______ students are ready right now.
3. The largest group is ______, which means ______.
4. The single most useful training session would be ______ because ______.
5. One thing that surprised me in this data was ______.
6. If I only had time to help ten students, I would pick ______ because ______.

---

## What to submit

| File | Contents |
|---|---|
| `placement_analysis.py` | Your full code |
| `placement_results.csv` | Your table including the new columns |
| `charts/` | Your three saved chart images |
| `report.md` | Your six sentences |

---

## Marking

| Area | Weight |
|---|---:|
| Code runs without errors | 20% |
| Correct NumPy operations | 20% |
| Correct Pandas operations | 20% |
| New columns built correctly | 15% |
| Charts titled and labelled | 15% |
| Written report is clear and honest | 10% |

---

## Rules

1. Use **your own generated file**. Do not use a friend's.
2. Type the code. Do not paste it.
3. If you use an AI tool, you must be able to explain **every line** when asked.
4. Bring one question to the next class.

---

## Why this project matters more than it looks

Change the column names and this becomes:

- Employee performance review
- Loan approval scoring
- Customer risk scoring
- Product quality grading

You are not learning "a placement project".
You are learning **scoring and segmentation** — one of the most common jobs in analytics.

And on Day 9, a machine will learn the readiness rule from data
instead of you writing it by hand.
