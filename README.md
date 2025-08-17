KNN – Diabetes Prediction

Project Overview
This project is a Machine Learning Web Application built with Flask, HTML, and CSS.
It uses the K-Nearest Neighbors (KNN) algorithm to predict whether a person is Diabetic or Not Diabetic based on health parameters.

Problem Statement
Diabetes is a growing health concern. Early prediction can help in lifestyle adjustments and preventive measures.
This project aims to provide a basic prediction system using KNN, a supervised ML algorithm.

Dataset

Synthetic / Sample dataset generated with columns:
• Age
• BMI
• Glucose Level
• Diabetes (0 = Not Diabetic, 1 = Diabetic)

The dataset is used to train the KNN classifier.

Model

Algorithm: K-Nearest Neighbors (KNN)

Library: Scikit-learn

Output:
0 → Not Diabetic
1 → Diabetic

How to Run the Project

Step 1: Train the Model
python train_model.py

Step 2: Start Flask Server
python app.py

Step 3: Open in Browser
http://127.0.0.1:5000

User Interface

<img width="1600" height="792" alt="image" src="https://github.com/user-attachments/assets/aedfd2c7-f961-4675-8596-7fef37b06911" />


Requirements
Install dependencies before running:
pip install flask scikit-learn pandas numpy

Next Steps

Improve dataset with real health data

Enhance frontend with Bootstrap or Tailwind CSS

Deploy the app on Heroku, Render, or Vercel

Output

Input: Age, BMI, Glucose

Output: Diabetic or Not Diabetic
