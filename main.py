from marvel import Marvel
# from keys import PUBLIC_KEY, PRIVATE_KEY 
from dotenv import load_dotenv
import os

# load the environment variables from .env
load_dotenv()

# Access the variables
PUBLIC_KEY = os.getenv('PUBLIC_KEY')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')


marvel = Marvel(PUBLIC_KEY= PUBLIC_KEY,
                PRIVATE_KEY= PRIVATE_KEY)

print(f"Pub Key: {PUBLIC_KEY}")