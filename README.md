# Fake-News-Predictor
Machine learning based fake news detection web application using Flask and NLP.

# Fake News Detection

A Machine Learning based web application that predicts whether a given news article is **Fake** or **Real**. The project uses Natural Language Processing (NLP), TF-IDF feature extraction, and a Machine Learning classification model, with Flask as the backend.

## 📌 Project Overview

Fake news can spread misleading or false information very quickly. This project uses Machine Learning to analyze the text of a news article and classify it as:

* **FAKE** — The model predicts that the news is likely fake.
* **REAL** — The model predicts that the news is likely real.

The trained Machine Learning model is integrated into a Flask web application where users can enter news text and receive a prediction along with the model's confidence score.

> **Note:** The prediction is a Machine Learning model output and should not be treated as a definitive fact-check. The system may make incorrect predictions, especially for news topics or writing styles that differ from its training data.

---

## 🚀 Features

* 📰 News article text input
* 🧹 Text preprocessing
* 🔢 TF-IDF based text feature extraction
* 🤖 Machine Learning based classification
* 🎯 Fake/Real prediction
* 📊 Prediction confidence
* 🌐 Flask web application
* 💻 HTML, CSS and JavaScript frontend
* 📦 Saved trained model using Joblib

---

## 🛠️ Technologies Used

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* TF-IDF
* Machine Learning Classification

### Backend

* Flask
* Python
* Joblib

### Frontend

* HTML
* CSS
* JavaScript

### Development Tools

* VS Code
* Git
* GitHub

---

## 🔄 Project Workflow

```text
News Article
     │
     ▼
Text Preprocessing
     │
     ▼
TF-IDF Vectorization
     │
     ▼
Trained ML Classifier
     │
     ▼
Prediction
     │
 ┌───┴────┐
 ▼        ▼
FAKE     REAL
     │
     ▼
Confidence Score
     │
     ▼
Web Interface
```

---

## 📁 Project Structure

```text
Fake-News-Predictor/
│
├── app.py
├── requirements.txt
├── README.md
│
├── news_classifier.pkl
├── tfidf_vectorizer.pkl
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

---

## 🧠 Machine Learning Pipeline

### 1. Data Collection

A labelled news dataset containing real and fake news articles is used for training the model.

### 2. Data Preprocessing

The news text is cleaned before being passed to the Machine Learning model.

Typical preprocessing includes:

* Converting text to lowercase
* Removing URLs
* Removing unnecessary characters
* Removing extra spaces

### 3. TF-IDF

TF-IDF (Term Frequency-Inverse Document Frequency) converts the cleaned news text into numerical features that can be used by the Machine Learning model.

### 4. Model Training

The TF-IDF features are used to train a classification model.

### 5. Model Saving

The trained classifier and TF-IDF vectorizer are saved using Joblib:

```text
news_classifier.pkl
tfidf_vectorizer.pkl
```

### 6. Prediction

When a user enters new news:

```text
Input News
    ↓
Preprocessing
    ↓
TF-IDF
    ↓
ML Model
    ↓
FAKE / REAL
```

---

## 💻 How to Run the Project Locally

### Step 1: Clone the Repository

```bash
git clone https://github.com/vk8413381-pixel/Fake-News-Predictor.git
```

Move into the project directory:

```bash
cd Fake-News-Predictor
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run Flask

```bash
python app.py
```

### Step 5: Open the Website

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

---

## 📊 Model Output

Example:

```text
Prediction: REAL
Confidence: 92.35%
```

or:

```text
Prediction: FAKE
Confidence: 87.64%
```

The confidence score represents the model's estimated probability, not a guarantee that the article is factually true or false.

---

## 🔌 Flask Backend

The Flask application provides the prediction endpoint:

```text
POST /predict
```

The frontend sends the news article to the Flask backend, which:

1. Receives the news text.
2. Preprocesses the text.
3. Converts it using the saved TF-IDF vectorizer.
4. Passes the features to the trained classifier.
5. Returns the prediction and confidence score.

---

## 📦 Requirements

Main dependencies include:

```text
Flask
joblib
scikit-learn
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## ⚠️ Limitations

* The model can make incorrect predictions.
* Accuracy depends on the quality and diversity of the training dataset.
* The model may not perform well on completely new topics or writing styles.
* A Machine Learning prediction does not replace professional fact-checking.
* Confidence scores should not be interpreted as absolute certainty.

---

## 🔮 Future Improvements

Possible improvements include:

* Add a larger and more diverse dataset.
* Compare Logistic Regression, Naive Bayes and SVM.
* Use cross-validation and hyperparameter tuning.
* Improve text preprocessing.
* Add explainable predictions.
* Add a news URL input option.
* Use advanced NLP models such as BERT.
* Deploy the application online.
* Add prediction history.
* Improve the UI and responsiveness.

---

## 👨‍💻 Author

**Vicky Kumar**

Computer Science & Engineering Student

---

## ⭐ Project Purpose

This project was developed as a Machine Learning and Web Development project to demonstrate:

* Natural Language Processing
* Text classification
* Machine Learning model training
* Model deployment
* Flask backend development
* Frontend and backend integration

If you find this project useful, consider giving the repository a ⭐ on GitHub.

