- [Step 5 — NumPy, The Fast Maths Engine](#step-5--numpy-the-fast-maths-engine)
  - [ELI5](#eli5)
  - [Part A — Bring in the helper](#part-a--bring-in-the-helper)
    - [English](#english)
    - [Your translation](#your-translation)
  - [Part B — Build the tray](#part-b--build-the-tray)
    - [English](#english-1)
    - [English](#english-2)
  - [Part C — The replacements](#part-c--the-replacements)
    - [English](#english-3)
    - [English](#english-4)
    - [English](#english-5)
    - [English](#english-6)
    - [English](#english-7)
  - [Part D — Reaching inside the tray  *(indexing)*](#part-d--reaching-inside-the-tray--indexing)
    - [English](#english-8)
    - [English](#english-9)
    - [English](#english-10)
  - [Part E — Taking a slice  *(slicing)*](#part-e--taking-a-slice--slicing)
    - [English](#english-11)
    - [English](#english-12)
    - [English](#english-13)
  - [Part F — One instruction, every number  *(the big moment)*](#part-f--one-instruction-every-number--the-big-moment)
    - [English](#english-14)
    - [English](#english-15)
  - [Part G — The security gate  *(boolean filtering)*](#part-g--the-security-gate--boolean-filtering)
    - [English](#english-16)
    - [English](#english-17)
    - [English](#english-18)
    - [English](#english-19)
  - [Part H — Compare and reflect](#part-h--compare-and-reflect)
  - [The question that leads to Step 6](#the-question-that-leads-to-step-6)


# Step 5 — NumPy, The Fast Maths Engine

> ## **KEY: NumPy = Fast Math Engine**
> ### One instruction. Many numbers.

---

## ELI5

A Python list is a **shopping bag**.
It will hold anything: numbers, words, other bags. It does not care.

A NumPy array is a **calculator tray**.
Everything in it is the same kind of number, lined up neatly,
so the calculator can work on the whole tray at once.

Same items. Very different capability.

---

## Part A — Bring in the helper

### English
> Bring in the NumPy library and give it the short nickname `np`.

### Your translation
One import line. Everyone uses the same nickname — it is a universal habit.

---

## Part B — Build the tray

### English
> Take the seven Instagram values and put them into a NumPy array.

Use the same seven numbers as before:

```
95, 120, 80, 140, 60, 170, 110
```

### English
> Also build an array for Study minutes:

```
120, 45, 200, 30, 240, 15, 150
```

---

## Part C — The replacements

For each row: **predict the answer first**, then write the code,
then compare it with what you wrote in Step 2.

| English instruction | Lines in Step 2 | Lines now |
|---|---:|---:|
| Add everything up | 4 | 1 |
| Share the total equally | 2 | 1 |
| Find the biggest | 5 | 1 |
| Find the smallest | 5 | 1 |
| Count how many | 1 | 1 |

### English
> Add up every value in the array.

### English
> Find the average of the array.

### English
> Find the largest value.

### English
> Find the smallest value.

### English
> How many values are in the array?

---

## Part D — Reaching inside the tray  *(indexing)*

### English
> Show me the very first day.

Remember: Python starts counting at **zero**, not one.

### English
> Show me the very last day.

There is a shortcut for "last" that does not need you to know the length.

### English
> Show me the third day.

**Predict:** which index number is the third day?

---

## Part E — Taking a slice  *(slicing)*

### English
> Show me the first three days.

### English
> Show me the last two days.

### English
> Show me days two, three and four.

**Careful:** when you ask for a range, the ending point is **not included**.
This is the single most common beginner mistake in Python.

**Predict before running:** how many values will you get back each time?

---

## Part F — One instruction, every number  *(the big moment)*

### English
> Convert every Instagram value from minutes into hours.

In Step 2, that would have been a loop.

Now: divide the **whole array** by 60. One line.

### English
> For every single day, subtract Instagram minutes from Study minutes.

Two arrays. One subtraction. Seven answers.

**Predict:** if the result is negative, what does that mean about that day?

---

## Part G — The security gate  *(boolean filtering)*

### English
> Ask each value: are you greater than 100?

Run it. Look carefully at what comes back.
It is not the numbers. It is a list of **yes/no answers**.

### English
> Now show me only the values where the answer was yes.

That is the gate: **True passes through, False stays outside.**

### English
> How many days were above 100 minutes?

Hint: True counts as 1, False counts as 0. So you can just add them up.

### English
> Show me only the days that were above your own average.

---

## Part H — Compare and reflect

Fill this in honestly:

| | Plain Python | NumPy |
|---|---:|---:|
| Lines for total, average, max, min | | |
| Lines for "days above average" | | |
| Lines to convert all to hours | | |
| Places a silent bug could hide | | |

---

## The question that leads to Step 6

NumPy handled the numbers beautifully.

Now try this:

> Put the **date**, the **app name**, and the **minutes** into one NumPy array together.

Attempt it. See what happens to your numbers.

Then ask yourself:

> "What if my data has **labels**, **text** and **numbers** all mixed together —
> like a real table?"

That question is the door to Pandas.
