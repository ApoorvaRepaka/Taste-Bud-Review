from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "*"}})  # Allow requests from frontend

# Load model & vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json  
        if not data or "review" not in data:
            return jsonify({"error": "Invalid request. 'review' field is required."}), 400
        
        review_text = data["review"]
        transformed_text = vectorizer.transform([review_text]).toarray()
        prediction = model.predict(transformed_text)
        
        sentiment = "Positive" if prediction[0] == 1 else "Negative"
        return jsonify({"sentiment": sentiment})
    
    except Exception as e:
        print("Error:", str(e))  
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
