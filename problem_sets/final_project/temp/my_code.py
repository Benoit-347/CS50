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
         # ideal workflow- "foods = [ dict_food, dict_food_2..]; dict_food = {"foodNutrients": [ {"nutrientName": <name_1>, "value": <val_1>}, {"nutrientName": <name_2>, "value": <val_2>} ] }
    for nutrient in food["foodNutrients"]:
        if nutrient["nutrientName"] == name:
            return nutrient["value"]
        
def get_nutrient_new(food, name):
    # this fn runs on the node to response object from request. Searching for matching nutrient name from value to nutrientName key, from node to foodNutrients value, which is from dict food.  
         # ideal workflow- "foods = [ dict_food, dict_food_2..]; dict_food = {"foodNutrients": [ {"nutrientName": <name_1>, "value": <val_1>}, {"nutrientName": <name_2>, "value": <val_2>} ] }
    for nutrient in food["foodNutrients"]:
        if nutrient["nutrientName"] == name:
            return nutrient["value"], nutrient['unitName']
        
def get_all_details_food(foods, food_name):
    if not foods:
        print("No match to food query")

    for food in foods:
        kcal = get_nutrient(food, "Energy")     #  # ideal workflow- "foods = [ dict_food, dict_food_2..]; dict_food = {"foodNutrients": [ {"nutrientName": <name_1>, "value": <val_1>}, {"nutrientName": <name_2>, "value": <val_2>} ] }
        prot = get_nutrient(food, "Protein")
        fat  = get_nutrient(food, "Total lipid (fat)")
        carb = get_nutrient(food, "Carbohydrate, by difference")

        print(f"Food name: {food["description"]}")
        print(f"Calories: {kcal}\nProtein: {prot}\nFat: {fat}\nCarbohydrates: {carb}")

        return kcal, prot, fat, carb

"""

food_name = "chicken" # Apple, baked; Apple, dried; Apple, raw

foods = request_food(food_name, 25)     # ideal workflow- "foods = [ dict_food, dict_food_2..]; dict_food = {"foodNutrients": { <nutrient>: {"nutrientName": name}, {"nutrientName": name_2}]}"
# foods = [{food_1: {""}}]
for food in foods:
    print(f"Food name: {food["description"]}")  
    kcal = get_nutrient(food, "Energy")
    prot = get_nutrient(food, "Protein")
    fat  = get_nutrient(food, "Total lipid (fat)")
    carb = get_nutrient(food, "Carbohydrate, by difference")
    print(f"Nutrients: kcal: {kcal}, prot: {prot}, fat: {fat}, carb: {carb}")
# get_all_details_food(foods, food_name)
"""

# TRIAL program
    
food_name = "idly" # Apple, baked; Apple, dried; Apple, raw

foods = request_food(food_name, 25)    

first_food = foods[0]
kcal_1 = get_nutrient(first_food, "Energy")
prot_1 = get_nutrient(first_food, "Protein")
fat_1  = get_nutrient(first_food, "Total lipid (fat)")
carb_1 = get_nutrient(first_food, "Carbohydrate, by difference")
'unitName'

kcal_2, unit_kcal = get_nutrient_new(first_food, "Energy")
print(unit_kcal)
prot_1, unit_kcal = get_nutrient_new(first_food, "Protein")
print(unit_kcal)

food_name = "mutton"

foods = request_food(food_name, 25)    

second_food = foods[0]
kcal_2 = get_nutrient(second_food, "Energy")
prot_2 = get_nutrient(second_food, "Protein")
fat_2  = get_nutrient(second_food, "Total lipid (fat)")
carb_2 = get_nutrient(second_food, "Carbohydrate, by difference")

if 'ingredients' in first_food:
    print(first_food['ingredients'])
    
"""
import matplotlib.pyplot as plt
import numpy as np

# 1. DATA PREP: Ensure values are normalized (e.g., "per 100g")
# This addresses your "nutrient per gram" requirement.
foods = [first_food["description"], second_food["description"]]
nutrients = ['Kcal', 'Protein', 'Fat', 'Carbs']

# Values in grams per 100g of food
first_data = [kcal_1, prot_1, fat_1, carb_1]   # High protein, low fat/carb
second_data  = [kcal_2, prot_2, fat_2, carb_2]   # High fat, moderate protein/carb

# 2. SETUP PLOT
x = np.arange(len(nutrients))  # Label locations
width = 0.35  # Width of the bars

fig, ax = plt.subplots(figsize=(10, 6))

# 3. PLOT BARS
# We shift the position of the bars by +/- width/2 so they sit side-by-side
rects1 = ax.bar(x - width/2, first_data, width, label=first_food["description"], color='#66b3ff')
rects2 = ax.bar(x + width/2, second_data, width, label=second_food["description"], color='#ff9999')

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
plt.show()

"""
"""
Tags available:
1. food.foodcategory.description- snacks, baked, vegetables
2. food.brandedfoodcategory- yogurt, ice cream
3. The brand food.brandOwner- dairy_milk

['fdcId', 'description', 'dataType', 'gtinUpc', 'publishedDate', 'brandOwner', 'ingredients', 'marketCountry', 'foodCategory', 'modifiedDate', 'dataSource', 'servingSizeUnit', 'servingSize', 'householdServingFullText', 'tradeChannels', 'allHighlightFields', 'score', 'microbes', 'foodNutrients', 'finalFoodInputFoods', 'foodMeasures', 'foodAttributes', 'foodAttributeTypes', 'foodVersionIds']

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