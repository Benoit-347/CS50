
import os, sys
import requests
from dotenv import load_dotenv  # load .env file
import matplotlib.pyplot as plt
import numpy as np
import project

load_dotenv()
API_KEY = os.getenv("USDA_API_KEY")
if not API_KEY:
    sys.exit("API KEY empty")

SEARCH_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"
food_name = "apple"

def test_request_food():
    foods = project.request_food(SEARCH_URL, API_KEY, food_name, 25)
    assert len(foods) > 0

food_obj = project.request_food(SEARCH_URL, API_KEY, food_name, 25)
food_obj_1 = food_obj[0]

def test_get_nutrient():
    assert project.get_nutrient(food_obj_1, "Energy") != None

def test_get_nutrients_food():
    list_data = project.get_nutrients_food(food_obj_1)
    assert list_data[0] != None
    assert list_data[1] != None
    assert list_data[2] != None
    assert list_data[3] != None