import ast
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def extract_names(obj:str) ->str:
    return [item['name'] for item in ast.literal_eval(obj)]


def extract_top_cast(obj:str ,top_n:int =3)-> str:
    return [item['name'] for item in ast.literal_eval(obj)[:top_n]]

def fetch_director(obj :str) ->str:
    return [item['name']for item in ast.literal_eval(obj)
        if item['job'] == 'Director']

def stem(text:str)->str:
    return " ".join(ps.stem(word) for word in text.split())