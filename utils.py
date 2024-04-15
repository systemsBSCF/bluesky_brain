# utils.py
import requests
from openai import OpenAI
import streamlit as st

@st.cache_data
def fetch_data_from_backend(prospect_id):
    api_url = "http://benatarofir.pythonanywhere.com/fetch_user_data"
    params = {"user_id": prospect_id, "module_api_name": 'Accounts'}
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data from backend"}

@st.cache_resource
def get_context(JSON_data):
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    messages = [
        {"role": "system", "content": "You are tasked with interpreting JSON data to generate concise narratives in plain English. These narratives will be utilized as context within a chatbot application for BlueSky Capital Funding, a company specializing in Merchant Cash Advance (MCA) loans. Your generated context is crucial for assisting sales representatives in composing targeted emails to potential clients. Your response should exclusively contain the context derived from the provided JSON data. Structure your output to first present the prospect's general information, followed by a narrative crafted from the JSON data. Aim for a medium-length output that is neither too brief nor overly extended."},
        {"role": "user", "content": JSON_data}
    ]
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=messages
    )
    return response.choices[0].message.content

@st.cache_resource
def generate_response(user_input, context):
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    messages = [
        {"role": "system", "content": context},
        {"role": "user", "content": user_input},
        
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        
    )
    return response.choices[0].message.content

@st.cache_data
def fetch_reps_data(sales_rep_id):
    # Make an API request to the Flask backend to fetch user data
    api_url = "https://wideeyed-forked-enterprise-benatarofir.replit.app/fetch_reps_data"
    params = {"user_id": sales_rep_id}
    response = requests.get(api_url, params=params)
   
    if response.status_code == 200:
        return response.json()
    else:
        return None