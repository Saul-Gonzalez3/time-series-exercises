#Import

import requests
import math
import pandas as pd

----------------------------------------------------

def acquire_people_df():
    response = requests.get('https://swapi.dev/api/people')
    data = response.json()
    df = pd.DataFrame(data['results'])
    
    
    count = 8

    while True:
        if count > 0:
            response = requests.get(data['next'])
            data = response.json()
            number_of_people = data['count']
            next_page = data['next']
            previous_page = data['previous']
            number_of_results = len(data['results'])
            max_page = math.ceil(number_of_people / number_of_results)
            print(f'number_of_people: {number_of_people}')
            print(f'next_page: {next_page}')
            print(f'previous_page: {previous_page}')
            print(f'number_of_results: {number_of_results}')
            print(f'max_page: {max_page}')
            df = pd.concat([df, pd.DataFrame(data['results'])])
            count -= 1
        else:
            break
    return df
----------------------------------------------------
def acquire_planets_df():
    response2 = requests.get('https://swapi.dev/api/planets')
    data2 = response2.json()
    df2 = pd.DataFrame(data2['results'])
    
    
    count = 5

    while True:
        if count > 0:
            response2 = requests.get(data2['next'])
            data2 = response2.json()
            number_of_people = data2['count']
            next_page = data2['next']
            previous_page = data2['previous']
            number_of_results = len(data2['results'])
            max_page = math.ceil(number_of_people / number_of_results)
            print(f'number_of_people: {number_of_people}')
            print(f'next_page: {next_page}')
            print(f'previous_page: {previous_page}')
            print(f'number_of_results: {number_of_results}')
            print(f'max_page: {max_page}')
            df2 = pd.concat([df2, pd.DataFrame(data2['results'])])
            count -= 1
        else:
            break
        
    return df2

----------------------------------------------------
def acquire_starships_df():
    response3 = requests.get('https://swapi.dev/api/starships/')
    data3 = response3.json()
    df3 = pd.DataFrame(data3['results'])
    count = 3

    while True:
        if count > 0:
            response3 = requests.get(data3['next'])
            data3 = response3.json()
            number_of_people = data3['count']
            next_page = data3['next']
            previous_page = data3['previous']
            number_of_results = len(data3['results'])
            max_page = math.ceil(number_of_people / number_of_results)
            print(f'number_of_people: {number_of_people}')
            print(f'next_page: {next_page}')
            print(f'previous_page: {previous_page}')
            print(f'number_of_results: {number_of_results}')
            print(f'max_page: {max_page}')
            df3 = pd.concat([df3, pd.DataFrame(data3['results'])])
            count -= 1
        else:
            break
    return df3

----------------------------------------------------


----------------------------------------------------