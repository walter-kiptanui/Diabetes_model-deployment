# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 23:12:19 2023

@author: kiptanui
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int
    
#Loading the saved model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb')) 

#Creating the API
@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters : model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    preg = input_dictionary['Pregnancies'] 
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThickness']
    ins = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']
    
    #Now we pass these values to our model for prediction
    #the final data that we will be passing to our model

    input_list = [preg, glu, bp, skin, ins, bmi, dpf, age]

    #Now we can pass this list to our model and make the prediction

    prediction = diabetes_model.predict([input_list])

    if prediction[0] == 0:
        return 'The person is not Diabetic'
    else:
        return 'The person is Diabetic'
    