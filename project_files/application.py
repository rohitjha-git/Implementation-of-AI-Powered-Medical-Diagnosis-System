import streamlit as st
import pandas as pd
import pickle

# Load Models
with open("project_files/Models/diabetes_model.sav", 'rb') as f:
    diabetes_model = pickle.load(f)
with open("project_files/Models/heart_disease_model.sav", 'rb') as f:
    heart_model = pickle.load(f)
with open("project_files/Models/lungs_disease_model.sav", 'rb') as f:
    lungs_model = pickle.load(f)
with open("project_files/Models/parkinsons_model.sav", 'rb') as f:
    parkinson_model = pickle.load(f)

# Streamlit Configuration
st.set_page_config(page_title="AI-Powered Medical Diagnosis System", page_icon="🧠")

# Hiding Streamlit add-ons
hide_st_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Custom CSS Styling
selectbox_style = """
<style>
    div[data-baseweb="select"] {
        border: 3px solid #FDFCDC !important; 
        border-radius: 10px !important;  
        padding: 0px !important;
        background-color: #f9f9f9 !important;
    }
    div[data-baseweb="select"] * {
        color: Black !important;
    }
</style>
"""
sidebar_style = """
<style>
    [data-testid="stSidebar"] {
        background-color: #1976D2 !important;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
</style>
"""
st.markdown(selectbox_style, unsafe_allow_html=True)
st.markdown(sidebar_style, unsafe_allow_html=True)

# App Title
st.sidebar.title("AI-Powered Medical Diagnosis System")
# Sidebar Navigation
option = st.sidebar.selectbox("Select Diagnosis Type", ["Home", "Diabetes", "Heart Disease", "Lung Disease", "Parkinson's Disease"])

# Home Page
if option == "Home":
    st.markdown("""
        <div style="text-align: center;">
            <h1>⚕️ Welcome to the AI-Powered Medical Diagnosis System</h1>
        </div>
    """, unsafe_allow_html=True)


     # Display Image from URL
    image_url = "https://services.brieflands.com/cdn/serve/316a3/d822ee1d2d9bfa6c9ed8e7c36ae61a1d8705918c/Explore%20how%20AI%20is%20revolutionizing%20healthcare,%20from%20disease%20tracking%20and%20pathology%20to%20psychiatric%20care,%20promising%20a%20transformative%20impact%20on%20medicine..jpeg"
    st.image(image_url, caption="AI in Healthcare", use_container_width=True)


    st.write("""
        Maintaining good health is essential for a happy and active life. Follow these key principles to enhance your well-being.  

        ### ✅ Benefits of Good Health:
        - **Increased Energy**: Feel more active and productive throughout the day.  
        - **Stronger Immune System**: Reduce the risk of infections and diseases.  
        - **Improved Mental Well-being**: Stay positive and manage stress effectively.  
        - **Longevity**: Live a longer, healthier life with fewer health complications.  

        ### 🛠 Key Health Tips:
        - **Balanced Diet** 🥗: Eat a variety of nutrient-rich foods, including fruits, vegetables, and proteins.  
        - **Regular Exercise** 🏃‍♂️: Engage in at least 30 minutes of physical activity daily.  
        - **Hydration** 💧: Drink plenty of water to keep your body hydrated and functioning well.  
        - **Quality Sleep** 😴: Aim for 7-9 hours of sleep each night for optimal recovery.  
        - **Mental Wellness** 🧘‍♀️: Practice mindfulness, meditation, and stress management techniques.  
        - **Routine Checkups** 🏥: Visit a doctor regularly for preventive healthcare and screenings.  
    """)

    st.warning("⚠️ This is an AI-based prediction. Please visit a doctor for professional medical advice.")

# Input Field Template
def display_input(label, tooltip, key, type="text"):
    if type == "text":
        return st.text_input(label, key=key, help=tooltip)
    elif type == "number":
        return st.number_input(label, key=key, help=tooltip, step=1)

# Prediction Logic for Different Diseases
def predict_diabetes():
    st.subheader("Diabetes Diagnosis")
    pregnancies = st.number_input("Pregnancies", min_value=0)
    glucose = st.number_input("Glucose", min_value=0)
    blood_pressure = st.number_input("Blood Pressure", min_value=0)
    skin_thickness = st.number_input("Skin Thickness", min_value=0)
    insulin = st.number_input("Insulin", min_value=0)
    bmi = st.number_input("BMI", min_value=0.0)
    diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0)
    age = st.number_input("Age", min_value=0)
    
    if st.button("Predict Diabetes"):
        result = diabetes_model.predict([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
        st.write("Result:", "Positive" if result[0] == 1 else "Negative")

def predict_heart_disease():
    st.subheader("Heart Disease Diagnosis")
    age = st.number_input("Age", min_value=0)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.number_input("Chest Pain Type", min_value=0, max_value=3)
    trestbps = st.number_input("Resting Blood Pressure", min_value=0)
    chol = st.number_input("Cholesterol", min_value=0)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
    restecg = st.number_input("Resting Electrocardiographic Results", min_value=0, max_value=2)
    thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0)
    exang = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
    oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0)
    slope = st.number_input("Slope of the Peak Exercise ST Segment", min_value=0, max_value=2)
    ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy", min_value=0, max_value=4)
    thal = st.number_input("Thalassemia Type", min_value=0, max_value=3)
    
    if st.button("Predict Heart Disease"):
        result = heart_model.predict([[age, 1 if sex == "Male" else 0, cp, trestbps, chol, 1 if fbs == "Yes" else 0, restecg, thalach, 1 if exang == "Yes" else 0, oldpeak, slope, ca, thal]])
        st.write("Result:", "Positive" if result[0] == 1 else "Negative")

def predict_lung_disease():
    st.subheader("Lung Disease Diagnosis")
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=0)
    smoking = st.selectbox("Smoking", ["Yes", "No"])
    yellow_fingers = st.selectbox("Yellow Fingers", ["Yes", "No"])
    anxiety = st.selectbox("Anxiety", ["Yes", "No"])
    peer_pressure = st.selectbox("Peer Pressure", ["Yes", "No"])
    chronic_disease = st.selectbox("Chronic Disease", ["Yes", "No"])
    fatigue = st.selectbox("Fatigue", ["Yes", "No"])
    allergy = st.selectbox("Allergy", ["Yes", "No"])
    wheezing = st.selectbox("Wheezing", ["Yes", "No"])
    alcohol_consuming = st.selectbox("Alcohol Consuming", ["Yes", "No"])
    coughing = st.selectbox("Coughing", ["Yes", "No"])
    shortness_of_breath = st.selectbox("Shortness of Breath", ["Yes", "No"])
    swallowing_difficulty = st.selectbox("Swallowing Difficulty", ["Yes", "No"])
    chest_pain = st.selectbox("Chest Pain", ["Yes", "No"])
    
    if st.button("Predict Lung Disease"):
        result = lungs_model.predict([[1 if gender == "Male" else 0, age, 1 if smoking == "Yes" else 0, 1 if yellow_fingers == "Yes" else 0, 1 if anxiety == "Yes" else 0, 1 if peer_pressure == "Yes" else 0, 1 if chronic_disease == "Yes" else 0, 1 if fatigue == "Yes" else 0, 1 if allergy == "Yes" else 0, 1 if wheezing == "Yes" else 0, 1 if alcohol_consuming == "Yes" else 0, 1 if coughing == "Yes" else 0, 1 if shortness_of_breath == "Yes" else 0, 1 if swallowing_difficulty == "Yes" else 0, 1 if chest_pain == "Yes" else 0]])
        st.write("Result:", "Positive" if result[0] == 1 else "Negative")

def predict_parkinsons():
    st.subheader("Parkinson's Diagnosis")
    input_values = []
    for col in parkinson_data.columns[1:23]:  # Taking first 22 features for model compatibility
        value = st.number_input(f"{col.replace('_', ' ').title()}")
        input_values.append(value)
    
    if st.button("Predict Parkinson's"):
        result = parkinson_model.predict([input_values])
        st.write("Result:", "Positive" if result[0] == 0 else "Negative")

# Disease Diagnosis Routes
if option == "Diabetes":
    predict_diabetes()
elif option == "Heart Disease":
    predict_heart_disease()
elif option == "Lung Disease":
    predict_lung_disease()
elif option == "Parkinson's":
    predict_parkinsons()

