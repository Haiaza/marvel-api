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
HASH = hashlib.md5(f'{TS}{PRIVATE_KEY}{PUBLIC_KEY}') # encrypt the hash

marvel = Marvel(PUBLIC_KEY= PUBLIC_KEY,
                PRIVATE_KEY= PRIVATE_KEY)

# example of an authenticated url request 
# http://gateway.marvel.com/v1/public/comics?ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150



# TESTING GRAVEYARD

# print(f"Pub Key: {PUBLIC_KEY}")

# characters = marvel.characters
# all_characters = marvel.characters.all()
# print(all_characters)

# comics = marvel.comics
# all_comics = comics.all()
# print(all_comics)