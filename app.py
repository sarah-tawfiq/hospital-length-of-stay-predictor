import streamlit as st
import pandas as pd
import joblib
from datetime import date

st.set_page_config(page_title="Hospital Length of Stay Predictor", page_icon="🏥", layout="wide")

model = joblib.load("best_rf_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

st.title("🏥 Hospital Length of Stay Predictor")

visit_date = st.date_input("Visit Date", value=date.today())

c1,c2=st.columns(2)
with c1:
    rcount=st.number_input("Readmission Count",0,20,1)
    gender=st.selectbox("Gender",["Female","Male"])
    fac=st.selectbox("Hospital",["A","B","C","D","E"])
with c2:
    hematocrit=st.number_input("Hematocrit",40.0)
    neutrophils=st.number_input("Neutrophils",50.0)
    sodium=st.number_input("Sodium",140.0)
    glucose=st.number_input("Glucose",100.0)
    bloodureanitro=st.number_input("Blood Urea Nitrogen",20.0)
    creatinine=st.number_input("Creatinine",1.0)
    bmi=st.number_input("BMI",25.0)
    pulse=st.number_input("Pulse",80)
    respiration=st.number_input("Respiration",18.0)
    secondarydiagnosisnonicd9=st.number_input("Secondary Diagnosis",0)

st.subheader("Diseases")
disease_names=[
"dialysisrenalendstage","asthma","irondef","pneum","substancedependence",
"psychologicaldisordermajor","depress","psychother","fibrosisandother",
"malnutrition","hemo"]
vals={}
cols=st.columns(3)
for i,n in enumerate(disease_names):
    with cols[i%3]:
        vals[n]=1 if st.checkbox(n) else 0

year=visit_date.year
month=visit_date.month
day=visit_date.day
dayofweek=visit_date.weekday()
quarter=(month-1)//3+1
disease_count=sum(vals.values())
high_risk=int(disease_count>=3)
abnormal_lab_score = (
    int(glucose > 140)
    + int(creatinine > 1.3)
    + int(bloodureanitro > 20)
)
high_pulse=int(pulse>100)
high_respiration=int(respiration>20)

row={c:0 for c in feature_columns}
row.update({
"rcount":rcount,
**vals,
"hematocrit":hematocrit,
"neutrophils":neutrophils,
"sodium":sodium,
"glucose":glucose,
"bloodureanitro":bloodureanitro,
"creatinine":creatinine,
"bmi":bmi,
"pulse":pulse,
"respiration":respiration,
"secondarydiagnosisnonicd9":secondarydiagnosisnonicd9,
"gender_M":1 if gender=="Male" else 0,
"facid_B":1 if fac=="B" else 0,
"facid_C":1 if fac=="C" else 0,
"facid_D":1 if fac=="D" else 0,
"facid_E":1 if fac=="E" else 0,
"year":year,"month":month,"day":day,"dayofweek":dayofweek,"quarter":quarter,
"disease_count":disease_count,
"high_risk":high_risk,
"abnormal_lab_score":abnormal_lab_score,
"high_pulse":high_pulse,
"high_respiration":high_respiration
})


if st.button("Predict"):
    X=pd.DataFrame([row])[feature_columns]
    st.write(X)
    pred=model.predict(X)[0]
    prob=model.predict_proba(X)[0].max()*100
    if pred==1:
        st.error(f"Prediction: Long Stay\n\nConfidence: {prob:.2f}%")
    else:
        st.success(f"Prediction: Short Stay\n\nConfidence: {prob:.2f}%")
