import spacy
import numpy as np
import os
import pandas as pd

def load_nlp_model():
    try:
        return spacy.load("en_core_web_md")
    except OSError:
        from spacy.cli import download
        download("en_core_web_md")
        return spacy.load("en_core_web_md")

def create_question_matrix(df, nlp):
    matrix_file = "Datasets/question_matrix.npy"
    df_cached_file = "Datasets/processed_df.pkl"
    if os.path.exists(matrix_file) and os.path.exists(df_cached_file):
        df = pd.read_pickle(df_cached_file)
        question_matrix = np.load(matrix_file)
        return df, question_matrix

    df["question_vector"] = list(doc.vector for doc in nlp.pipe(df["clean_question"]))
    question_matrix = np.vstack(df["question_vector"].values)
    np.save(matrix_file, question_matrix)
    df.to_pickle(df_cached_file)
    
    return df, question_matrix
