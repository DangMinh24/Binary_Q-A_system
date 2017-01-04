
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from hyponym_synonym import hyponym, synonym
from check import *
from nltk.corpus import wordnet
wn_NOUN=wordnet.NOUN
wn_VERB=wordnet.VERB
wn_ADJ=wordnet.ADJ
wn_ADV=wordnet.ADV

def answer_bin_q(transformed_q,reference):
    tagged_transformed_q = pos_tag(word_tokenize(transformed_q))
    tmp=filter_answer_bin_q(tagged_transformed_q)
    print(tmp)
    list_check=[synonym(w,t) for w,t in tmp]
    print(list_check)
    got_all=False
    tokenized_reference=word_tokenize(reference)
    result_list=[False]*len(list_check)
    for iter,w_l in enumerate(list_check):
        for w in w_l:
            if w in tokenized_reference:
                result_list[iter]=True
                break
    if "not" in reference and all(result_list)==True:
        return False

    if all(result_list)==True:
        return True

def filter_answer_bin_q(tagged_sent):
    result=[]
    for w,t in tagged_sent:
        if is_NOUN(t):
            result.append((w,wn_NOUN))
        elif is_VERB(t):
            result.append((w,wn_VERB))
        elif is_ADJ(t):
            result.append((w,wn_ADJ))
        elif is_ADV(t):
            result.append((w,wn_ADV))
    return result