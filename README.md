# Simple ChatBot

*Created by Shreshtha, updated for Modern UI and NLP*

Welcome to the **Simple ChatBot**! This project is a modular, Streamlit-based chatbot built in Python. It uses advanced Natural Language Processing (via **spaCy** word embeddings) and Cosine Similarity to understand user input and find the most relevant response from a compiled dataset.

> **Note:** This project is fundamentally a proof-of-concept for NLP that operates based on the provided datasets. to make the chatbot "smarter" and capable of handling a wider variety of topics, we would simply need to include larger and more diverse datasets for it to search through.

This updated version features a clean web interface, conversation history, and built-in rules for math and time/date detection!

---

## Capabilities & Features

1. **Modern Web UI**: Uses `Streamlit` for a clean, WhatsApp-like chat interface right in your browser.
2. **Advanced NLP**: Leverages `spaCy`'s `en_core_web_md` model to convert sentences into dense vector representations.
3. **Smart Matching**: Uses `scikit-learn`'s `cosine_similarity` to find the semantically closest question in the dataset.
4. **Context Awareness**: Remembers the last few messages to handle short follow-up questions contextually.
5. **Rule-based Utilities**:
   - **Math Solver**: Can evaluate basic math expressions (e.g., "5 * 5").
   - **Time & Date**: Can tell you the current time or date if asked.
   - **Greetings & Farewells**: Fast, hardcoded responses for basic conversational pleasantries.

---

## Workflow: How Does it Work?

The project has been refactored into a clear, modular architecture:

### 1. **Data Processing (`data_processing.py`)**
A chatbot is only as smart as its knowledge base! This module reads from three different data sources located in the `Datasets/` folder: a full dataset (`full_dataset.csv`), a dialog text file (`dialogs.txt`), and standard greetings (`chatbot_greetings_dataset.csv`). It uses `pandas` to stitch them all into one giant, unified DataFrame and cleans the text (removing punctuation, making lowercase).

### 2. **NLP & Vectorization (`model.py`)**
Computers understand numbers better than text. This script loads the `spaCy` language model and converts every cleaned question in our dataset into a mathematical vector representation. To make the bot load instantly next time, it caches these calculations into `.npy` and `.pkl` files in the `Datasets/` folder.

### 3. **The Brains (`chatbot.py`)**
This is the core logic. When you send a message, the `ChatBot` class follows this workflow:
- **Clean**: Strips punctuation from your input.
- **Check Utilities**: Checks if you are asking for the time/date or supplying a math equation.
- **Check Greetings**: Checks if it's a simple greeting or farewell.
- **Vector Search (Fallback)**: If none of the above match, it transforms your query into a vector, calculates the cosine similarity against the entire dataset, and returns the highest-matching answer (as long as it exceeds a 60% confidence threshold).

### 4. **User Interface (`main.py`)**
We use `Streamlit` to tie everything together. It initializes the bot (with a loading spinner), maintains the chat history using `st.session_state`, and dynamically renders the chat bubbles on the screen.

---

## Steps to Use (From Scratch)

Follow these steps to get the bot running on your local machine:

### 1. Prerequisites
Ensure you have Python 3.8+ installed on your system. It is highly recommended to use a virtual environment.

### 2. Install Dependencies
Install the required packages. You will need:
```bash
pip install streamlit pandas scikit-learn numpy spacy
```

### 3. Download the Language Model
The bot uses `spaCy`'s medium English model. You must download it before running (the code will attempt to download it automatically if missing, but it's best to run this manually):
```bash
python -m spacy download en_core_web_md
```

### 4. Run the Application
Start the Streamlit server by running `main.py`:
```bash
streamlit run main.py
```

### 5. Chat!
A new browser tab will automatically open at `http://localhost:8501`. Type your message in the chat box at the bottom and press Enter to talk to the bot!
