import os, sys
import requests
from dotenv import load_dotenv  # load .env file

# laoding api key
load_dotenv()
API_KEY = os.getenv("USDA_API_KEY")
if not API_KEY:
    sys.exit("API KEY empty")

SEARCH_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"

def request_food(food_query, page_limit):
    # get (url, parameters);     parameters  = "api_key", "query" (food name), "pageSize" (max results count)
    search_result = requests.get(SEARCH_URL, params= {"api_key": API_KEY, "query": food_query, "pageSize": page_limit}, timeout=10)
    search_result.raise_for_status()        # raise exception if failed web request.

    return search_result.json().get("foods", [])     # convert result obj into json dict, use dict get method to obtain value in "foods" key (default []).

def get_nutrient(food, name):
    # this fn runs on the node to response object from request. Searching for matching nutrient name from value to nutrientName key, from node to foodNutrients value, which is from dict food.  
    for nutrient in food["foodNutrients"]:
        if nutrient["nutrientName"] == name:
            return nutrient["value"]

def get_all_details_food(food_name):
    foods = request_food(food_name, 25)     # ideal workflow- "foods = [ dict_food, dict_food_2..]; dict_food = {"foodNutrients": [{"nutrientName": name}, {"nutrientName": name_2}]}"
    if not foods:
        print("No match to food query")

    for food in foods:
        kcal = get_nutrient(food, "Energy")
        prot = get_nutrient(food, "Protein")
        fat  = get_nutrient(food, "Total lipid (fat)")
        carb = get_nutrient(food, "Carbohydrate, by difference")

        print(f"Food name: {food["description"]}")
        print(f"Calories: {kcal}\nProtein: {prot}\nFat: {fat}\nCarbohydrates: {carb}")

food_name = "apple"
get_all_details_food(food_name)