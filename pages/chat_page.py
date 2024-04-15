import json
import streamlit as st
from openai import OpenAI
from rewrite import prompts
from utils import fetch_data_from_backend

def show_chat_page():
    st.title("BlueSky Email Rewriter")
    prospect_id = st.query_params.get("prospect_id")
    if prospect_id:
        data = fetch_data_from_backend(prospect_id)
        prompt = prompts["rewrite prompt"]
        system_message = f"{prompt} --- [context]: --- {data} ---"
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
        
        if "openai_model" not in st.session_state:
            st.session_state["openai_model"] = "gpt-3.5-turbo"
        if "messages" not in st.session_state:
            st.session_state.messages = [{"role": "system", "content": system_message}]
        
        def display_messages():
            for message in st.session_state["messages"]:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
        
        st.write(f"Prospect ID: {prospect_id}")
        expander = st.expander("how to use the chat interface:")
        
        
        display_messages()
        
        prompt = st.chat_input("Your message:")
        
        if prompt:
            st.session_state["messages"].append({"role": "user", "content": prompt})
            
            api_messages = [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state["messages"]
            ]
            
            with st.chat_message("assistant"):
                stream = client.chat.completions.create(
                    model=st.session_state["openai_model"],
                    messages=api_messages,
                    stream=True
                )
                response = st.write_stream(stream)
            
            st.session_state["messages"].append({"role": "assistant", "content": response})
        
        if st.button("Clear Chat"):
            st.session_state.messages = [{"role": "system", "content": system_message}]
    else:
        st.error("Prospect ID not found in the query parameters.")