# riot api calls
# looking to get more recent data from the riot api
# and store it in a local database for analysis

# work in progress

import os
import sys
import json
import requests
import time
import sqlite3
import pandas as pd
from dotenv import load_dotenv
from util import db

# Load environment variables from .env file
load_dotenv()
RIOT_API_KEY = os.getenv('RIOT_API_KEY')
RIOT_API_URL = os.getenv('RIOT_API_URL')
RIOT_API_REGION = os.getenv('RIOT_API_REGION')
RIOT_API_VERSION = os.getenv('RIOT_API_VERSION')
RIOT_API_PLATFORM = os.getenv('RIOT_API_PLATFORM')

# Check if the API key is set
if not RIOT_API_KEY:
    print("Error: RIOT_API_KEY is not set in the .env file.")
    sys.exit(1)

# Function to get the summoner ID from the summoner name
def get_summoner_id(summoner_name):
    url = f"{RIOT_API_URL}/lol/summoner/v{RIOT_API_VERSION}/summoners/by-name/{summoner_name}"
    headers = {
        "X-Riot-Token": RIOT_API_KEY
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['id']
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Function to get the match history for a summoner ID
