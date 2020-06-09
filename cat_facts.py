import requests

url = "https://cat-fact.herokuapp.com/facts/random/"
#sends request for a catfact, receives a response
def reqFact():
    fact = requests.request("GET", url)
    fact_data = data.json()
    return data[0].text
    
