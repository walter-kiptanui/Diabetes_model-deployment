# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 11:34:17 2023

@author: kiptanui
"""

import json
import requests

url = ''
input_data_for_model = {
    'Pregnancies' : 6,
    'Glucose' : 148,
    'BloodPressure' : 72,
    'SkinThickness' : 35,
    'Insulin' : 0,
    'BMI' : 33.6,
    'diabetesPedigreeFunction' : 0.627,
    'Age' : 50
    }

#Now the above code is in the form of a dictionary, so we convert it to json

input_json = json.dumps(input_data_for_model)
response = requests.post(url, data = input_json)
print(response.txt)