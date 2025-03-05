from marvel import Marvel
# from keys import PUBLIC_KEY, PRIVATE_KEY 
from dotenv import load_dotenv
import os
import requests
import hashlib
import time

# load the environment variables from .env
load_dotenv()

# Access the variables
TS  = time.time()
PUBLIC_KEY = os.getenv('PUBLIC_KEY')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
HASH = hashlib.md5(f'{TS}{PRIVATE_KEY}{PUBLIC_KEY}'.encode()).hexdigest() # encrypt the hash


# example of an authenticated url request 
# http://gateway.marvel.com/v1/public/comics?ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150

# construct a url
base_url = 'https://gateway.marvel.com/v1/public/comics'
# add params
params = {
    'titleStartsWith' : 'Avengers',
    'startYear' : 2012,
    'limit' : 50,
    'apikey' : HASH,
    'ts' : TS,
}

response = requests.get(base_url, params=params)
data = response.json()

print (data)


# TESTING GRAVEYARD

# for comic in data["data"]["results"]: 
#     print(comic["title"])

