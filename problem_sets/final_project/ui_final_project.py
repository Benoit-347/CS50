import os, sys
import requests
from dotenv import load_dotenv  # load .env file
import matplotlib.pyplot as plt
import numpy as np
import streamlit

"""
Todo-
1. Allow user to select nutrient to display thorugh UI

Additional display info:
3. Set a simple if else classification if the food is high in bad cholesterol, and sugar.
4. Display nutrient density score with density = (sum(weighted_important_nutrients)) / calories

Big updates
5. Multi food cmp

Extras:
1. keep track and update all keys with new values of dict_memoization data if oldest data, older than 1 year.
    # dicts in py after 3.7 uses arrays to have spare hash tables, that preserve order of keys that is inserted.

Done:

cleared: 2. Already did memorization, turn it into a local database storage
method: Store memoized data in dict format and store it to a json file when program terminates. Load the same file back on when programs execution starts, keeping data and appending over n number of program executions.
            Uses json module with json.dump(<dict>, <file_obj>) and <dict> = json.load(<file_obj>)

Further details:
    # Using python to format to storing <dict> type hash (faster as build in), and storing as json (Reading- if able to load full file into python- o(n) speed to read inputs. Else- vary slow, fix- shelve)
    # Medium size (over 1 GB files) shelve- allows partial load of database, smaller file size as uses binary format to store. 
        # shelve uses random single-key reads/writes; shelve = best for many small persistent operations without loading all data.
    # High size (and majority of scenarios)- SQLite
        Even while reading/writing, uses B-Tree lookup. Bulk inserts & queries are available, with optimized features.
        Has smallest file size.

    -> UI:

    # Title of the app
    st.title("Answer these questions to determine your disease")

    # Initialize session state
    if "submitted" not in st.session_state:
        st.session_state.submitted = False
    if "prediction" not in st.session_state:
        st.session_state.prediction = None

    # Create form for answers
    if not st.session_state.submitted:
        with st.form(key="question_form"):
            answers = []
            for i, question in enumerate(disease_questions, 1):
                answer = st.radio(f"Question {i}: {question}", options=["Yes", "No"], key=f"q{i}")
                answers.append(1 if answer == "Yes" else 0)
            submit_button = st.form_submit_button(label="Submit Answers")

            if submit_button:
                # Write to CSV for debugging (optional)
                write_to_csv("main_V2_data.csv", disease_questions, answers)
                st.session_state.submitted = True
                # Run prediction
                prediction = predict_disease(answers, disease_questions)
                if prediction:
                    st.session_state.prediction = prediction
                    st.success("Prediction complete!")
                else:
                    st.error("Prediction failed. Please try again.")

    # Display prediction
    if st.session_state.submitted and st.session_state.prediction:
        pred = st.session_state.prediction
        st.write("### Prediction Result:")
        st.write(f"**Most likely disease**: {pred['predicted_disease']}")
        st.write("**Class probabilities**:")
        for cls, prob in pred['probabilities'].items():
            st.write(f"{cls}: {prob:.2%}")
        if pred['predicted_disease'] == "tuberculosis":
            st.write("Treatment: Long-term antibiotics (e.g., isoniazid, rifampin) for 6-9 months; directly observed therapy (DOT) to ensure compliance.\n\nCommon Causes: Infection by Mycobacterium tuberculosis, spread through airborne droplets; risk factors include close contact with infected individuals, weakened immune systems (e.g., HIV), and living in high-prevalence areas.")
        
        elif pred['predicted_disease'] == "pneumonia":
            st.write("Treatment: Antibiotics for bacterial pneumonia (e.g., amoxicillin); antivirals or antifungals for viral/fungal cases; oxygen therapy and fluids for severe cases.\n\nCommon Causes: Bacterial (Streptococcus pneumoniae), viral (e.g., influenza), or fungal infections; risk factors include smoking, chronic lung diseases, and recent respiratory infections.")

        elif pred['predicted_disease'] == "lung_cancer":
            st.write("Treatment: Surgery, chemotherapy, radiation, targeted therapy, or immunotherapy, depending on stage and type (small cell or non-small cell).\n\nCommon Causes: Smoking (primary cause), exposure to radon, asbestos, or secondhand smoke; family history and occupational hazards (e.g., mining) increase risk.")

    
    st.title("Do a deeper analysis with images?")


"""


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
    # feature 1
    import json
    memoization_file_name = "dict_memoization.json"
    if not os.path.exists(memoization_file_name):
        dict_memoization = {}
    else:
        with open(memoization_file_name, 'r') as file_obj:
            dict_memoization = json.load(file_obj)

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
    
    # feature 1

    with open(memoization_file_name, 'w') as file_obj:
        json.dump(dict_memoization, file_obj)

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