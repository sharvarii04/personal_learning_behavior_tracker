# Personal Learning Behaviour Tracker with ML and Agentic Insights

This project analyzes personal study behavior using Python, Pandas, machine learning, and a simple agentic insight workflow.

The goal is to understand which behavioral factors influence study focus and to generate weekly learning recommendations based on study patterns.

## Project Timeline

The dataset covers study sessions from January 2024 to December 2025.

## Main Features

- Study session data cleaning and preprocessing
- Exploratory data analysis
- Focus score prediction using machine learning
- Feature importance analysis
- Weekly learning summary generation
- Rule-based agentic recommendation workflow

## Dataset

Each row represents one study session.

Important columns include:

- date
- time_of_day
- duration_min
- topic_type
- sleep_hours
- energy_before_1_10
- distraction_level_1_10
- completion_percent
- focus_score_1_10

## Model

A Random Forest Regressor was trained to predict `focus_score_1_10`.

Model performance:

- Mean Absolute Error: 0.825
- Root Mean Squared Error: 1.025
- R² Score: 0.645

## Key Findings

The model found that `completion_percent`, `distraction_level_1_10`, `hour_of_day`, `sleep_hours`, and `energy_before_1_10` were among the most important predictors of focus score.

The exploratory analysis also showed that morning sessions had the highest average focus score, while night sessions had the lowest.

## Project Structure

```text
personal_learning_behavior_tracker/
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── notebooks/
├── outputs/
│   ├── reports/
│   └── weekly_insights/
├── requirements.txt
├── .gitignore
└── README.md

## How to Run

### 1. Open the project in VS Code

Open the project folder in VS Code:

```text
personal_learning_behavior_tracker
