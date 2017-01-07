# We will have some article to express knowledges, concepts in wikipedia
# These articles were written in html format. If we want to get information from these articles, we must parse them

# Using BeautifulSoup to parse html file into text file:
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
from nltk.parse.stanford import StanfordParser
from nltk.tree import Tree
file=open("kanjira.html","r")
soup=BeautifulSoup(file.read(),"html.parser")
# print(soup.prettify())
# for link in soup.find_all("a"):
#     print(link)

for citation in soup.find_all("sup"):
    citation.decompose() # remove all <sup> tag out of html file

paragraphs=soup.find_all("p")
for p in paragraphs:
    print(p.get_text())

paragraphs_text=[p.get_text() for p in paragraphs]
all_text=" ".join(paragraphs_text)
sentences=sent_tokenize(all_text)

# To user StanfordParser on python, we must determine some parameters on our system:
# 1/ Location of Standford_parser. usr/<username>/Desktop/stanford-corenlp-full-2016-10-31 (or stanford-parser-python-r22186,
# depend on your download version)
# 2/ Location of Standford models. usually like 1/, or if you save your training model in somewhere else,
# this is path to your model. usr/<username>/Desktop/stanford-corenlp-full-2016-10-31
# 3/ Location of Java. usr/bin/java
# 4/ Location of your PCFG model : usr/<username>/Desktop/stanford-corenlp-full-2016-10-31/edu/stanford/models/lexparser/englishPCFG.ser.gz


parser=StanfordParser("[userlocation]/stanford-corenlp-full-2016-10-31/stanford-corenlp-3.7.0.jar",
                      "[userlocation]/stanford-corenlp-full-2016-10-31/stanford-corenlp-3.7.0-models.jar")
parse_trees=parser.raw_parse_sents(sentences[:200])

# question base pattern
SIMPLE_PREDICATE=("ROOT", (("S", ("NP","VP",".")),))
APPOSITION=("S", (("NP",("NP",",","NP")), "VP","."))

trees=[]
for tree in parse_trees:
    for i in tree:
        tmp_tree=i
    trees.append(tmp_tree)

PATTERN_EXAMPLE=("S",("NP","VP","."))
# To see how to compare pattern and Tree, we compare tmp tree and pattern SIMPLE_PREDICATE
def if_match(tree,pattern):
    if not isinstance(pattern,tuple):
        return tree.label()==pattern
    else:
        parent=pattern[0]
        children=pattern[1]
        if tree.label()==parent and len(tree)==len(children):
            for i in range(len(tree)):
                sub_tree=tree[i]
                if not if_match(sub_tree,children[i]):
                    return False
            return True
print(if_match(tmp_tree,PATTERN_EXAMPLE))

# Now we can create a function for find each question pattern, which we defined first
# in SIMPLE_PREDICATE

def find_appositions(parse_tree):
    if if_match(parse_tree,APPOSITION):
        return (parse_tree[0,0],parse_tree[0,2])

def find_predicates(parse_trees):
    result=[]
    for parse_tree in parse_trees:
        if if_match(parse_tree,SIMPLE_PREDICATE):
            result.append(parse_tree[0])
    return result

predicates=find_predicates(trees)
# for pred in predicates:
#     print(pred)

tmp_pred=predicates[0]
def sent_to_bin_q(sentence_tree):
    assert(sentence_tree.label()=="S")
    sub=sentence_tree[0]
    if sub.label()!="NP":
        return sentence_tree.leaves()
    assert (sub.label() =="NP")

    vp=sentence_tree[1]
    assert(vp.label()=="VP")
    head_verb=vp[0]
    # head_verb have 3 case: 1) is/are/has 2) modal(may,can,should,...) 3) VP
    if head_verb.label()=="VP":
        return
    else:
        verb=head_verb
    modal=verb[0]

    raw_sent=sentence_tree.leaves()
    raw_sent.remove(modal)
    raw_sent[0]=raw_sent[0].lower()
    question= [modal] +raw_sent
    return question
    # for i in vp[1:]:
    #     print(i)

bi_quest=[]
for predicate in predicates:
    bi_quest.append(sent_to_bin_q(predicate))
