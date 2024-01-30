# Student Score Prediction

## Overview
This project involves building a machine learning model to predict student scores based on various factors such as gender, ethnicity, parental level of education, lunch, and test preparation course. The goal is to understand how these variables impact students' performance in exams.

## Problem Statement
The primary problem is to analyze and predict the test scores of students, taking into account multiple influencing factors.

## Data Collection
- **Dataset Source:** [Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977)
- **Data Description:**
  - Columns: 8
  - Rows: 1000

## Project Structure
- **Exploratory Data Analysis (EDA):** Jupyter Notebook (`eda.ipynb`) containing data exploration, visualization, and insights.
- **Model Development:** Python script (`model.py`) implementing machine learning model training and evaluation.
- **Web Application:** Flask application (`app.py`) for deploying the model and allowing users to input variables and receive predictions.
- **Requirements:** `requirements.txt` file listing project dependencies.

## Dependencies
- Python 3.x
- Flask
- Pandas
- Scikit-Learn
- Matplotlib
- Seaborn

## Usage
1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Explore the dataset and insights using `eda.ipynb`.
4. Train and evaluate the machine learning model using `model.py`.
5. Deploy the model with the Flask web application using `python app.py`.
6. Access the web interface at `http://localhost:5000` in your web browser.
7. Input student information and receive score predictions.

## Model Training
- The machine learning model is trained in the `model.py` script.
- Modify hyperparameters or try different algorithms for experimentation.

## Acknowledgments
- Dataset source: [Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977)

## License
This project is licensed under the [MIT License](LICENSE).

## Author
Aswathi
