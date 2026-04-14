import re
import random
import datetime
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from data_processing import clean_text

class ChatBot:
    def __init__(self, df, question_matrix, nlp):
        self.df = df
        self.question_matrix = question_matrix
        self.nlp = nlp
        self.chat_history = []

    def get_time_date(self, text):
        text = text.lower()
        if "time" in text:
            return f"time is {datetime.datetime.now().strftime('%I:%M %p')}"
        elif "date" in text or "day" in text:
            return f"date is {datetime.datetime.now().strftime('%B %d, %Y')}"
        return None

    def calculate_math(self, expression):
        match = re.search(r'(\d+(?:\.\d+)?)\s*([\+\-\*\/])\s*(\d+(?:\.\d+)?)', expression)
        if match:
            num1 = float(match.group(1))
            op = match.group(2)
            num2 = float(match.group(3))
            if op == '+':
                return num1 + num2
            elif op == '-':
                return num1 - num2
            elif op == '*':
                return num1 * num2
            elif op == '/':
                if num2 != 0:
                    return num1 / num2
                else:
                    return "Cannot divide by zero"
        return None

    def get_response(self, user_input, threshold=0.6, use_history=True):
        cleaned_input = clean_text(user_input)
        response_text = ""
        greeting_keywords = ['hello', 'hi', 'hey', 'greetings', 'sup', 'whatsup']
        farewell_keywords = ['bye', 'goodbye', 'see ya', 'cya', 'farewell']
        words = cleaned_input.split()
        is_greeting = any(word in greeting_keywords for word in words) and len(words) < 5
        is_farewell = any(word in farewell_keywords for word in words) and len(words) < 5
        
        time_date_result = None
        if "time" in cleaned_input or "date" in cleaned_input or "day" in cleaned_input:
            time_date_result = self.get_time_date(user_input)
            
        math_result = self.calculate_math(user_input)

        if time_date_result is not None:
            response_text = f"Chatbot [TimeDate] : The {time_date_result}"
        elif math_result is not None:
            response_text = f"Chatbot [Math] : The answer is {math_result}"
        elif is_greeting:
            greetings = ["Hello there!", "Hi! How can I help you?", "Greetings! Whats up?", "Hey!"]
            response_text = f"Chatbot [Greeting] : {random.choice(greetings)}"
        elif is_farewell:
            farewells = ["Goodbye!", "See you later!", "Have a great day!", "Take care!"]
            response_text = f"Chatbot [Farewell] : {random.choice(farewells)}"
        else:
            search_query = cleaned_input
            if use_history and len(self.chat_history) > 0 and len(cleaned_input.split()) <= 3:
                last_query = self.chat_history[-1]['user']
                search_query = f"{clean_text(last_query)} {cleaned_input}"

            input_vector = self.nlp(search_query).vector.reshape(1, -1)
            similarities = cosine_similarity(input_vector, self.question_matrix).flatten()
            best_sim_idx = int(np.argmax(similarities))
            best_sim_score = similarities[best_sim_idx]

            if best_sim_score < threshold:
                response_text = "Chatbot [GeneralQA] : Sorry, I'm not sure how to answer that. Could you rephrase?"
            else:
                response_text = f"Chatbot [GeneralQA] : {self.df['answer'].iloc[best_sim_idx]}"

        self.chat_history.append({'user': user_input, 'bot': response_text})
        if len(self.chat_history) > 5:
            self.chat_history.pop(0)

        return response_text
