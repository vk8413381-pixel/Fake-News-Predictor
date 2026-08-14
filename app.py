from flask import Flask, render_template, request, jsonify
import joblib
import re

app = Flask(__name__)


# ==========================================
# Load trained ML model and TF-IDF vectorizer
# ==========================================

model = joblib.load("news_classifier.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")


# ==========================================
# Text preprocessing function
# ==========================================

def clean_text(text):

    # Convert to string
    text = str(text)

    # Convert text to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove punctuation and numbers
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# ==========================================
# Home page
# ==========================================

@app.route("/")
def home():

    return render_template("index.html")


# ==========================================
# Prediction API
# ==========================================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Get JSON data from frontend
        data = request.get_json()

        news_text = data.get("text", "")

        # Check empty input
        if not news_text.strip():

            return jsonify({
                "error": "Please enter some news text."
            }), 400


        # Clean news text
        cleaned_text = clean_text(news_text)


        # Convert text into TF-IDF
        text_vector = vectorizer.transform([cleaned_text])


        # Make prediction
        prediction = model.predict(text_vector)[0]


        # Get probability if model supports it
        if hasattr(model, "predict_proba"):

            probabilities = model.predict_proba(text_vector)[0]

            confidence = max(probabilities) * 100

        else:

            confidence = None


        # ==================================
        # Prediction mapping
        # ==================================

        if prediction == 0:

            result = "FAKE"

        else:

            result = "REAL"


        # Return result
        return jsonify({

            "prediction": result,

            "confidence": round(confidence, 2)
            if confidence is not None else None

        })


    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ==========================================
# Run Flask application
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True
    )