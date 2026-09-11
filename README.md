# Local AI Study Assistant

A beginner-friendly AI question-answering application built using **Ollama, Gemma 3:4B, Python, and Streamlit**.

## Project Overview

This project allows users to ask study-related questions and receive responses from a locally running AI model. The application uses Ollama to run the Gemma 3:4B model and Streamlit to provide a simple interactive web interface.

## Technologies Used

* Python
* Streamlit
* Ollama
* Gemma 3:4B

## Features

* Local AI question answering
* Interactive chat interface
* Conversation history
* Clear chat option
* No external cloud API required

## Installation

### 1. Clone the repository

git clone <repository-link>
cd ollama_streamlit_chatbot

### 2. Create a virtual environment

python -m venv venv

### 3. Activate the environment

Windows PowerShell:
.\venv\Scripts\Activate.ps1

### 4. Install dependencies

pip install -r requirements.txt

### 5. Install the Ollama model

ollama pull gemma3:4b

### 6. Run the application

streamlit run app.py

## Sample Prompts Tested

1. Explain polymorphism in Java in simple words with an example.
2. What is the difference between a stack and a queue?
3. Explain the difference between a list and a tuple in Python.
4. What is the difference between Artificial Intelligence and Generative AI?
5. Give me a short revision note on database normalization.

## Learning Outcomes

Through this project, I learned how to:

* Run a local language model using Ollama
* Connect Python with a local AI model
* Build an interactive interface using Streamlit
* Manage chat history using Streamlit session state
* Organize and document a Python AI project

## Author

ManiHarsha Chetlapelly
