simple chatbot

created by shreshtha and updated for modern web and natural language processing.

welcome to the simple chatbot. this project is a stream lit based chatbot built in python. it uses spacy for natural language processing and cosine similarity to understand what you type and find the best reply from its dataset. 

this is mainly a proof of concept. to make the bot smarter and talk about more things, we just need to give it bigger datasets to learn from.

this version has a clean web interface, memory of past messages, and built in features to solve math or tell you the time and date.

capabilities and features
it uses stream lit for a clean chat interface in your browser.
it uses spacy to change sentences into numbers that the computer understands.
it uses cosine similarity to find the closest matching question in its dataset.
it remembers the last few messages to understand the context of your questions.
it can solve basic math equations and tell you the current time or date.
it has fast hardcoded answers for simple hellos and goodbyes.

how it works
the project is built in clear separate parts.

the data processing part reads from three different sources in the datasets folder. it combines a full dataset, a dialog text file, and a greetings dataset into one big table and cleans up the text by removing punctuation and making it lowercase.

the nlp part uses the spacy language model to turn every cleaned question into numbers. it saves these calculations into cache files so the bot loads instantly the next time.

the chatbot brain is where the real logic happens. when you send a message, it cleans your text, checks if you are asking for the time or doing math, checks for simple greetings, and if none of those match, it searches the entire dataset for the highest matching answer.

the user interface uses stream lit to bring it all together. it shows a loading spinner when starting, keeps track of your chat history, and displays the chat bubbles on your screen.

how to use it
make sure you have python installed. it is best to use a virtual environment.

install the required packages by running pip install streamlit pandas scikit learn numpy spacy in your terminal.

the bot uses a medium english model from spacy. you should download it by running python m spacy download en core web md in your terminal.

start the server by running streamlit run main.py in your terminal.

a new browser tab will open automatically. type your message in the chat box at the bottom and press enter to talk to the bot.
 
