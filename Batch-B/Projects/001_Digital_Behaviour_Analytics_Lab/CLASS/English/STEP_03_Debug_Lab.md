- [Step 3 — Debug Lab](#step-3--debug-lab)
  - [The mindset](#the-mindset)
  - [The detective method](#the-detective-method)
  - [The two families of bugs](#the-two-families-of-bugs)
    - [Family 1 — Loud bugs](#family-1--loud-bugs)
    - [Family 2 — Silent bugs](#family-2--silent-bugs)
  - [Your task](#your-task)
  - [Questions to ask yourself for silent bugs](#questions-to-ask-yourself-for-silent-bugs)
  - [The three most expensive habits in real jobs](#the-three-most-expensive-habits-in-real-jobs)
  - [Exit thought](#exit-thought)


# Step 3 — Debug Lab

## The mindset

An error message is **not** the computer insulting you.
It is the computer **handing you a clue**.

> ## **KEY: Debugging = Detective Work**

---

## The detective method

Use this exact order every single time:

```
1. PREDICT   What should the answer be?
2. RUN       What actually happened?
3. READ      Read the LAST line of the error first
4. LOCATE    Which line number is named?
5. EXPLAIN   Say the problem in plain English
6. FIX       Change one thing only
7. RERUN     Did it work? Did it break something else?
```

**One change at a time.** Never fix three things at once.

---

## The two families of bugs

### Family 1 — Loud bugs

The program **stops**. Red text appears.

These are the easy ones. The computer told you.

### Family 2 — Silent bugs

The program **runs fine**.
It prints a number.
The number is **wrong**.

Nobody tells you. These are the dangerous ones.

> ## **KEY: Code that runs is not the same as code that is correct.**

---

## Your task

Your instructor will hand you a broken version of your Step 2 program.

For each bug, fill this in:

| # | What I predicted | What actually happened | Which line | Plain-English problem | My fix |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |

---

## Questions to ask yourself for silent bugs

When the program runs but you suspect it is wrong:

1. **Is the answer the right size?**
   If 7 days averaged around 110 minutes, is a total of 76 believable?

2. **Is the answer the right type?**
   Should this be a decimal? Did I get a whole number?

3. **Is the answer the right direction?**
   If actual time is *more* than planned, should the result be positive or negative?

4. **Does the answer change when it should?**
   Add one more value. Did the answer move sensibly?

5. **What happens at the edges?**
   What if every value is the same? What if one is zero?

---

## The three most expensive habits in real jobs

| Habit | Why it costs |
|---|---|
| Trusting output without checking magnitude | Wrong reports get sent to real people |
| Fixing several things at once | You never learn which fix worked |
| Reading the first line of an error instead of the last | The last line names the actual problem |

---

## Exit thought

> A bug that crashes your program costs you five minutes.
>
> A bug that quietly gives you the wrong number can cost a company a decision.
