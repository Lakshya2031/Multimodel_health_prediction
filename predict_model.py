# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 17:02:20 2025

@author: HP
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model=pickle.load(open("diabetes_model.sav",'rb'))
heart_disease_model=pickle.load(open("heart_disease_model.sav",'rb'))
parkinson_disease_model=pickle.load(open("parkinsons_model.sav",'rb'))

# sidebar
with st.sidebar:
    selected=option_menu('Multiple Disease System',['Diabetes_prediction','Heart_disease_Prediction','Parkinson_Prediction'],icons=['bandaid-fill','bandaid-fill','bandaid-fill'],default_index=0)
    
    


if (selected=='Diabetes_prediction'):
    st.title("Diabetes_prediction")
    
    Pregnancies=st.number_input("Pregnancie")
    Glucose=st.number_input("Glucose")
    BloodPressure=st.number_input("BloodPressure")
    SkinThickness=st.number_input("SkinThickness")
    Insulin=st.number_input("Insulin")
    BMI=st.number_input("BMI")
    DiabetesPedigreeFunction=st.number_input("DiabetesPedigreeFunction")
    Age=st.number_input("Age")
    
    diab_diagnosis=''
    if st.button('Diabetes_test_result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        
        if diab_prediction[0]==0:
            diab_diagnosis='No Diabetes'
            
        else:
            diab_diagnosis='Diabetes'
            
    st.success(diab_diagnosis)
    

if (selected=='Heart_disease_Prediction'):
    st.title("Heart Disease Prediction")
    
    
    col1,col2,col3=st.columns(3)
    with col1:
        age=st.number_input("age")
        
    with col2:
        sex=st.number_input("sex->1.Male 0->Female")
        
    with col3:
        cp=st.number_input("cp")
        
        
    with col1:
        trestbps=st.number_input("trestbps")
        
    with col2:
        chol=st.number_input("chol")
        
    with col3:
        fbs=st.number_input("fbs")
        
        
    with col1:
        restecg=st.number_input("restecg")
        
    with col2:
        exang=st.number_input("exang")
        
    with col3:
        oldpeak=st.number_input("oldpeak")
        
    
    with col1:
        slope=st.number_input("slope")
        
    with col2:
        ca=st.number_input("ca")
        
    with col3:
        thal=st.number_input("thal")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    hd_diagnosis=''
    if st.button('HD_test'):
        hd_prediction=heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if hd_prediction==0:
            hd_diagnosis="No hd"
            
        else:
            hd_diagnosis='Hd'
        
    st.success(hd_diagnosis)
    
    
    
    
if (selected=='Parkinson_Prediction'):
   st.title("Parkinson Prediction")
    
    
    
   FoHz=st.number_input("MDVP:Fo(Hz)")
   MDVPFhiHz=st.number_input(" MDVP:Fhi(Hz)")
   MDVPFloHz=st.number_input("MDVP:Flo(Hz)")
   MDVPJitter=st.number_input("MDVP:Jitter(%)")
   MDVPJitterAbs=st.number_input("MDVP:Jitter(Abs)")
   MDVPRAP=st.number_input("MDVP:RAP")
   MDVPPPQ=st.number_input("MDVP:PPQ")
   JitterDDP=st.number_input("Jitter:DDP")
   MDVPShimmer=st.number_input("MDVP:Shimmer")
   MDVPShimmerdB=st.number_input("MDVP:Shimmer(dB)")
   ShimmerAPQ3=st.number_input("Shimmer:APQ3")
   ShimmerAPQ5=st.number_input("Shimmer:APQ5")
   MDVPAPQ=st.number_input("MDVP:APQ")
   ShimmerDDA=st.number_input("Shimmer:DDA")
   NHR=st.number_input("NHR")
   HNR=st.number_input("HNR")
   RPDE=st.number_input("RPDE")
   DFA=st.number_input("DFA")
   spread1=st.number_input("spread1")
   spread2=st.number_input("spread2")
   D2=st.number_input("D2")
   PPE=st.number_input("PPE")
   
   parkinson_diagnosis=''
   if (st.button("Parkison_Test")):
       p_Prediction=parkinson_disease_model.predict([[FoHz,MDVPFhiHz,MDVPFloHz,MDVPJitter,MDVPJitterAbs,MDVPRAP,MDVPPPQ,JitterDDP,MDVPShimmer,MDVPShimmerdB,ShimmerAPQ3,ShimmerAPQ5,MDVPAPQ,ShimmerDDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
       if (p_Prediction==0):
           parkinson_diagnosis='No'
       else:
           parkinson_diagnosis='Yes'
   st.success(parkinson_diagnosis)
    