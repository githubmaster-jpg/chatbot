import difflib
import random
from time import sleep
from datetime import datetime

word_list = ['WHAT', 'IS', 'AI', 'MACHINE', 'SUPERVISED', 'UNSUPERVISED',
             'DEEP', 'LEARNING', 'NEURAL', 'NETWORK', 'A', 'AN', 'I', 'TRIVIA'] 
             # because of the AI topic, some basic determiners and words have been added to the typo list to avoid confusion to difflib

chatbot_topics = ['AI', 'MACHINE', 'SUPERVISED', 
                  'UNSUPERVISED', 'DEEP', 'NEURAL', 'TRIVIA']

predefined_list = ['AI', 'machine learning', 'supervised learning',
                'unsupervised learning', 'deep learning', 'neural networks']

# all answers are summarized from wikipedia complemented by my own knowledge
chatbot_topic_answers = {'AI':'Artificial intelligence is intelligence exhibited by machines like computer systems. It is a field of computer science research that focuses on developing and studying methods and softwares that allow machines the highest chances of achieving set goals by being able to learn and perceive their environment in a more human like way.'
                         , 
                         'MACHINE': 'Machine learning is a research field of artificial intelligence that focuses on developing and studying algorithms that can learn from data and generalise to unseen data, allowing the compuntational algorithms to work on tasks successfully without constant human intervention.' 
                         , 
                         'SUPERVISED':'Supervised learning is a paradigm of machine learning. A supervised model is built by training it on input objects and desired output values which are most often labeled by humans. The training process should return a model that can map unseen data to excpected output values as long as the training was done successfully.'
                         , 
                         'UNSUPERVISED':'Unsupervised learning is a paradigm of machine learning. An unsupervised model is built by the algorithm learning and finding patterns in unlabeled data, meaning there is no human intervention needed in the building of an unsupervised model.'
                         , 
                         'DEEP':'Deep learning is a subset of machine learning. It utilizes neural networks in processing different types of tasks by stacking multiple layers of neurons to go through data. These layers allow it to solve various problems!'
                         , 
                         'NEURAL':'Neural network is a machine learning model inspired by the structure and function of biologically occuring networks in brains. It has layers and neurons to mimic brain functions to train itself on data.'
                         }

trivia_list = ['The first AI to beat a chess world champion in a chess match was Deep Blue! This historical moment happened in 1997.',
               'The term for "Machine learning" was coined by Arthur Samuel in 1959. Articifial intelligence has come a long way since then!',
               'A "strong AI" is an AI that aims to have a mind that is no different from a human mind. How long would it take an AI child to grow up?',
               'A robot named Sophia was given citizenship for Saudi Arabia in 2017, making her the first AI to recieve legal personhood of any country.',
               'An AI named Libratus won over $1,7 million from a poker tournament in 2017!'
               ]

def file_logger(log:str) -> None:
    """ Logs the user's and chatbot's conversation
    
    Creates a new file or writes into existing chat file all user-bot interactions.
    Exception can happen if for some reason file cannot be created in the directory the bot is in.

    Parameters
    ----------
    log : str
        The string provided by user or bot
    
    Returns
    ----------
    None
    """
    try:
        chat_file = open('chat_file.txt', 'a+')
        chat_file.write("{0} -- {1}\n".format(datetime.now().strftime("%Y-%m-%d %H:%M"), log))
        chat_file.close()
        return None
    except:
        print("Error with log file, conversation not saved.")
        return None


def user_typo_handler(question:str) -> list:
    """ Checks for possible user created typos

    By using the difflib module, we can check the user's question and match it to the
    closest word in the word_list. Includes chatbot question topics as well as other
    interactions.

    Parameters
    ----------
    question : str
        The input written by the user
    
    Returns
    ----------
    list
    """
    exact_words = difflib.get_close_matches(question,word_list, n=1,cutoff=0.5)
    if len(exact_words)>0:
        return exact_words[0]
    else:
        return list(question)

def user_question_handler(question:str, topics:list, predefined_topics:list) -> str:
    """ Checks user inputted question and sorts it to the correct answer if possible
    
    Breaks down the user's inputted question, runs it through the typo handler function word for word and
    then checks if there is any word in the question that relates to a chatbot topic through a for loop.
    If no matching word for a topic is found, the function shows a print indicating to that and exits the function.

    Parameters
    ----------
    question : str
        The input written by the user
    topics : list
        The list of topics the chatbot can answer to
    predefined_topics : list
        Chatbot's list of topics it can talk about

    Returns
    ----------
    str
    """
    question = question.upper()
    question = question.split(' ')
    question = [user_typo_handler(word) for word in question]
    for word in question:
        if word in topics:
            topic = word
            return topic
        else:
            pass
    if True: # = if still running after trying to check for a matching word
        suggestion = random.choice(predefined_topics)
        answer = (f"I'm sorry, I didn't quite understand you. Maybe you'd like to know about {suggestion}?")
        file_logger(answer)
        for char in answer:
            sleep(0.05)
            print(char, end='', flush=True)
        return None
    
def answer_returner(topic:str, topic_answer:dict)-> None:
    """ Finds the answer based on topic given
    
    Parameters
    ----------
    topic : str
        The topic that we want answered
    topic_answer : dict
        The dictionary containing topics as keys and answers as values

    Returns
    -------
    None
    """
    answer = topic_answer.get(topic)
    file_logger(answer)
    for char in answer:
        sleep(0.05)
        print(char, end='', flush=True)
    return None


def main():
    """
    Enables chatbot to run
    """
    user_question = None
    start = ("Hello, I'm chatbot! What would you like to ask me today?\n")
    for char in start:
        sleep(0.05)
        print(char, end='', flush=True)
    while True:
        if user_question is None:
            ask = ("Please enter your question below.\n")
            for char in ask:
                sleep(0.05)
                print(char, end='', flush=True)
            user_question = str(input())
            file_logger(user_question)
        else:
            ask = ("\nWhat else would you like to ask me?\n")
            for char in ask:
                sleep(0.05)
                print(char, end='', flush=True)
            user_question = str(input())
            file_logger(user_question)
        if user_question.lower() == "exit":
            print('Thanks for your time!')
            break
        question_topic = user_question_handler(user_question, chatbot_topics, predefined_list)
        if question_topic != None:
            if question_topic.upper() == "TRIVIA":
                trivia = random.choice(trivia_list)
                file_logger(trivia)
                for char in trivia:
                    sleep(0.05)
                    print(char, end='', flush=True)
            else:
                answer_returner(question_topic, chatbot_topic_answers)

if __name__ == "__main__":
    main()
