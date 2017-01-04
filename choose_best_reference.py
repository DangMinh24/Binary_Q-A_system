from nltk.tokenize import word_tokenize
from nltk import defaultdict
import math
def closest_sentence(target,references):
    # You get a set of sentences which are used as answers for your later question
    # However, to extract answer for your question, it must know which sentence in this set of sentences will
    # be used to extract information
    # To do this, we must compare similarity between transformed_question with each sentences in the set
    # Choose the best sentence have similarity with transformed_question

    # Comparing similarity between 2 sentences is a very tough problem, and still being developed.
    # To simplify, we only compare similarity between 2 sentences by cosine
    # Cosine similarity definition here: https://en.wikipedia.org/wiki/Cosine_similarity
    # Disadvantage of this method appears when you compare two sentences with similar meaning but have different representation
    # To see more example of cosine similarity : http://stackoverflow.com/questions/1746501/can-someone-give-an-example-of-cosine-similarity-in-a-very-simple-graphical-wa
    lfd=calculate_lfd(references)
    best_cosine=0
    best_select=-1

    # tokenized_target=word_tokenize(target)
    vec_target=sent2vec(target,lfd)

    for iter,ref in enumerate(references):
        vec_ref=sent2vec(ref,lfd)
        similarity_score=dot(vec_ref,vec_target)
        if similarity_score>best_cosine:
            best_cosine=similarity_score
            best_select=iter

    return references[best_select]

def calculate_lfd(sentences):
    N=len(sentences)

    fd=defaultdict(lambda :0)
    for sentence in sentences:
        tokenize_sent=word_tokenize(sentence)
        for w in tokenize_sent:
            fd[w]+=1
    l_value=defaultdict(lambda :0)
    for w in fd.keys():
        l_value[w]=math.log(float(N)/fd[w],2)

    return l_value
def sent2vec(sent,lfd):
    tokenized_sent=word_tokenize(sent)
    vec=defaultdict(lambda :0)
    for w in tokenized_sent:
        if w in lfd.keys():
            vec[w]+=1
    max_freq = 0
    for k,v in vec.items():
        if max_freq<v:
            max_freq=v

    for k in vec.keys():
        vec[k]=lfd[k]*(float(vec[k])/max_freq)

    return vec
def dot(v_a,v_b):
    norm_v_a=norm(v_a)
    norm_v_b=norm(v_b)
    mutual_space=dict()
    for key in v_a.keys():
        if key not in mutual_space.keys():
            mutual_space[key]=0
    for key in v_b.keys():
        if key not in mutual_space.keys():
            mutual_space[key]=0
    result=0
    for key in mutual_space.keys():
        if key not in v_a:
            v_a[key]=0
        if key not in v_b:
            v_b[key]=0
        result+=v_a[key]*v_b[key]

    return float(result)/(norm_v_a*norm_v_b)

def norm(vector):
    result=0
    for w in vector.keys():
        result+= vector[w]**2
    return math.sqrt(result)

