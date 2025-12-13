
import streamlit as st
from typing import List, Optional

def render_filtering_ui():
    """
    Renders the UI and returns the filter config only if valid.
    """
    
    # 1. Containerize inputs to prevent premature re-runs
    with st.form(key="data_intake_form"):
        st.subheader("Configuration")
        
        # Mandatory Field
        # Note: We cannot enforce 'required' here, we validate post-submit
        user_name: str = st.text_input(
            label="User Name (Mandatory)", 
            placeholder="Enter your identifier",
            help="This field is required to proceed."
        )
        
        # Multi-choice Filters
        # Hardcoded options for example, usually fetched from data
        options_source = ["Log Logs", "Metrics", "Traces", "Events"]
        selected_filters: List[str] = st.multiselect(
            label="Select Data Streams",
            options=options_source,
            default=["Metrics"]
        )
        
        # The Trigger
        # This returns True ONLY on the re-run caused by the click
        submitted: bool = st.form_submit_button(label="Continue >>")

    # 2. Validation Logic (Outside the form context)
    if submitted:
        # Check Mandatory Constraint
        if not user_name.strip():
            st.error("❌ Validation Error: User Name is mandatory.")
            # HALT EXECUTION HERE
            st.stop()
        
        # Check Business Logic Constraint (Optional)
        if not selected_filters:
            st.warning("⚠️ Warning: No filters selected. Defaulting to ALL.")
            
        # 3. Success State
        st.success(f"Welcome, {user_name}. Processing {len(selected_filters)} streams.")
        
        # Return the clean data dict for downstream consumption
        return {
            "name": user_name,
            "filters": selected_filters,
            "is_valid": True
        }

    return None

# --- Main Execution Flow ---
def main():
    st.title("System Filter Interface")
    
    # The UI function handles the display and the logic
    filter_data = render_filtering_ui()
    
    # Only proceed if the form was submitted AND valid
    if filter_data:
        st.divider()
        st.write("### System Output")
        st.json(filter_data)
        # Your heavy logic (Pandas filtering, API calls) goes here
        # ...

if __name__ == "__main__":
    main()