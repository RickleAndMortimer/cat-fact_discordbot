import requests
import random
import json
url = "https://cat-fact.herokuapp.com/facts/random"
requestNo = 50
random.seed()
#sends request for a catfact, receives a response
def requestFacts():
    facts = requests.get(url, data = {'amount': requestNo, 'animal_type': 'cat'})
    return json.loads(facts.text)
def pickFact(data):
    rand = random.randint(0, requestNo-1)
    return data[rand]['text']
