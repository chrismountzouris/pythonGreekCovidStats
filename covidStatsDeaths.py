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

    response = requests.get("https://covid-19-greece.herokuapp.com/deaths")

    if (response.status_code == 200):

        return response.json()

    else :

        print ("Unsuccessful Request with error code :",response.status_code)

        return None

# Initialize variables

datesArray = []

deathCases = []

# Request JSON object and turn it into a Python dictionary
covid_json = get_covid_json()

formatted_json = jprint(covid_json)

loaded_json = jload(covid_json)

# Iterate through dictionary and perform actions on the last day's data
for key in loaded_json['cases']:
    
    deathCases.append(key['deaths'])

    datesArray.append(key['date'])

print ("Total confirmed COVID-19 death cases in Greece:",deathCases[-1],",last updated on:",datesArray[-1])
