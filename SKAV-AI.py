import streamlit as st
import requests
import webbrowser
import pyautogui
from google.generativeai import configure, GenerativeModel
from IPython.display import Markdown
from urllib.parse import urlparse
import textwrap
import os

# Set up the Generative AI configuration with the API key
configure(api_key='AIzaSyBOc7WOykXVHvnU-GsMgCYZwoBqFERjQFI')

# Create a Generative Model instance (assuming 'gemini-pro' is a valid model)
model = GenerativeModel('gemini-pro')

# Function to convert plain text to Markdown format
def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Function to download and save HTML code
def download_html_code(html_content, url):
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.replace("www.", "")
        file_name = f"{domain}.html"
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        file_path = os.path.join(downloads_path, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        st.success(f"HTML content saved to {file_path}")
    except Exception as e:
        st.error(f"An error occurred while saving HTML content: {str(e)}")
# Function to automatically write content to Notepad
def write_to_notepad(content):
    try:
        file_name = "generated_code.txt"
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        file_path = os.path.join(downloads_path, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        st.success(f"Content written to Notepad and saved to {file_path}")
    except Exception as e:
        st.error(f"An error occurred while writing to Notepad: {str(e)}")



# Function to open URLs in the default web browser

def open_url(url):
    webbrowser.open(url)

# Main Streamlit application
def main():
    st.title("SKAV TECH")
    st.markdown("Streamlit-powered SKAV TECH AI: Extract HTML, AI Chatbot, Notepad Integration, and More for Enhanced Web Interaction.")
    # HTML Extraction section
    st.header("Extract HTML Code")
    url = st.text_input("Enter URL:")
    if st.button("Extract HTML Code"):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                download_html_code(response.text)
            else:
                st.error(f"Failed to retrieve HTML content. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    # AI Chatbot section
    st.header("SKAV AI Chatbot")
    question = st.text_input("Ask the model a question:")
    if st.button("Ask SKAV AI"):
        # Call your AI model and get the responsepip
        response = model.generate_content(question)
        st.text("SKAV AI Response:")
        st.write(response.text)

        # Check if the response is related to code writing
        if "write code" in question.lower() or "develop code" in question.lower() or "can you write" in question.lower() or "code" in question.lower():
            write_to_notepad(response.text)

        # Check if the response contains a URL
        if "http" in response.text:
            st.write("The response contains a URL. Do you want to open it?")
            if st.button("Open URL"):
                open_url(response.text)

        # Additional buttons
        st.markdown('---')
        st.markdown("&copy; 2024 - All rights reserved SKAV TECH.")
        st.subheader('Our recent projects using online templates')
        button_col3, button_col4 = st.columns(2)

        if button_col3.button('DataVerse AI'):
            open_url("https://dataverse-ai.vercel.app/")

        if button_col4.button('Ulink'):
            open_url("https://ulink-io.vercel.app")

        st.subheader('Contact us')
        button_insta, button_github = st.columns(2)

        if button_insta.button('Instagram'):
            open_url("https://instagram.com/sandeep_kasturi_")

        if button_github.button('Github'):
            open_url("https://github.com/sandeepkasturi")


if __name__ == "__main__":
    main()
