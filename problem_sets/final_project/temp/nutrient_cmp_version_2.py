import os, sys      # opening files, and exiting program
import requests     # sending api requests
from dotenv import load_dotenv  # load .env file
import matplotlib.pyplot as plt     # for plotting bar graphs
import numpy as np
import json # loading json file, which we create ourselves to store previously searched food names
import streamlit
import atexit   # to do fns when a user exits program

if False:
    """
    
    when submitting- The graders will primarily look at demo video. pytests should ignore using api keys


    Todo-
    1. Allow user to select nutrient to display thorugh UI
    2. Allow users to show bad nutrient graph as well.

    Additional display info:
    3. (follwed with 2nd feature) Do self chk on food, to see if it is relatively high on bad nutrients using a simple if else classification if the food is high in bad cholesterol, and sugar.
    4. Display nutrient density score with density = (sum(weighted_important_nutrients)) / calories

    Big updates
    5. Multi food cmp

    Extras:
    1. keep track and update all keys with new values of dict_memoization data if oldest data, older than 1 year.
        # dicts in py after 3.7 uses arrays to have spare hash tables, that preserve order of keys that is inserted.

    Done:

    1. 
    cleared: Already did memorization, turn it into a local database storage
    method: Store memoized data in dict format and store it to a json file when program terminates. Load the same file back on when programs execution starts, keeping data and appending over n number of program executions.
                Uses json module with json.dump(<dict>, <file_obj>) and <dict> = json.load(<file_obj>)

        Further details:
            # Using python to format to storing <dict> type hash (faster as build in), and storing as json (Reading- if able to load full file into python- o(n) speed to read inputs. Else- vary slow, fix- shelve)
            # Medium size (over 1 GB files) shelve- allows partial load of database, smaller file size as uses binary format to store. 
                # shelve uses random single-key reads/writes; shelve = best for many small persistent operations without loading all data.
            # High size (and majority of scenarios)- SQLite
                Even while reading/writing, uses B-Tree lookup. Bulk inserts & queries are available, with optimized features.
                Has smallest file size.

    2.
    Implemented UI on program, using input and submit button,
        atexit module to run save fn only after exit program is initiated.

    """


def request_food(SEARCH_URL, API_KEY, food_query, page_limit, dict_memoization):
    
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
    label_1 = first_food_obj['description']
    label_2 = second_food_obj['description']

    # 2. SETUP PLOT
    x = np.arange(len(nutrients))  # Label locations
    width = 0.35  # Width of the bars

    fig, ax = plt.subplots(figsize=(10, 8))

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

    
    # Add Text 1: Positioned below the axis, aligned left
    if False:
        """
        if 'ingredients' in first_food_obj:
            fig.text(
                0.05, 0.20, # x=5% from left, y=20% from bottom (in figure coordinates)
                f"{first_food_obj['description']}- ingredients: \n{first_food_obj['ingredients'][:150]}", 
                wrap=True, 
                fontsize=9, 
                color='#66b3ff', # Match bar color
                transform=fig.transFigure # Use figure coordinates for stability
            )
        
        if 'ingredients' in second_food_obj:
        # Add Text 2: Positioned slightly lower
            fig.text(
                0.05, 0.15, # x=5% from left, y=15% from bottom
                f"{second_food_obj['description']}- ingredients: \n{second_food_obj['ingredients'][:150]}", 
                wrap=True, 
                fontsize=9, 
                color='#ff9999', # Match bar color
                transform=fig.transFigure
            )
        """

    # Optional: Add the specific numbers on top of the bars for clarity
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    
    return fig

def load_stored_json(memoization_file_name):
    # feature 1
        # storing previously searched food data.
    if not os.path.exists(memoization_file_name):
        dict_memoization = {}
    else:
        with open(memoization_file_name, 'r') as file_obj:
            dict_memoization = json.load(file_obj)
    return dict_memoization

def save_json(memoization_file_name, dict_memoization):
    with open(memoization_file_name, 'w') as file_obj:
        json.dump(dict_memoization, file_obj)
    print("Saved file, holding results")


def main():

    # setting up cross session variables.
    if 'count' not in streamlit.session_state:
        streamlit.session_state.count = 0

    memoization_file_name = "dict_memoization.json"

    if 'loaded' not in streamlit.session_state:
        dict_memoization = load_stored_json(memoization_file_name)
        streamlit.session_state.loaded = 1
        streamlit.session_state.dict_mem = dict_memoization    
        # loading api key
        load_dotenv()
        API_KEY = os.getenv("USDA_API_KEY")
        if not API_KEY:
            sys.exit("API KEY empty")
        streamlit.session_state.api_key = API_KEY

    dict_memoization = streamlit.session_state.dict_mem

    SEARCH_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"


    # START OF PROGRAM

    streamlit.title("Food Nutrient Program")
    
    # INPUT
    with streamlit.form(key = "Form_1"):
        
        input_box_1, input_box_2 = streamlit.columns(2)
        # 1st food item
        input_box_1 = streamlit.text_input("\nEnter first food to compare: ").lower()
        # 2nd food item
        input_box_2 = streamlit.text_input("Enter second food to compare: ").lower()

    # BUTTON, send api request
        button_1 = streamlit.form_submit_button("Submit")

        if button_1:
            with streamlit.spinner(f"\nSearching for food: {input_box_1}..."):
                foods = request_food(SEARCH_URL, streamlit.session_state.api_key, input_box_1, 25, dict_memoization)
                first_food = foods[0]
            streamlit.success(f"Found- {first_food["description"]}")
            #obtain relevant nutrients of first food
            first_data = get_nutrients_food(first_food)

            with streamlit.spinner(f"Searching for food: {input_box_2}..."):
                foods = request_food(SEARCH_URL, streamlit.session_state.api_key, input_box_2, 25, dict_memoization)  
                second_food = foods[0]
            streamlit.success(f"Found: {second_food["description"]}")
            #obtain relevant nutrients of second food
            second_data = get_nutrients_food(second_food)
        
            nutrients = ['Kcal', 'Protein', 'Fat', 'Carbs']
        
            # PLOT a bar graph of the 2 foods

            streamlit.title(f"\nBar graph of nutrients")
            streamlit.pyplot(graph_food(first_food, second_food, first_data, second_data, nutrients))

            if 'ingredients' in first_food:
                streamlit.write(f"{first_food["description"]} ingredients: ")
                streamlit.write(f"{first_food["ingredients"]}")
            if 'ingredients' in second_food:
                streamlit.write(f"{second_food["description"]} ingredients: ")
                streamlit.write(f"{second_food["ingredients"]}")

            streamlit.session_state.count += 1  # keeps track of number of times program was executed
            streamlit.write(f"\n\nExecuted program {streamlit.session_state.count} times in this session!")
    
    # Below code makes fn 'save_json' run only when terminating
    # every time atexit.register(fn_name) is called, sends the fn to a queue, which runs at program termination
        # Below makes it call atexit.register only once
    if "terminated" not in streamlit.session_state:
        atexit.register(save_json, memoization_file_name, dict_memoization)
        streamlit.session_state.terminated = True

if __name__ == "__main__":
    main()

if False:
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