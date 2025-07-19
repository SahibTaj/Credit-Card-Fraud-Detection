# 💳 Credit Card Fraud Detection 🔍⚠️  
> Stop fraudsters before they stop your funds!

![Python](https://img.shields.io/badge/Made%20with-Python-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Backend-Flask-red?style=for-the-badge&logo=flask)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-yellow?style=for-the-badge&logo=scikit-learn)

---

## 🧠 Project Overview

This is a **Machine Learning-powered web API** that detects **fraudulent credit card transactions**. It’s your digital bodyguard for payment security 💪💳.

**Built With:**
- 🐍 Python for ML Model Training
- 🔬 Scikit-Learn for classification
- 🌐 Flask for API
- 💻 Runs completely locally (for now!)

> “If catching fraud was a video game, this app would be Final Boss level. 😎”

---

## 📊 Dataset

This project uses the [Kaggle Credit Card Fraud Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud), containing:
- 284,807 transactions
- 492 fraud cases 😱  
- Imbalanced? Oh yeah — but we’ve got that covered with smart resampling tricks (SMOTE and friends).

---

## 📁 Project Structure
Credit-Card-Fraud-Detection/
│
├── app.py # Flask API
├── models/
│ └── best_model.pkl # Trained model
├── requirements.txt # Python dependencies
├── utils/
│ └── preprocess.py # (optional) preprocessing code
├── README.md # This file 😄
└── venv/ # Virtual environment (not pushed to Git)


---

## 🧪 How It Works

- Accepts 29 features: `V1...V28` + `Amount`
- Runs them through a trained classifier (e.g., Logistic Regression / Random Forest)
- Returns if the transaction is **Fraud** or **Not Fraud**, with a confidence score

---

## 🧰 Setup Instructions

### 🐍 Local Installation

> Don’t worry, this won’t take longer than a coffee break ☕

```bash
# Clone the repository
git clone https://github.com/SahibTaj/Credit-Card-Fraud-Detection.git
cd Credit-Card-Fraud-Detection

# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install all dependencies
pip install -r requirements.txt
