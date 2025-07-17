from flask import Flask, request, jsonify
import joblib
import numpy as np

model = joblib.load('models/best_model.pkl')  # ✅ Path to your trained model

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Fraud Detection API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.json
        
        features = np.array([input_data['features']]).reshape(1, -1)

        proba = model.predict_proba(features)[0][1]  # class 1 = fraud

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
