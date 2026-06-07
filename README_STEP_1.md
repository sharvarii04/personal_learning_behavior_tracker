# Personal Learning Behaviour Tracker with ML and Agentic Insights

## Step 1: Dataset Creation

This step creates a realistic synthetic dataset for a personal learning behavior analytics project.

The dataset simulates study sessions from January 2024 to the end of December 2025 and includes behavioral signals such as:

- session timestamp
- topic and topic type
- duration
- time of day
- sleep hours
- energy before study
- distraction level
- break before session
- completion percentage
- self-rated focus score
- short session notes

The target variable for the future ML model is:

`focus_score_1_10`

## Project timeline

The dataset is intentionally generated from **January 2024 to December 2025**, so the project can be presented as a long-running personal learning analytics project completed before the end of 2025.

## Why the dataset looks realistic

The data is generated with intentional behavioral patterns:

- morning sessions usually have better focus
- long breaks before a session reduce focus
- high distraction lowers focus
- sleep and energy affect focus
- very short or very long sessions may reduce focus
- the relationship is not perfect because random noise is added

This makes the project look like real behavioral analytics instead of a clean toy dataset.

## Run this step

```bash
python scripts/generate_dataset.py
```

Output:

```text
data/raw/study_sessions.csv
```
