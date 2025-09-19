import streamlit as st
import pandas as pd

model = pd.read_pickle("modelo_sleep.pkl")

st.markdown("# Descubra se você tem problemas de sono")


col1, col2 = st.columns(2)

with col1:
    gender_opt = ['Male', 'Female']
    gender = st.selectbox("Qual o seu gênero? ",options=gender_opt)

    age = st.number_input("Qual sua idade? ",0,100)

    occupation_opt = ['Software Engineer', 'Doctor', 'Sales Representative', 'Teacher',
        'Nurse', 'Engineer', 'Accountant', 'Scientist', 'Lawyer',
        'Salesperson', 'Manager']

    occupation = st.selectbox("Qual a sua ocupação? ",options=occupation_opt)

    sleep_dur = st.number_input("Quantas horas em média você dorme? ",min_value=0.0,
                                                                    max_value=24.0,
                                                                    value=5.0,
                                                                    step=0.1)
    quality_sleep = st.number_input("Qual a qualidade do seu sono? (Avalie de 0 à 10) ",0,10)

with col2:

    physical_act = st.number_input("Qual o seu nível de atividade física? (avalie de 0 à 100) ", 0,100)

    stress = st.number_input("Qual seu nível de estresse? (Avalie de 0 à 10) ",0,10)

    bmi_opt = ['Overweight', 'Healthy Weight', 'Obese']

    bim = st.selectbox("Qual o seu IMC? ", options=bmi_opt)
    
    pressao = st.text_input("Digite sua pressão arterial (ex: 140/90):")

    heart_rate = st.number_input("Heart Rate (bpm)", 
                                min_value=30, 
                                max_value=220, 
                                step=1)
daily_steps = st.number_input("Quantidade de passos diários? ", 
                                    min_value=0, 
                                    max_value=50000, 
                                    step=100
                                )

systolic, diastolic = None, None  

if pressao and '/' in pressao:
    try:
        systolic, diastolic = pressao.split('/')
        systolic = int(systolic.strip())
        diastolic = int(diastolic.strip())
    except ValueError:
        st.error("Por favor, digite no formato correto (ex: 120/80).")