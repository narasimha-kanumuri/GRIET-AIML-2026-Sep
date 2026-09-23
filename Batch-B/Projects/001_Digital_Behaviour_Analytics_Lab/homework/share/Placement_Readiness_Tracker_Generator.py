"""
GRIET AI/ML 2026 - Day 1 Homework
Placement Readiness Tracker - Dataset Generator

WHAT THIS DOES
--------------
Creates a file called placement_readiness.csv on your laptop.

Everyone in the class gets THE SAME COLUMNS.
Everyone in the class gets DIFFERENT NUMBERS.

So the steps are identical for everyone,
but your findings are genuinely yours.

HOW TO RUN
----------
    python generate_placement_data.py

IMPORTANT
---------
This is SIMULATED data created for learning.
These are not real students.
Student IDs are invented. Scores are invented.

Never run this kind of analysis on your actual classmates.
Scoring real people without their knowledge is not a coding exercise.
"""

import csv
import random

# ----------------------------------------------------------
# SETTINGS
# ----------------------------------------------------------

NUM_STUDENTS = 120
OUTPUT_FILE = "placement_readiness.csv"

# No fixed seed - every student gets different numbers.
random.seed()

BRANCHES = ["CSE", "ECE", "IT", "MECH"]

COLUMNS = [
    "Student_ID",
    "Branch",
    "Python_Score",
    "SQL_Score",
    "Aptitude_Score",
    "Communication_Score",
    "Projects_Completed",
    "Mock_Interviews_Attended",
]


# ----------------------------------------------------------
# HELPERS
# ----------------------------------------------------------

def clamp(value, low=0, high=100):
    """Keep a score inside 0..100."""
    return max(low, min(high, int(round(value))))


def pick_branch():
    """CSE and IT are larger batches than ECE and MECH."""
    return random.choices(BRANCHES, weights=[40, 25, 25, 10])[0]


# ----------------------------------------------------------
# BUILD ONE STUDENT
# ----------------------------------------------------------

def make_one_student(student_number):
    """
    Create one realistic-looking student record.

    Design notes (why this is not pure random):

    1. Each student has a hidden 'ability' level.
       Strong students tend to score well across the board.
       This makes the data feel real instead of noise.

    2. Technical branches lean higher on Python and SQL.
       Communication does NOT follow that pattern.

    3. Communication is deliberately the weakest column overall.
       Students should DISCOVER this, not be told it.

    4. Projects and mock interviews loosely follow ability,
       so the Readiness_Score calculation produces a sensible spread.
    """

    branch = pick_branch()

    # Hidden ability: the quiet driver behind every score.
    ability = random.gauss(60, 15)

    # Technical branches get a small technical lift.
    if branch in ("CSE", "IT"):
        tech_bonus = random.uniform(4, 12)
    else:
        tech_bonus = random.uniform(-6, 4)

    python_score = clamp(ability + tech_bonus + random.gauss(0, 10))
    sql_score = clamp(ability + tech_bonus * 0.6 + random.gauss(0, 12))
    aptitude_score = clamp(ability + random.gauss(0, 12))

    # Communication is the weak spot across the batch.
    # This is the finding the homework is designed to surface.
    communication_score = clamp(ability - 12 + random.gauss(0, 14))

    # Stronger students tend to build more and practise more.
    projects = clamp(
        random.gauss(ability / 22, 1.2),
        low=0,
        high=8,
    )
    mocks = clamp(
        random.gauss(ability / 18, 1.8),
        low=0,
        high=12,
    )

    student_id = f"S{student_number:04d}"

    return [
        student_id,
        branch,
        python_score,
        sql_score,
        aptitude_score,
        communication_score,
        projects,
        mocks,
    ]


# ----------------------------------------------------------
# BUILD ALL ROWS
# ----------------------------------------------------------

def build_rows(num_students):
    rows = []
    for i in range(1, num_students + 1):
        rows.append(make_one_student(i))
    return rows


# ----------------------------------------------------------
# WRITE THE CSV
# ----------------------------------------------------------

def write_csv(filename, columns, rows):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerows(rows)


# ----------------------------------------------------------
# RUN
# ----------------------------------------------------------

def main():
    rows = build_rows(NUM_STUDENTS)
    write_csv(OUTPUT_FILE, COLUMNS, rows)

    print(f"{OUTPUT_FILE} created successfully!")
    print(f"Rows: {len(rows)}")
    print(f"Columns: {len(COLUMNS)}")
    print()
    print("Reminder: this is simulated data. These are not real students.")
    print()
    print("Next step: open this file in Excel and look at it.")
    print("Then read the homework brief before writing any code.")


if __name__ == "__main__":
    main()
