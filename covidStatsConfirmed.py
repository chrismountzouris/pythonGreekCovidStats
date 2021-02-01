# Import libraries
import requests

import json

import matplotlib.pyplot as plt

import re

# Initialize variables
def jprint(obj):

    text = json.dumps(obj, sort_keys=True, indent=4)
    
    return text

def jload(obj):

    loaded_json = json.loads(formatted_json)

    return loaded_json
    
# A function that returns the JSON request respond
def get_covid_json():

    response = requests.get("https://covid-19-greece.herokuapp.com/confirmed")

    if (response.status_code == 200):

        return response.json()

    else :

        print ("Unsuccessful Request with error code :",response.status_code)

        return None

def reduceDates(datesArray):

    reducedDatesArray = []

    for singleDay in datesArray:

        match = re.findall(r"[\d]{4}-[\d]{1,2}-01", singleDay)

        if (match):

            reducedDatesArray.append(match[0])

        else:

            reducedDatesArray.append('x')

    return reducedDatesArray

def create_covid_plot(datesArray, confirmedCases):

    plt.rcParams.update({'font.size': 8})

    plt.figure(figsize=(7,7))

    plt.plot(datesArray, confirmedCases)

    plt.title('COVID-19 Total Cases | Greece')

    plt.xlabel('Date')

    plt.xticks(rotation=90)

    plt.ylabel('Total cases')

    plt.show()

    return None

# Initialize variables

datesArray = []

confirmedCases = []

# Request JSON object and turn it into a Python dictionary
covid_json = get_covid_json()

formatted_json = jprint(covid_json)

loaded_json = jload(covid_json)

# Iterate through dictionary and perform actions on the last day's data
for key in loaded_json['cases']:
    
    confirmedCases.append(key['confirmed'])

    datesArray.append(key['date'])

print ("Total confirmed COVID-19 cases in Greece:",confirmedCases[-1],",last updated on:",datesArray[-1])

reducedDateArray = reduceDates(datesArray)

create_covid_plot(datesArray, confirmedCases)
