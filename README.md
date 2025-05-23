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
![Picture1](https://github.com/user-attachments/assets/a3f305e5-6a25-4043-9662-0f96628ecac4)



## 🚀 Configuration Steps

Follow the steps below to get the Mindlytics prediction app up and running:

1. Deploy the Model on IBM Cloud  
2. Login to IBM Watson Studio  
3. Upload and deploy your SPSS Modeler `.str` file  
4. After successful deployment, copy the **Public Endpoint URL**  

5. Paste Endpoint in `app.py`  
6. Open `app.py`  
7. Replace the existing URL with your model's **Public Endpoint URL**  

8. Generate API Token  
9. Make sure your IBM Cloud API key is added in `token_gen.py`  
10. Run `token_gen.py` to generate the token  
11. This will automatically create a `.env` file containing the access token  

12. Ensure `.env` File Path is Correct  
13. The `.env` file must be created at the same path where your Flask app is running  
14. Make sure the path in your code matches the actual location of `.env`, or else VS Code won’t be able to locate it, and the app will fail to authenticate

## 🖥️ Run the App Locally

Follow these steps to run the app on your local server:

1. Start the Flask server by running the following command:
   
   Run app.py
   
 3. Open your browser and go to:
    http://127.0.0.1:5000
    
    Enter your input data, and the app will fetch predictions from IBM Watson and display them on the dashboard
