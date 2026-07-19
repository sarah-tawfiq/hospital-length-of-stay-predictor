# 🏥 Hospital Length of Stay Predictor

##  Overview

This project predicts whether a patient is likely to have a **Short
Stay** (≤ 3 days) or a **Long Stay** (\> 3 days) using a Machine
Learning model trained on hospital patient data.

##  Problem Statement

Predict whether a patient's hospital stay will be: - **Short Stay (≤ 3
days)** - **Long Stay (\> 3 days)**

##  Dataset

Hospital Length of Stay Dataset (Microsoft)

Target: `long_stay`

##  Technologies Used

-   Python
-   Pandas
-   NumPy
-   Scikit-learn
-   Streamlit
-   Joblib

##  Machine Learning Model

Random Forest Classifier

  Metric          Score
  ----------- ---------
  Accuracy          94%
  Precision     92--95%
  Recall        93--95%
  F1-Score          94%

##  Input Features

-   Readmission Count
-   Gender
-   Hospital
-   Hematocrit
-   Neutrophils
-   Sodium
-   Glucose
-   Blood Urea Nitrogen
-   Creatinine
-   BMI
-   Pulse
-   Respiration
-   Secondary Diagnosis
-   Disease Indicators

### Engineered Features

-   Disease Count
-   High Risk
-   Abnormal Lab Score
-   High Pulse
-   High Respiration
-   Year, Month, Day, Day of Week, Quarter

##  Live Demo

https://hospital-length-of-stay-predictor-uesnhtogzy5hkw7rxeklao.streamlit.app/


##  Author

**Sarah Tawfiq**
