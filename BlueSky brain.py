# main.py
import streamlit as st
from pages import chat_page, overview_page, your_data_page, agents_page

PAGES = {
    "Chat": chat_page.show_chat_page,  # where the chat interface with RAG will be presented (the entry to the app)
    "Overview": overview_page.show_overview_page,  # will show an overview of the prospect data with AI functionality to generate text on each section of the overview
    "Your Data": your_data_page.show_your_data_page,  # use the sales rep data from the CRM to present them with a map of their data
    "Agents": agents_page.show_agents_page,
}

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page()

if __name__ == "__main__":
    main()
