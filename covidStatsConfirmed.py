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
def get_vacs_json():

    response = requests.get("https://covid-19-greece.herokuapp.com/confirmed")

    if (response.status_code == 200):

        return response.json()

    else :

        print ("Unsuccessful Request with error code :",response.status_code)

        return None

# Initialize variables

datesArray = []

confirmedCases = []

# Request JSON object and turn it into a Python dictionary
vacs_json = get_vacs_json()

formatted_json = jprint(vacs_json)

loaded_json = jload(vacs_json)

# Iterate through dictionary and perform actions on the last day's data
for key in loaded_json['cases']:
    
    confirmedCases.append(key['confirmed'])

    datesArray.append(key['date'])

print ("Total confirmed COVID-19 cases in Greece:",confirmedCases[-1],",last updated on:",datesArray[-1])
