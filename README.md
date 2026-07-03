# Spam Classifier ML Project

## Overview
This project is a Machine Learning model that classifies SMS messages as **Spam or Not Spam (Ham)**.

It uses Natural Language Processing (NLP) and a Naive Bayes classifier to detect spam messages with high accuracy.

---

## Tech Stack
- Python
- Scikit-learn
- Pandas
- Joblib
- NLP (Text Processing)
- CountVectorizer
- Multinomial Naive Bayes

---

## How It Works
1. Load SMS dataset
2. Clean and preprocess text data
3. Convert text into numerical features using CountVectorizer
4. Train a Naive Bayes model
5. Predict whether a message is Spam or Not Spam

---

## Project Structure
```
SpamEmailClassifier/
│
├── model/
│   └── spam_model.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

---

## How to Run

```bash
pip install -r requirements.txt
python app.py
```

---

## Example Usage

```
Input: Win a free iPhone now
Output: Spam !!

Input: Hey, are we meeting today?
Output: Not Spam ~
```

---

## Sample Prediction

The model predicts:
- `1` → Spam
- `0` → Not Spam

---

## Installation

```bash
pip install scikit-learn joblib pandas
```

---

## Features
- Real-time SMS classification
- Simple CLI interface
- Lightweight ML model
- Beginner-friendly NLP project

---

## Author
Built as a beginner Machine Learning project to understand NLP, classification, and model deployment basics.

---

## Future Improvements
- Add Flask web interface 🌐
- Improve accuracy using TF-IDF + SVM
- Deploy online as a web app
```

