import pandas as pd
import re
import string

def load_data():
    df_csv = pd.read_csv("Datasets/full_dataset.csv")
    df_csv = df_csv.rename(columns={"input": "question", "target": "answer"})
    df_txt = pd.read_csv("Datasets/dialogs.txt", sep='\t', header=None, names=["question", "answer"])
    df_greetings = pd.read_csv("Datasets/chatbot_greetings_dataset.csv")
    df_greetings = df_greetings[["input", "response"]].rename(columns={"input": "question", "response": "answer"})
    df = pd.concat([df_greetings, df_csv, df_txt], ignore_index=True)
    df = df.dropna()
    return df

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def preprocess_data(df):
    df["clean_question"] = df["question"].apply(clean_text)
    return df
