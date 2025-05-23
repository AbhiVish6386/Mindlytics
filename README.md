# 🧠 Mindlytics – Mental Health Prediction Using IBM Watson

**Mindlytics** is a web-based mental health prediction tool that uses a machine learning model trained in **SPSS Modeler 18.5** and deployed on **IBM Watson Studio**. The user fills out a questionnaire, and the application sends this data to Watson's public API endpoint. Based on the model's prediction, the user is shown their estimated mental health category in real-time.

---

## 🌟 Features

- 📋 Five-question anxiety assessment form
- 🤖 Predicts mental health condition (e.g., Moderate Anxiety)
- ☁️ Model hosted on **IBM Watson Studio**
- 🔗 Uses Watson's **public API endpoint** for prediction
- 🌐 Built with **Flask**, HTML, and CSS
- 📈 Real-time result display with gauge-style dashboard

---

## 🧠 Sample Questions

1. Nervous, anxious, or on edge?
2. Unable to stop worrying?
3. Trouble relaxing?
4. So restless it's hard to sit still?
5. Felt afraid something awful might happen?

Each question allows the user to choose a level (e.g., *Minimal*, *Mild*, *Moderate*, *Severe*).

---

## 🛠 Tech Stack

| Layer       | Technology              |
|------------|--------------------------|
| Frontend    | HTML, CSS               |
| Backend     | Python Flask            |
| ML Model    | SPSS Modeler 18.5       |
| Hosting     | IBM Watson Studio       |
| API Comm.   | REST (Public Endpoint)  |

---

## 🚀 How It Works

1. User selects answers from the dropdown form.
2. The Flask app sends the collected data to the **IBM Watson ML API**.
3. The trained model processes the inputs and returns a numeric prediction.
4. The result is displayed on a speedometer-style dashboard with a category label (e.g., Moderate Anxiety).

---
## GUI
https://github.com/AbhiVish6386/Mindlytics/blob/dcab215d204291b17ba281e359fc8b4d0da7cfee/Picture1.png


## 🧪 Example API Interaction

```python
# Sample Python code (requests) for sending data to Watson
import requests

payload = {
  "input_data": [{
    "fields": ["Q1", "Q2", "Q3", "Q4", "Q5"],
    "values": [["Minimal", "Mild", "Moderate", "Minimal", "Mild"]]
  }]
}

response = requests.post(
  "<YOUR_WATSON_MODEL_ENDPOINT>",
  json=payload,
  headers={"Authorization": "Bearer <YOUR_API_KEY>"}
)

prediction = response.json()
