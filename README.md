# Personal Learning Behaviour Tracker with ML and Agentic Insights

This repository contains a personal study behavior analytics project built with Python, Pandas, scikit-learn, and an agentic weekly insight workflow.

The main goal is to explore which session-level behavioral features influence self-rated study focus and to generate weekly recommendations based on session patterns.

## What is included

- `data/raw/study_sessions.csv`: raw study session data covering January 2024 through December 2025.
- `data/processed/cleaned_study_sessions.csv`: cleaned and preprocessed session data used for modeling and insight generation.
- `notebooks/01_data_cleaning_eda.ipynb`: exploratory data analysis, data cleaning, feature inspection, and visualization of study behavior.
- `notebooks/02_model_training.ipynb`: machine learning pipeline comparing Random Forest, Gradient Boosting, and Ridge Regression for predicting `focus_score_1_10`.
- `notebooks/03_agentic_weekly_insights.ipynb`: weekly summary generation, rule-based weekly insights, and optional LangChain/OpenAI insight generation.
- `models/focus_score_model.pkl`: saved regression model artifact from the training workflow.
- `outputs/reports/`: CSV reports including feature importance, grouped feature importance, and model predictions.
- `outputs/weekly_insights/`: generated weekly insight text files, both basic and LangChain/OpenAI versions.

## Dataset

Each row represents one study session and includes session metadata, behavioral signals, and a self-rated focus score.

Important columns include:

- `session_id`
- `date`
- `day_of_week`
- `start_time`
- `end_time`
- `hour_of_day`
- `time_of_day`
- `duration_min`
- `topic`
- `topic_type`
- `difficulty_1_5`
- `sleep_hours`
- `energy_before_1_10`
- `distraction_level_1_10`
- `break_before_days`
- `location`
- `device_used`
- `completion_percent`
- `focus_score_1_10`
- `notes`
- engineered time features: `year`, `month`, `week`, `weekday_number`

## Machine learning model

The modeling pipeline is built in `notebooks/02_model_training.ipynb`.

- Target variable: `focus_score_1_10`
- Final selected model: tuned `GradientBoostingRegressor`
- Other compared models: `RandomForestRegressor` and `Ridge`
- Preprocessing uses scaling for numerical features and one-hot encoding for categorical features.
- The project also includes feature importance analysis to explain which behavioral factors matter most.

## Weekly insight workflow

The third notebook generates weekly summaries and insights from the processed study session data.

- Basic rule-based insight generation uses session averages and thresholds for sleep, distraction, completion, and focus.
- Optional LangChain/OpenAI insight generation is included if `OPENAI_API_KEY` is available.
- Generated files are saved under `outputs/weekly_insights/`.

## Project structure

```text
personal_learning_behavior_tracker/
├── data/
│   ├── processed/
│   │   └── cleaned_study_sessions.csv
│   └── raw/
│       └── study_sessions.csv
├── models/
│   └── focus_score_model.pkl
├── notebooks/
│   ├── 01_data_cleaning_eda.ipynb
│   ├── 02_model_training.ipynb
│   └── 03_agentic_weekly_insights.ipynb
├── outputs/
│   ├── reports/
│   │   ├── feature_importance.csv
│   │   ├── grouped_feature_importance.csv
│   │   └── model_predictions.csv
│   └── weekly_insights/
│       ├── basic_weekly_insight_*.txt
│       └── langchain_weekly_insight_*.txt
├── requirements.txt
├── README.md
├── README_STEP_1.md
└── .gitignore
```

## Dependencies

Install the Python dependencies with:

```bash
pip install -r requirements.txt
```

The main dependencies include:

- `pandas`
- `numpy`
- `matplotlib`
- `scikit-learn`
- `jupyter`
- `ipykernel`
- `joblib`
- `langchain`
- `langchain-openai`
- `openai`
- `python-dotenv`

## How to run

1. Open the repository in VS Code or Jupyter.
2. Activate your Python environment and install dependencies.
3. Open and run the notebooks in order:
   - `notebooks/01_data_cleaning_eda.ipynb`
   - `notebooks/02_model_training.ipynb`
   - `notebooks/03_agentic_weekly_insights.ipynb`
4. If you want LangChain/OpenAI insights, set:

```bash
export OPENAI_API_KEY="your_api_key"
# optional:
export OPENAI_API_BASE="https://api.openai.com/v1"
export OPENAI_MODEL_NAME="gpt-4o-mini"
```

## Notes

- The notebook kernel should be configured to use the same Python environment that has the dependencies installed.
- If `OPENAI_API_KEY` is not available, the weekly insights workflow will fall back to the rule-based insight generator.


## Summary

This project combines EDA, regression modeling, feature importance analysis, and weekly recommendation generation to turn personal study session behavior into actionable insights.
