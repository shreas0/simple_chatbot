import streamlit as st
from data_processing import load_data, preprocess_data
from model import load_nlp_model, create_question_matrix
from chatbot import ChatBot

st.set_page_config(page_title="ChatBot")
st.title("Simple ChatBot Made By Siri")

@st.cache_resource
def load_resources():
    df = load_data()
    df = preprocess_data(df)
    nlp = load_nlp_model()
    df, question_matrix = create_question_matrix(df, nlp)
    return df, question_matrix, nlp

try:
    with st.spinner("Loading models and datasets..."):
        df, question_matrix, nlp = load_resources()
        if "bot" not in st.session_state:
            st.session_state.bot = ChatBot(df, question_matrix, nlp)
except Exception as e:
    st.error(f"Error initializing chatbot: {str(e)}")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I help you today?"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.spinner("Thinking..."):
        response = st.session_state.bot.get_response(user_input)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)


