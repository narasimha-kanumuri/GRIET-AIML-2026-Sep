- [Step 6 — Pandas, Excel Controlled by Python](#step-6--pandas-excel-controlled-by-python)
  - [What just went wrong with NumPy](#what-just-went-wrong-with-numpy)
  - [ELI5](#eli5)
  - [Part A — Bring in the helper](#part-a--bring-in-the-helper)
    - [English](#english)
  - [Part B — Load your own data](#part-b--load-your-own-data)
    - [English](#english-1)
  - [Part C — Look before you leap](#part-c--look-before-you-leap)
    - [English](#english-2)
    - [English](#english-3)
    - [English](#english-4)
    - [English](#english-5)
    - [English](#english-6)
  - [Part D — Picking columns](#part-d--picking-columns)
    - [English](#english-7)
    - [English](#english-8)
  - [Part E — Column maths, no loop](#part-e--column-maths-no-loop)
    - [English](#english-9)
    - [English](#english-10)
    - [English](#english-11)
  - [Part F — The security gate, on a table  *(filtering)*](#part-f--the-security-gate-on-a-table--filtering)
    - [English](#english-12)
    - [English](#english-13)
    - [English](#english-14)
    - [English](#english-15)
  - [Part G — Sorting](#part-g--sorting)
    - [English](#english-16)
    - [English](#english-17)
    - [English](#english-18)
  - [Part H — Creating new knowledge  *(calculated columns)*](#part-h--creating-new-knowledge--calculated-columns)
    - [English](#english-19)
    - [English](#english-20)
    - [English](#english-21)
  - [Part I — Turning numbers into judgement  *(classification)*](#part-i--turning-numbers-into-judgement--classification)
    - [English](#english-22)
  - [Part J — Answer the real questions](#part-j--answer-the-real-questions)
  - [Part K — Save your work](#part-k--save-your-work)
    - [English](#english-23)


# Step 6 — Pandas, Excel Controlled by Python

> ## **KEY: Pandas = Excel Controlled by Python**
> ### KEY: DataFrame = Digital Register

---

## What just went wrong with NumPy

You tried to mix dates, app names and minutes in one array.

A NumPy array wants **one kind of thing**. Put text next to numbers and
your numbers stop behaving like numbers.

That is not a flaw. It is the trade-off that makes NumPy fast.

But your CSV has:

- Text columns
- Number columns
- Column **names**
- Rows that mean something as a **whole row**

You need a **table**, not a tray.

---

## ELI5

Open your CSV in Excel.
You see rows, columns, headers, and you can filter and sort.

Pandas is that same table — but you drive it with Python instead of a mouse.

```
Excel     →  you click
Pandas    →  you instruct
```

Everything you can do by clicking, you can now do by typing.
And typing can be repeated, saved, and run on 10 million rows.

---

## Part A — Bring in the helper

### English
> Bring in the Pandas library and give it the short nickname `pd`.

---

## Part B — Load your own data

### English
> Read the file `digital_behaviour.csv` and store the table in a variable called `df`.

`df` is the universal habit-name for a DataFrame. Use it.

---

## Part C — Look before you leap

Always inspect a table before analysing it.

### English
> Show me the first five rows.

### English
> Show me the last five rows.

### English
> How many rows and columns are there?

### English
> What are the column names?

### English
> Give me a quick summary of the numeric columns.

**Predict:** the summary will show count, mean, min, max and a few more.
Which of those did you calculate by hand in Step 2?

---

## Part D — Picking columns

### English
> Show me only the Instagram minutes column.

### English
> Show me the Date and the Instagram minutes together.

**Notice:** one column and two columns are not written the same way.
Ask yourself why, then look at what each one returns.

---

## Part E — Column maths, no loop

### English
> What is the total Instagram time across all days?

### English
> What is the average study time?

### English
> What was the single heaviest YouTube day?

Notice something: these are the **same instructions as NumPy**.
That is not a coincidence — Pandas uses NumPy underneath.

---

## Part F — The security gate, on a table  *(filtering)*

### English
> Show me only the days where Instagram was above 100 minutes.

### English
> Show me only the days where study time was above 180 minutes.

### English
> Show me the days where Instagram was high **and** study was low.

Two conditions. Both must pass. Each condition needs its own brackets.

### English
> How many heavy Instagram days were there?

---

## Part G — Sorting

### English
> Arrange the table from the highest Instagram usage to the lowest.

### English
> Show me only my top five Instagram days.

### English
> Show me my five best study days.

---

## Part H — Creating new knowledge  *(calculated columns)*

This is where the project becomes yours.

### English
> Create a new column called `Total_Screen_Time`
> by adding Instagram, YouTube, WhatsApp and LinkedIn minutes together.

### English
> Create a new column called `Screen_Hours`
> by converting total screen time into hours.

### English
> Create a new column called `Digital_Balance`
> by dividing study minutes by total screen time.

**Think before you run:**
- If `Digital_Balance` is greater than 1, what does that mean?
- If it is less than 1, what does that mean?
- What would a value of exactly 1 mean?

---

## Part I — Turning numbers into judgement  *(classification)*

### English
> Create a new column called `Day_Type`.
> If total screen time is above 300 minutes, call it "Heavy".
> Otherwise call it "Normal".

This is your first taste of something important:

```
Data  →  Rule  →  Category  →  Decision
```

Later in this course, a machine will learn that rule **from the data itself**
instead of you writing it by hand. That is Machine Learning.

Today, you are the rule.

---

## Part J — Answer the real questions

Write the code to answer each, and write the answer in a sentence.

| # | Question | Your answer |
|---|---|---|
| 1 | Total minutes on each of the four apps? | |
| 2 | Which app consumed the most time? | |
| 3 | How many Heavy days did you have? | |
| 4 | What was your best study day? | |
| 5 | On your heaviest screen day, how much did you study? | |
| 6 | What is your average Digital Balance? | |

---

## Part K — Save your work

### English
> Save the table, including your new columns, to a file called `my_analysis.csv`.

You have just completed the full loop:

```
Read  →  Calculate  →  Add knowledge  →  Save
```

That is a data pipeline.
