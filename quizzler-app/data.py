import requests
import random

"""
To do
Modify the data.py file (dont change the main.py)
Make a get() request to fetch 10 True or False questions.
Parse the JSON response and replace the value of question_data
(don't change the variable name)
Hint: create a python dictionary for the amount and type parameter
"""

parameters = {"amount": 10, "type": "boolean"}

data = requests.get(
    "https://opentdb.com/api.php?amount=10&type=boolean", params=parameters
)

question_data = data.json()["results"]
