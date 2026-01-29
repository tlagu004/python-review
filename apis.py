import requests
from dotenv import load_dotenv
import os
import streamlit

load_dotenv()

url="https://api.nasa.gov/planetary/apod?api_key="

def apod_generator(url, unique_key):
    final_url = url + unique_key
    unique_key = os.getenv("NASA_API_KEY")
    response = requests.get(final_url).json()
    return response

# print(response["title"])
# print(response["hdurl"])
# print(response["date"])
# print(response["explanation"])
