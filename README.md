# Diabetes_model-deployment
In this repository I am deploying a machine learning model called diabetes_model using fastapi framework.
I am deploying the ML model in the form of an API and integrating the API with a UI system.
I first saved my model as diabetes_model.sav. The saved model would be deployed as API.

I created a file on spyder in order to create the API and saved it in the same folder where my saved model was.
I installed the necessary libraries for API creation. The libraries were fastapi, uvicorn, pydantic, json, pickle and requests.

After generating the code for the API I used the post method to give some values to our API, these are values of the features of my dataset.
These values were then passed to my model for prediction.
