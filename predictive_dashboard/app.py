from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

# Watson API endpoint and key
URL = "https://au-syd.ml.cloud.ibm.com/ml/v4/deployments/4d099d2c-f60e-4cd0-8b2a-c4435b6db85e/predictions?version=2021-05-01"
BEARER_TOKEN = os.getenv("BEARER_TOKEN")  # Store your token in .env for safety

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get input values from form
        inputs = [
            int(request.form["q1"]), int(request.form["q2"]), 
            int(request.form["q3"]), int(request.form["q4"]), int(request.form["q5"])
        ]
        
        payload = {
            "input_data": [
                {
                    "fields": [
                        "1. In a semester, how often you felt nervous, anxious or on edge due to academic pressure? ",
                        "2. In a semester, how often have you been unable to stop worrying about your academic affairs? ",
                        "3. In a semester, how often have you had trouble relaxing due to academic pressure? ",
                        "6. In a semester, how often have you been so restless due to academic pressure that it is hard to sit still?",
                        "7. In a semester, how often have you felt afraid, as if something awful might happen?"
                    ],
                    "values": [inputs]  # User input
                }
            ]
        }

        response = requests.post(URL, headers=headers, json=payload)
        prediction = response.json()  # Prediction data from API
        print("Full API response:", prediction)
        try:
            prediction_value = float(prediction["predictions"][0]["values"][0][0])

        except (KeyError, IndexError) as e:
            print("Prediction parsing error:", e)
            prediction_value = "Error"
        
        # Map prediction to anxiety category
        if prediction_value <= 4.0:
            category = "Minimal Anxiety"
        elif prediction_value <= 9.0:
            category = "Mild Anxiety"
        elif prediction_value <= 14.0:
            category = "Moderate Anxiety"
        else:
            category = "Severe Anxiety"
            

        return render_template("index.html", prediction=prediction_value, category=category)
    
    return render_template("index.html", prediction=None, category=None)

if __name__ == "__main__":
    app.run(debug=True)
