import streamlit as st
import requests
import matplotlib.pyplot as plt
import numpy as np
import os
from dotenv import load_dotenv

# ==========================================
# 1. PURE LOGIC & BACKEND (Defined at Top)
# ==========================================

# Load environment variables once
load_dotenv()

# We replace the manual JSON file handling with Streamlit's native Caching
# This persists data across re-runs automatically and is much faster/safer.
@st.cache_data(show_spinner=False)
def request_food(api_key, food_query, page_limit=25):
    """
    Fetches food data from USDA API. 
    Cached automatically: inputs (query) -> output (json) mapping is saved.
    """
    search_url = "https://api.nal.usda.gov/fdc/v1/foods/search"
    
    try:
        response = requests.get(
            search_url, 
            params={"api_key": api_key, "query": food_query, "pageSize": page_limit}, 
            timeout=10
        )
        response.raise_for_status()
        data = response.json().get("foods", [])
        
        if not data:
            return None # Handle empty logic in the UI layer
            
        return data
        
    except requests.exceptions.RequestException as e:
        st.error(f"API Request Failed: {e}")
        st.stop() # Halts execution safely

def get_nutrient(food, name):
    """Extracts specific nutrient value from the complex nested JSON"""
    for nutrient in food.get("foodNutrients", []):
        if nutrient.get("nutrientName") == name:
            return nutrient.get("value")
    return 0.0 # Return 0 if nutrient missing to prevent crashes

def get_nutrients_food(food):
    """Aggregates the 4 key macros"""
    if not food:
        return None
        
    kcal = get_nutrient(food, "Energy")
    prot = get_nutrient(food, "Protein")
    fat  = get_nutrient(food, "Total lipid (fat)")
    carb = get_nutrient(food, "Carbohydrate, by difference")
    
    return kcal, prot, fat, carb

def create_comparison_graph(food1, food2, data1, data2, nutrients):
    """
    Refactored to RETURN a Figure object instead of calling plt.show().
    Streamlit needs the object to render it.
    """
    label_1 = food1["description"][:20] + "..." # Truncate long names
    label_2 = food2["description"][:20] + "..."

    x = np.arange(len(nutrients))
    width = 0.35

    # Explicitly create Figure and Axes objects (OO-style Matplotlib)
    fig, ax = plt.subplots(figsize=(10, 6))
    
    rects1 = ax.bar(x - width/2, data1, width, label=label_1, color='#66b3ff')
    rects2 = ax.bar(x + width/2, data2, width, label=label_2, color='#ff9999')

    ax.set_ylabel('Nutrient Density (grams per 100g)')
    ax.set_title('Nutrient Density Comparison')
    ax.set_xticks(x)
    ax.set_xticklabels(nutrients)
    ax.legend()
    
    ax.bar_label(rects1, padding=3, fmt='%.1f')
    ax.bar_label(rects2, padding=3, fmt='%.1f')
    
    plt.tight_layout()
    return fig

# ==========================================
# 2. STATE MANAGEMENT (The "Loop" Logic)
# ==========================================

def init_state():
    # 'id_counter' is our mechanism to reset the form. 
    # Incrementing it generates new keys for widgets, clearing them.
    if 'id_counter' not in st.session_state:
        st.session_state.id_counter = 0

def reset_logic():
    st.session_state.id_counter += 1

# ==========================================
# 3. UI LAYOUT & EXECUTION
# ==========================================

def main():
    st.set_page_config(page_title="USDA Food Compare", page_icon="🍎")
    init_state()

    st.title("🍎 Nutrient Comparator")
    
    # 3a. API Key Handling
    # Ideally set in .env, but UI fallback provided
    api_key = os.getenv("USDA_API_KEY")
    if not api_key:
        api_key = st.text_input("Enter USDA API Key", type="password")
        if not api_key:
            st.warning("Please provide an API Key to proceed.")
            st.stop()

    # 3b. The Input Form
    # We use the 'id_counter' to generate unique keys. 
    # When reset_logic runs, counter goes up -> keys change -> widgets reset.
    current_key = st.session_state.id_counter
    
    with st.form(key=f"search_form_{current_key}"):
        col1, col2 = st.columns(2)
        with col1:
            query_1 = st.text_input("First Food", key=f"q1_{current_key}")
        with col2:
            query_2 = st.text_input("Second Food", key=f"q2_{current_key}")
            
        # The Trigger
        submitted = st.form_submit_button("Compare Foods")

    # 3c. The Execution Logic
    if submitted:
        if not query_1 or not query_2:
            st.error("Please enter both food names.")
            st.stop()

        with st.spinner("Fetching data from USDA..."):
            # Fetch Data
            foods_1 = request_food(api_key, query_1)
            foods_2 = request_food(api_key, query_2)

            # Validation
            if not foods_1:
                st.error(f"Could not find any food matching '{query_1}'")
                st.stop()
            if not foods_2:
                st.error(f"Could not find any food matching '{query_2}'")
                st.stop()

            # Process Data (First match logic)
            # You could add a Selectbox here to let user choose which result, 
            # but we stick to your logic (index 0)
            f1_obj = foods_1[0]
            f2_obj = foods_2[0]
            
            data_1 = get_nutrients_food(f1_obj)
            data_2 = get_nutrients_food(f2_obj)
            nutrients_labels = ['Kcal', 'Protein', 'Fat', 'Carbs']

        # 3d. Output Display
        st.divider()
        st.subheader("Comparison Results")
        
        # Draw the graph
        fig = create_comparison_graph(f1_obj, f2_obj, data_1, data_2, nutrients_labels)
        st.pyplot(fig)
        
        # Raw Data (Optional Geeky Detail)
        with st.expander("See Raw Data"):
            st.write(f"**{f1_obj['description']}**", data_1)
            st.write(f"**{f2_obj['description']}**", data_2)

        # 3e. The "Continue" Feature
        # This button triggers the callback, which updates the state, 
        # causing a rerun with fresh widgets.
        st.button("Compare Another Pair (Reset)", on_click=reset_logic, type="primary")

if __name__ == "__main__":
    main()