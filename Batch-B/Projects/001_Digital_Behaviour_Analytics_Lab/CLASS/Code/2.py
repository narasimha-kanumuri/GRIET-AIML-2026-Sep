"""
=============================================================================
DAY 1 - STEP 2 SOLUTION - PLAIN PYTHON
TEACHER ONLY. Never release to students.
=============================================================================

Matches: STEP_02_Pure_Python_English.md

PURPOSE OF THIS STEP
--------------------
This code is deliberately LONG and REPETITIVE.
That is the whole point.

Do NOT shorten it. Do NOT show sum(), max(), min() here.
The pain is the lesson. Step 4 collects the bill.

WHAT TO SAY WHILE TEACHING
--------------------------
"Everything here you already know. No new library. No new import.
 We are only translating English sentences into Python."

NUMBERS TO COLLECT AT THE END
-----------------------------
  - loops written        -> 4
  - near-identical loops -> 4
  - lines of real code   -> ~35
Write these on the board. You need them in Step 4.
=============================================================================
"""

import csv

# -----------------------------------------------------------------------
# PART A - STORE THE DATA
# -----------------------------------------------------------------------
# English: "Remember the app name we are studying."

APP = "Instagram"

# English: "Remember the minutes spent on Instagram for each day."
#
# Students read from THEIR OWN csv. Everyone's numbers differ.
# That is deliberate - nobody can copy an answer.

minutes = []

with open("digital_behaviour.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # int() matters enormously. CSV gives TEXT.
        # Removing this int() is exactly Bug 6.
        minutes.append(int(row["Instagram_Minutes"]))

# English: "Use only the first 7 days so we can check by eye."
#
# TEACHING NOTE: 0:7 gives 7 items, not 8.
# The end point is EXCLUDED. This is Bug 4, and it comes
# straight back in Step 5 slicing. Flag it now.

minutes = minutes[0:7]


# -----------------------------------------------------------------------
# PART B - TOTAL USAGE
# -----------------------------------------------------------------------
# English: "Start a counter at zero.
#           Go through every value one at a time.
#           Add each value to the counter."
#
# LOOP 1 of 4

total = 0

for value in minutes:
    total = total + value


# -----------------------------------------------------------------------
# PART C - AVERAGE USAGE
# -----------------------------------------------------------------------
# English: "Take the total. Share it equally across the number of days."
#
# TEACHING NOTE: '/' keeps decimals. '//' throws them away.
# Using '//' here is Bug 3 - the silent one. Do not mention it yet.

average = total / len(minutes)


# -----------------------------------------------------------------------
# PART D - HIGHEST USAGE DAY
# -----------------------------------------------------------------------
# English: "Assume the first day is the highest so far.
#           If a value is bigger, it becomes the new highest."
#
# LOOP 2 of 4
#
# TEACHING NOTE: we start with minutes[0], NOT 0.
# Ask: "Why not start at zero?"
# Answer: starting at 0 assumes the data can never be negative.
# That assumption is Bug tier T6. Real data breaks it.

highest = minutes[0]

for value in minutes:
    if value > highest:
        highest = value


# -----------------------------------------------------------------------
# PART E - LOWEST USAGE DAY
# -----------------------------------------------------------------------
# English: "Same idea as highest. But keep the smaller one."
#
# LOOP 3 of 4
#
# POINT AT THE SCREEN HERE.
# This block is Part D with ONE character changed.
# Students should feel the duplication.

lowest = minutes[0]

for value in minutes:
    if value < lowest:
        lowest = value


# -----------------------------------------------------------------------
# PART F - DAYS ABOVE AVERAGE
# -----------------------------------------------------------------------
# English: "Start a counter at zero.
#           If the value is greater than the average, increase by one."
#
# LOOP 4 of 4
#
# TEACHING NOTE: 'count = count + 1' builds on itself.
# Writing 'count = 1' throws away all previous work. That is Bug 5.

count = 0

for value in minutes:
    if value > average:
        count = count + 1


# -----------------------------------------------------------------------
# PART G - SHOW THE REPORT
# -----------------------------------------------------------------------

print("App:", APP)
print("Days:", len(minutes))
print("Total Minutes:", total)
print("Average Minutes:", average)
print("Highest Day:", highest)
print("Lowest Day:", lowest)
print("Days Above Average:", count)


# =======================================================================
# STOP HERE
# =======================================================================
#
# Tell students: "It works. Do not improve it. Do not shorten it."
#
# Then ask the three questions:
#   1. How many loops did you write?              -> 4
#   2. How many looked almost identical?          -> 4
#   3. If I ask for median, what do you write?    -> another loop
#
# Then the killer follow-up:
#   "Now do all of that for YouTube, WhatsApp and LinkedIn too."
#   4 apps x 6 questions = 24 near-identical blocks.
#
# Do NOT rescue them with NumPy yet.
# Step 3 breaks this code first. Step 4 collects the bill.
# =======================================================================
