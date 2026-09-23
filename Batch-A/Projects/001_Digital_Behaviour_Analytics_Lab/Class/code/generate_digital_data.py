"""
GRIET AI/ML 2026 - Day 1
Digital Behaviour Analysis - Dataset Generator

WHAT THIS DOES
--------------
Creates a file called digital_behaviour.csv on your laptop.

Everyone in the class gets THE SAME COLUMNS.
Everyone in the class gets DIFFERENT NUMBERS.

So the steps are identical for everyone,
but the findings are genuinely yours.

HOW TO RUN
----------
    python generate_digital_data.py

NOTE
----
This is simulated data created for learning.
It is not real data from any app or service.
"""

import csv
import random
from datetime import datetime, timedelta

# ----------------------------------------------------------
# SETTINGS
# ----------------------------------------------------------

NUM_DAYS = 30
OUTPUT_FILE = "digital_behaviour.csv"

# No fixed seed - every student gets different numbers.
random.seed()

COLUMNS = [
    "Date",
    "Instagram_Minutes",
    "YouTube_Minutes",
    "WhatsApp_Minutes",
    "LinkedIn_Minutes",
    "Reels_Watched",
    "Videos_Watched",
    "Messages_Sent",
    "Posts_Liked",
    "Study_Minutes",
]


# ----------------------------------------------------------
# BUILD ONE DAY OF DATA
# ----------------------------------------------------------

def make_one_day(date_text, is_weekend):
    """Create one realistic-looking row of digital behaviour."""

    # Weekends lean heavier on entertainment, lighter on study.
    if is_weekend:
        instagram = random.randint(60, 240)
        youtube = random.randint(60, 300)
        study = random.randint(0, 180)
        linkedin = random.randint(0, 30)
    else:
        instagram = random.randint(20, 180)
        youtube = random.randint(15, 210)
        study = random.randint(45, 360)
        linkedin = random.randint(0, 75)

    whatsapp = random.randint(10, 180)

    # Reels roughly track Instagram time, with natural variation.
    reels = int(instagram * random.uniform(0.6, 1.4))

    # Videos roughly track YouTube time, but each video is longer.
    videos = max(1, int(youtube * random.uniform(0.15, 0.45)))

    messages = int(whatsapp * random.uniform(1.5, 3.5))
    likes = int(reels * random.uniform(0.2, 0.7))

    return [
        date_text,
        instagram,
        youtube,
        whatsapp,
        linkedin,
        reels,
        videos,
        messages,
        likes,
        study,
    ]


# ----------------------------------------------------------
# BUILD ALL ROWS
# ----------------------------------------------------------

def build_rows(num_days):
    rows = []
    start_date = datetime.now() - timedelta(days=num_days)

    for day_number in range(num_days):
        current = start_date + timedelta(days=day_number)
        date_text = current.strftime("%Y-%m-%d")
        is_weekend = current.weekday() >= 5      # 5 = Saturday, 6 = Sunday

        rows.append(make_one_day(date_text, is_weekend))

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
    rows = build_rows(NUM_DAYS)
    write_csv(OUTPUT_FILE, COLUMNS, rows)

    print(f"{OUTPUT_FILE} created successfully!")
    print(f"Rows: {len(rows)}")
    print(f"Columns: {len(COLUMNS)}")
    print()
    print("Next step: open this file in Excel and look at it.")
    print("Do not write any analysis code yet.")


if __name__ == "__main__":
    main()
