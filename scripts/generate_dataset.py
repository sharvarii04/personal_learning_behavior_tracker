"""
Generate a realistic synthetic dataset for a Personal Learning Behaviour Tracker.

This dataset is designed for a portfolio/interview project. It simulates study
sessions from 2024 to the end of 2025 using realistic behavioral patterns:
- focus is usually stronger in the morning/early afternoon
- long gaps reduce consistency
- higher distractions reduce focus
- difficult topics can lower focus unless session quality is good

You can later replace this CSV with your real learning logs.
"""

from __future__ import annotations

import csv
import math
import random
from datetime import date, datetime, timedelta
from pathlib import Path

RANDOM_SEED = 42
random.seed(RANDOM_SEED)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = PROJECT_ROOT / "data" / "raw" / "study_sessions.csv"

TOPICS = [
    ("Machine Learning", "ML", 4),
    ("Deep Learning", "ML", 5),
    ("Statistics", "Math", 4),
    ("Linear Algebra", "Math", 4),
    ("Python Programming", "Programming", 3),
    ("SQL Practice", "Programming", 3),
    ("Data Visualization", "Data Analysis", 2),
    ("Big Data Analytics", "Data Engineering", 4),
    ("Generative AI", "GenAI", 4),
    ("German Language", "Language", 3),
]

LOCATIONS = ["Home Desk", "University Library", "Cafe", "Study Room"]
DEVICES = ["Laptop", "Laptop + Notebook", "Tablet", "Notebook"]


def clamp(value: float, low: int = 1, high: int = 10) -> int:
    return max(low, min(high, int(round(value))))


def choose_session_count(day: date) -> int:
    """Simulate realistic study frequency: more on weekdays, fewer on weekends."""
    weekday = day.weekday()  # Monday=0
    if weekday < 5:
        return random.choices([0, 1, 2], weights=[0.28, 0.52, 0.20])[0]
    return random.choices([0, 1, 2], weights=[0.48, 0.42, 0.10])[0]


def choose_start_hour() -> int:
    return random.choices(
        [7, 8, 9, 10, 11, 12, 14, 15, 16, 18, 20, 21, 22],
        weights=[3, 7, 13, 14, 9, 5, 8, 8, 7, 6, 5, 3, 2],
    )[0]


def time_of_day_bucket(hour: int) -> str:
    if 5 <= hour < 12:
        return "Morning"
    if 12 <= hour < 17:
        return "Afternoon"
    if 17 <= hour < 21:
        return "Evening"
    return "Night"


def focus_score_formula(
    hour: int,
    duration_min: int,
    difficulty: int,
    sleep_hours: float,
    energy_before: int,
    distraction_level: int,
    break_before_days: int,
) -> int:
    """Create a realistic focus score with visible but non-perfect patterns."""
    # Time effect: strongest in morning, decent afternoon, weaker late night.
    if 8 <= hour <= 11:
        time_effect = 1.45
    elif 12 <= hour <= 16:
        time_effect = 0.65
    elif 17 <= hour <= 20:
        time_effect = -0.25
    else:
        time_effect = -1.05

    # Session length effect: very short and very long sessions usually reduce focus.
    duration_effect = -abs(duration_min - 85) / 55

    # Long gaps make it harder to restart consistently.
    gap_effect = -0.32 * min(break_before_days, 5)

    sleep_effect = (sleep_hours - 7.0) * 0.45
    energy_effect = (energy_before - 5.5) * 0.42
    distraction_effect = -(distraction_level - 3) * 0.52
    difficulty_effect = -(difficulty - 3) * 0.28
    noise = random.gauss(0, 0.75)

    raw_score = (
        6.1
        + time_effect
        + duration_effect
        + gap_effect
        + sleep_effect
        + energy_effect
        + distraction_effect
        + difficulty_effect
        + noise
    )
    return clamp(raw_score)


def generate_rows(start: date, end: date) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    current = start
    last_study_date: date | None = None
    session_no = 1

    while current <= end:
        count = choose_session_count(current)
        used_hours: set[int] = set()

        for _ in range(count):
            topic, topic_type, difficulty = random.choice(TOPICS)
            hour = choose_start_hour()
            while hour in used_hours:
                hour = choose_start_hour()
            used_hours.add(hour)

            minute = random.choice([0, 10, 15, 20, 30, 45])
            start_dt = datetime(current.year, current.month, current.day, hour, minute)
            duration_min = random.choice([35, 45, 50, 60, 75, 90, 105, 120, 135])
            end_dt = start_dt + timedelta(minutes=duration_min)

            break_before_days = 0 if last_study_date is None else (current - last_study_date).days - 1
            break_before_days = max(0, break_before_days)

            sleep_hours = round(random.normalvariate(7.0, 0.9), 1)
            sleep_hours = max(4.5, min(9.5, sleep_hours))

            energy_before = clamp(random.normalvariate(6.1, 1.6))
            distraction_level = clamp(random.normalvariate(3.4, 1.7))

            focus_score = focus_score_formula(
                hour=hour,
                duration_min=duration_min,
                difficulty=difficulty,
                sleep_hours=sleep_hours,
                energy_before=energy_before,
                distraction_level=distraction_level,
                break_before_days=break_before_days,
            )

            completion_percent = clamp(
                55 + focus_score * 5 + random.gauss(0, 10), low=20, high=100
            )

            if focus_score >= 8:
                notes = "High clarity, strong concentration, completed planned tasks"
            elif focus_score >= 6:
                notes = "Decent session, some distractions but useful progress"
            elif break_before_days >= 3:
                notes = "Restart after long gap, took time to regain rhythm"
            elif distraction_level >= 7:
                notes = "Frequent interruptions reduced flow"
            else:
                notes = "Low energy, needed more breaks than expected"

            rows.append(
                {
                    "session_id": f"S{session_no:04d}",
                    "date": current.isoformat(),
                    "day_of_week": current.strftime("%A"),
                    "start_time": start_dt.strftime("%H:%M"),
                    "end_time": end_dt.strftime("%H:%M"),
                    "hour_of_day": hour,
                    "time_of_day": time_of_day_bucket(hour),
                    "duration_min": duration_min,
                    "topic": topic,
                    "topic_type": topic_type,
                    "difficulty_1_5": difficulty,
                    "sleep_hours": sleep_hours,
                    "energy_before_1_10": energy_before,
                    "distraction_level_1_10": distraction_level,
                    "break_before_days": break_before_days,
                    "location": random.choice(LOCATIONS),
                    "device_used": random.choice(DEVICES),
                    "completion_percent": completion_percent,
                    "focus_score_1_10": focus_score,
                    "notes": notes,
                }
            )
            session_no += 1
            last_study_date = current

        current += timedelta(days=1)

    return rows


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    rows = generate_rows(date(2024, 1, 8), date(2025, 12, 28))
    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"Generated {len(rows)} study sessions")
    print(f"Saved to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
