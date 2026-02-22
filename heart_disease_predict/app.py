# import streamlit as st
# import pandas as pd
# import joblib

# model=joblib.load('KNN_heart (1).pkl')
# scaler=joblib.load('scaler (2).pkl')
# expected_columns=joblib.load('columns (1).pkl')


# st.title('heart stroke prediction by Samay')
# st.markdown('Provide the following details')

# age=st.slider('Age',18,100,40)
# sex=st.selectbox('SEX',['M','F'])
# chest_pain=st.selectbox('chest Pain Type',['ATA(Atypical Angina) [Risk type-🟠 Medium]','NAP(Non-Anginal Pain)[Risk type-🟢 Low]','TA(Typical Angina) [Risk type-🔴 High]','ASY(Asymptomatic)[Risk type-🔴 High (Silent Risk)]'])
# resting_bp=st.number_input("Resting Blood Pressure(mm hg)",80,200,120)
# cholestrol=st.number_input("Cholestrol(mg/dl)",100,600,200)
# fasting_bs=st.selectbox("Fasting Blood Sugar > 120 mg/dL",[0,1])
# resting_ecg=st.selectbox("Resting ECG",["Normal","ST","LVH"])
# max_hr=st.slider("Max Heart Rate",60,220,150)
# exercise_agina=st.selectbox("Exercise-Induced Angina: Do you feel chest pain or pressure during physical activity?",['YES','NO'])
# oldpeak=st.slider("Oldpeak (ST Depression): The amount of change seen in the heart’s ECG during exercise.",0.0,6.0,1.0)
# st_slope=st.selectbox("ST Slope: Describes the shape of the heart’s electrical pattern during peak exercise.",["Upward (Upsloping) – Often normal","Flat – May indicate risk ⚠️","Downward (Downsloping) – Higher risk indicator ☠️"])

# if st.button("predict"):
#         raw_input = {
#         'Age': age,
#         'RestingBP': resting_bp,
#         'Cholesterol': cholestrol,
#         'FastingBS': fasting_bs,
#         'MaxHR': max_hr,
#         'Oldpeak': oldpeak,
#         'Sex_' + sex: 1,
#         'ChestPainType_' + chest_pain: 1,
#         'RestingECG_' + resting_ecg: 1,
#         'ExerciseAngina_' + exercise_agina: 1,
#         'ST_Slope_' + st_slope: 1
#     }
    
#         input_df=pd.DataFrame([raw_input])

#         for col in expected_columns:
#          if col not in input_df.columns:
#             input_df[col] = 0

#         input_df = input_df[expected_columns]

#         scaled_input = scaler.transform(input_df)

#         prediction = model.predict(scaled_input)[0]

#         if prediction == 1:
#          st.error("⚠️ High Risk of Heart Disease")
#         else:
#          st.success("✅ Low Risk of Heart Disease")
        




# import streamlit as st
# import pandas as pd
# import joblib

# # -------------------- Page Config --------------------
# st.set_page_config(page_title="Heart Disease Predictor", page_icon="❤️", layout="centered")

# # -------------------- Custom Styling --------------------
# st.markdown("""
# <style>
# .main {
#     background-color: #f5f7fa;
# }
# .stButton>button {
#     background-color: #e63946;
#     color: white;
#     font-size: 18px;
#     border-radius: 10px;
#     padding: 10px 25px;
# }
# .stButton>button:hover {
#     background-color: #d62828;
#     color: white;
# }
# .card {
#     padding: 20px;
#     border-radius: 15px;
#     background-color: white;
#     box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
# }
# </style>
# """, unsafe_allow_html=True)

# # -------------------- Load Model --------------------
# model = joblib.load('KNN_heart (1).pkl')
# scaler = joblib.load('scaler (2).pkl')
# expected_columns = joblib.load('columns (1).pkl')

# # -------------------- Header --------------------
# st.markdown("<h1 style='text-align:center; color:#e63946;'>❤️ Heart Disease Prediction</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align:center;'>Developed by <b>Samay</b></p>", unsafe_allow_html=True)
# st.markdown("---")

# st.markdown("### 📝 Provide Patient Details")

# # -------------------- Input Section --------------------
# with st.container():
#     col1, col2 = st.columns(2)

#     with col1:
#         age = st.slider('Age', 18, 100, 40)
#         sex = st.selectbox('Sex', ['M', 'F'])
#         resting_bp = st.number_input("Resting Blood Pressure (mm hg)", 80, 200, 120)
#         cholestrol = st.number_input("Cholesterol (mg/dl)", 100, 600, 200)
#         fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
#         max_hr = st.slider("Max Heart Rate", 60, 220, 150)

#     with col2:
#         chest_pain = st.selectbox(
#             'Chest Pain Type',
#             ['ATA(Atypical Angina) [Risk type-🟠 Medium]',
#              'NAP(Non-Anginal Pain)[Risk type-🟢 Low]',
#              'TA(Typical Angina) [Risk type-🔴 High]',
#              'ASY(Asymptomatic)[Risk type-🔴 High (Silent Risk)]']
#         )
#         resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
#         exercise_agina = st.selectbox(
#             "Exercise-Induced Angina: Do you feel chest pain or pressure during physical activity?",
#             ['YES', 'NO']
#         )
#         oldpeak = st.slider(
#             "Oldpeak (ST Depression): Change in ECG during exercise.",
#             0.0, 6.0, 1.0
#         )
#         st_slope = st.selectbox(
#             "ST Slope: Shape of heart’s electrical pattern during peak exercise.",
#             ["Upward (Upsloping) – Often normal",
#              "Flat – May indicate risk ⚠️",
#              "Downward (Downsloping) – Higher risk indicator ☠️"]
#         )

# st.markdown("---")

# # -------------------- Prediction Button --------------------
# if st.button("🔍 Predict Heart Risk"):

#     raw_input = {
#         'Age': age,
#         'RestingBP': resting_bp,
#         'Cholesterol': cholestrol,
#         'FastingBS': fasting_bs,
#         'MaxHR': max_hr,
#         'Oldpeak': oldpeak,
#         'Sex_' + sex: 1,
#         'ChestPainType_' + chest_pain: 1,
#         'RestingECG_' + resting_ecg: 1,
#         'ExerciseAngina_' + exercise_agina: 1,
#         'ST_Slope_' + st_slope: 1
#     }

#     input_df = pd.DataFrame([raw_input])

#     for col in expected_columns:
#         if col not in input_df.columns:
#             input_df[col] = 0

#     input_df = input_df[expected_columns]
#     scaled_input = scaler.transform(input_df)
#     prediction = model.predict(scaled_input)[0]

#     st.markdown("---")

#     if prediction == 1:
#         st.error("⚠️ High Risk of Heart Disease")
#         st.markdown("### 🚨 Please consult a cardiologist immediately.")
#     else:
#         st.success("✅ Low Risk of Heart Disease")
#         st.markdown("### ❤️ Your heart health looks stable. Maintain a healthy lifestyle!")



import streamlit as st
import pandas as pd
import joblib

# Page config
st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)

# Load model
# model = joblib.load('KNN_heart.pkl')
# scaler = joblib.load('scaler.pkl')
# expected_columns = joblib.load('columns.pkl')

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "KNN_heart.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))
expected_columns = joblib.load(os.path.join(BASE_DIR, "columns.pkl"))

# Custom CSS for background & button
st.markdown("""
<style>
/* Page background */
.css-18e3th9, .css-1d391kg {
    background-color: #f5f7fa;
}

/* Button style */
button.css-1emrehy.edgvbvh3 { 
    background-color: #ff4b4b;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    height: 3em;
    width: 100%;
}

/* Center title */
h1 {
    text-align: center;
    color: #ff4b4b;
}
h4 {
    text-align: center;
    color: #333333;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>❤️ Heart Disease Prediction</h1>", unsafe_allow_html=True)
st.markdown("<h4>Developed by Samay</h4>", unsafe_allow_html=True)
st.write("----")

st.markdown("### 📝 Provide Patient Details")

# ---------------- Single Column Inputs ----------------
age = st.slider('Age', 18, 100, 40)
sex = st.selectbox('Sex', ['M', 'F'])
chest_pain = st.selectbox(
    'Chest Pain Type',
    ['ATA(Atypical Angina) [Risk type-🟠 Medium]',
     'NAP(Non-Anginal Pain)[Risk type-🟢 Low]',
     'TA(Typical Angina) [Risk type-🔴 High]',
     'ASY(Asymptomatic)[Risk type-🔴 High (Silent Risk)]']
)
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholestrol = st.number_input("Cholesterol (mg/dl)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr = st.slider("Max Heart Rate", 60, 220, 150)
exercise_angina = st.selectbox(
    "Exercise-Induced Angina: Do you feel chest pain or pressure during physical activity?",
    ['YES', 'NO']
)
oldpeak = st.slider(
    "Oldpeak (ST Depression): The amount of change seen in the heart’s ECG during exercise.",
    0.0, 6.0, 1.0
)
st_slope = st.selectbox(
    "ST Slope: Describes the shape of the heart’s electrical pattern during peak exercise.",
    ["Upward (Upsloping) – Often normal",
     "Flat – May indicate risk ⚠️",
     "Downward (Downsloping) – Higher risk indicator ☠️"]
)

st.write("----")

# ---------------- Prediction ----------------
if st.button("🔍 Predict Heart Disease Risk"):

    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholestrol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    st.write("## 🩺 Prediction Result")
    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")