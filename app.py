from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the trained model
model = joblib.load('models/best_model.pkl')  # ✅ Path to your trained model

# Create Flask app
app = Flask(__name__)

# Home route (optional)
@app.route('/')
def home():
    return "🚀 Fraud Detection API is running!"

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        input_data = request.json
        
        # Extract features (V1–V28, Amount)
        features = np.array([input_data['features']]).reshape(1, -1)

        # ✅ Get fraud probability
        proba = model.predict_proba(features)[0][1]  # class 1 = fraud

        # ✅ Optional: use threshold (0.5) to decide label
        threshold = 0.5
        prediction = "Fraud" if proba > threshold else "Not Fraud"

        return jsonify({
            'prediction': prediction,
            'probability': round(proba, 4)  # Confidence in fraud
        })

    except Exception as e:
        return jsonify({'error': str(e)})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
