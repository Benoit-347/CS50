import os, sys
import requests
from dotenv import load_dotenv  # load .env file
import matplotlib.pyplot as plt
import numpy as np



def request_food(SEARCH_URL, API_KEY, food_query, page_limit):
    
    # check memoized data first
    if food_query in dict_memoization:
        return dict_memoization[food_query]
    
    # get (url, parameters);     parameters  = "api_key", "query" (food name), "pageSize" (max results count)
    search_result = requests.get(SEARCH_URL, params= {"api_key": API_KEY, "query": food_query, "pageSize": page_limit}, timeout=10)
    search_result.raise_for_status()        # raise exception if failed web request.

    result = search_result.json().get("foods", [])     # convert result obj into json dict, use dict get method to obtain value in "foods" key (default []).
    
    if bool(result) == False:
        print(f"Empty search for name {food_query}")
        sys.exit(1)
    
    # add to memoized data
    dict_memoization[food_query] = result

    return result

def get_nutrient(food, name):
    # this fn runs on the node to response object from request. Searching for matching nutrient name from value to nutrientName key, from node to foodNutrients value, which is from dict food.  
         # ideal workflow- "foods = [ dict_food, dict_food_2..]; dict_food = {"foodNutrients": [ {"nutrientName": <name_1>, "value": <val_1>}, {"nutrientName": <name_2>, "value": <val_2>} ] }
    for nutrient in food["foodNutrients"]:
        if nutrient["nutrientName"] == name:
            return nutrient["value"]

def get_nutrients_food(food):
    if not food:
        print("No match to food query")

    kcal = get_nutrient(food, "Energy")     #  # ideal workflow- "foods = [ dict_food, dict_food_2..]; dict_food = {"foodNutrients": [ {"nutrientName": <name_1>, "value": <val_1>}, {"nutrientName": <name_2>, "value": <val_2>} ] }
    prot = get_nutrient(food, "Protein")
    fat  = get_nutrient(food, "Total lipid (fat)")
    carb = get_nutrient(food, "Carbohydrate, by difference")

    return kcal, prot, fat, carb

def graph_food(first_food_obj, second_food_obj, first_food_data, second_food_data, nutrients):

    # 1. setup label
    label_1 = first_food_obj["description"]
    label_2 = second_food_obj["description"]

    # 2. SETUP PLOT
    x = np.arange(len(nutrients))  # Label locations
    width = 0.35  # Width of the bars

    fig, ax = plt.subplots(figsize=(10, 6))

    # 3. PLOT BARS
    # We shift the position of the bars by +/- width/2 so they sit side-by-side
    rects1 = ax.bar(x - width/2, first_food_data, width, label= label_1, color='#66b3ff')
    rects2 = ax.bar(x + width/2, second_food_data, width, label= label_2, color='#ff9999')

    # 4. STYLING & LABELS
    ax.set_ylabel('Nutrient Density (grams per 100g)')
    ax.set_title('Nutrient Density Comparison')
    ax.set_xticks(x)
    ax.set_xticklabels(nutrients)
    ax.legend()

    # Optional: Add the specific numbers on top of the bars for clarity
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    plt.tight_layout()
    plt.show(block= False)

def main():

    global dict_memoization
    dict_memoization = {}
    user_command = 1
    while (user_command != '0'):
        # laoding api key
        load_dotenv()
        API_KEY = os.getenv("USDA_API_KEY")
        if not API_KEY:
            sys.exit("API KEY empty")

        SEARCH_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"

        # Comparing food items

        # 1st food item
        food_name_1 = input("\nEnter first food to compare: ") 
        # 2nd food item
        food_name_2 = input("Enter second food to compare: ") 

        print(f"\nSearching for food: {food_name_1}...")
        foods = request_food(SEARCH_URL, API_KEY, food_name_1, 25)
        first_food = foods[0]
        print(f"Found- {first_food["description"]}")
        #obtain relevant nutrients of first food
        first_data = get_nutrients_food(first_food)

        print(f"Searching for food: {food_name_2}...")
        foods = request_food(SEARCH_URL, API_KEY, food_name_2, 25)  
        second_food = foods[0]
        print(f"Found: {second_food["description"]}")
        #obtain relevant nutrients of second food
        second_data = get_nutrients_food(second_food)
        
        nutrients = ['Kcal', 'Protein', 'Fat', 'Carbs']

        # plotting a bar graph of the 2 foods
        print(f"\nPlotting bar graph on comparison...")
        graph_food(first_food, second_food, first_data, second_data, nutrients)
        user_command = input("\nContinue food comparision (1/0)? ")

    print("\nExited program sucessfully!\n")

if __name__ == "__main__":
    main()

"""
NUTRIENTS AVAILABLE:
    Protein
    Total lipid (fat)
    Carbohydrate, by difference
    Energy
    Total Sugars
    Fiber, total dietary
    Calcium, Ca
    Iron, Fe
    Sodium, Na
    Vitamin A, IU
    Vitamin C, total ascorbic acid
    Cholesterol
    Fatty acids, total trans
    Fatty acids, total saturated
"""