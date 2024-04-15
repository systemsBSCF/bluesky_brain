# your_data_page.py
import streamlit as st
from utils import fetch_reps_data

def show_your_data_page():
    st.title("Your Data")
   
    # Get the user ID and sales rep ID from the query parameters
    user_id = "4910408000047960117" #st.experimental_get_query_params().get("user_id", [""])[0]
    sales_rep_id = "4910408000098821001" #st.experimental_get_query_params().get("sales_rep_id", [""])[0]
   
    if  sales_rep_id:
        # Fetch user data from the backend
        user_data = fetch_reps_data(sales_rep_id)
       
        if user_data:
            # Display user data
            
            st.write("Sales Rep ID:", sales_rep_id)
            st.write("Sales Stats:")
            # Display sales stats from user_data
            # ...
        else:
            st.error("Failed to fetch user data.")
    else:
        st.error("User ID and Sales Rep ID are required.")