- [Step 1 — Generate Your Own Data](#step-1--generate-your-own-data)
  - [Why we are generating data](#why-we-are-generating-data)
  - [About APIs (30 seconds, concept only)](#about-apis-30-seconds-concept-only)
  - [What to do](#what-to-do)
  - [Now open the CSV in Excel](#now-open-the-csv-in-excel)
  - [The columns you now have](#the-columns-you-now-have)
  - [Think about this before Step 2](#think-about-this-before-step-2)

# Step 1 — Generate Your Own Data

## Why we are generating data

Real app data would need accounts, logins, permissions and internet.
That wastes class time and exposes personal information.

So we simulate it.

**Everyone gets the same columns.**
**Everyone gets different numbers.**

That means:
- Nobody can copy your answers
- Everybody can follow the same steps
- Your findings will be genuinely *yours*

---

## About APIs (30 seconds, concept only)

If we *did* pull real data, the path would be:

```
App  →  API  →  JSON  →  CSV / DataFrame  →  NumPy  →  Chart
```

**KEY: API = Data Delivery Boy**

You ask. It brings. That is all an API does.

We are skipping the delivery boy today and starting from the CSV.

---

## What to do

1. Create a folder on your laptop called `digital_behaviour`
2. Put the file `generate_digital_data.py` inside it
3. Open a terminal in that folder
4. Run:

```
python generate_digital_data.py
```

5. You should see:

```
digital_behaviour.csv created successfully!
Rows: 30
```

---

## Now open the CSV in Excel

Look at it. Do not code yet.

Answer these on paper:

1. How many **rows** are there?
2. How many **columns** are there?
3. Which columns contain **numbers**?
4. Which column contains **text**?
5. Just by looking — which was your heaviest Instagram day?
6. How long did question 5 take you?

---

## The columns you now have

| Column | Meaning |
|---|---|
| `Date` | The day |
| `Instagram_Minutes` | Minutes on Instagram |
| `YouTube_Minutes` | Minutes on YouTube |
| `WhatsApp_Minutes` | Minutes on WhatsApp |
| `LinkedIn_Minutes` | Minutes on LinkedIn |
| `Reels_Watched` | Number of reels |
| `Videos_Watched` | Number of videos |
| `Messages_Sent` | Messages sent |
| `Posts_Liked` | Posts liked |
| `Study_Minutes` | Minutes studied |

---

## Think about this before Step 2

You just found one answer by eye, using **30 rows**.

> What if there were **365 rows**?
> What if there were **10,000 students**?

Hold that thought. We come back to it.
