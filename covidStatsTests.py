# Import libraries
import requests

import json

# Initialize variables
def jprint(obj):

    text = json.dumps(obj, sort_keys=True, indent=4)
    
    return text

def jload(obj):

    loaded_json = json.loads(formatted_json)

    return loaded_json
    
# A function that returns the JSON request respond
def get_covid_json():

    response = requests.get("https://covid-19-greece.herokuapp.com//total-tests")

    if (response.status_code == 200):

        return response.json()

    else :

        print ("Unsuccessful Request with error code :",response.status_code)

        return None

# Initialize variables

datesArray = []

testCases = []

# Request JSON object and turn it into a Python dictionary
covid_json = get_covid_json()

formatted_json = jprint(covid_json)

loaded_json = jload(covid_json)

# Iterate through dictionary and perform actions on the last day's data
for key in loaded_json['total_tests']:
    
    testCases.append(key['tests'])

    datesArray.append(key['date'])

print ("Total Test COVID-19 cases in Greece:",testCases[-1],",last updated on:",datesArray[-1])
