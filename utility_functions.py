
import spacy
from collections import Counter
from string import punctuation



def get_hotwords(text,nlp):

    result = []
    pos_tag = ['PROPN', 'ADJ', 'NOUN'] # 1
    doc = nlp(text.lower()) # 2
    for token in doc:
        # 3
        if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        # 4
        if(token.pos_ in pos_tag):
            result.append(token.text)
                
    return result # 5



def add_numerics(title,titleHotwords):  
    # ---------------------
    # when get_hotwords fails to include numberic information, this function adds it back in 
    #
    # ---------------------
    for titleToken in title.split(' '):
        if titleToken.isnumeric():
            if titleToken not in titleHotwords:
                print(f'Number {titleToken} not found in hotwords, adding')
                titleHotwords.append(titleToken)
    
    return titleHotwords



