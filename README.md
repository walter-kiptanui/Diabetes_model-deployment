# Diabetes_model-deployment
In this repository I am deploying a machine learning model called diabetes_model using fastapi framework.
I am deploying the ML model in the form of an API and integrating the API with a UI system.
I first saved my model and then deployed it as an API.

I created a file on spyder in order to create the API and saved it in the same fol
der where my saved model was.
I installed the necessary libraries for API creation. The libraries are fastapi, uvicorn, pydantic, json, pickle and requests.

After generating the code for the API I used the post method to give some values to our API, these are values of the features of my dataset.
These values were then passed to my model for prediction.

After creating the API, I made a test to ascertain if it was working. I created a new file in spyder for testing.

In this test file I imported the json and requests files. The requests library is used to post values to my API.
the json library is used to convert the dictionary file that I would create to a json format.
I then created a dictionary to input values to my features or keys.The dictionary is then posted to the url after conversion.

The final response is then given.
