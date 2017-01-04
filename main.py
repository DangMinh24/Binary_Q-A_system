from Extract_References import extract_statements
from stanford_parser import SFParser
from convert_extract import bin_q2sent
from answer import answer_bin_q
from choose_best_reference import calculate_lfd,closest_sentence
STANFORD_JAR="/home/dang/Desktop/stanford-corenlp-full-2016-10-31/stanford-corenlp-3.7.0.jar"
STANFORD_MODEL="/home/dang/Desktop/stanford-corenlp-full-2016-10-31/stanford-corenlp-3.7.0-models.jar"

parser=SFParser(STANFORD_JAR,STANFORD_MODEL)


html_file="kanjira.html"
# references=extract_statements(html_file)

# question="Is kanjira a hard Indian drum to play ?"
# question_parse=parser.raw_parse(question)
# for i in question_parse:
#     question_tree=i
#
# transformed_q=bin_q2sent(question_tree)
# reference=closest_sentence(transformed_q,references)
# print(answer_bin_q(transformed_q,reference))



from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize
from stanford_parser import SFParser
from stanford_parser import STANFORD_JAR,STANFORD_MODEL

from convert_extract import find_predicates
from convert_extract import tree2string
def extract_statements(html_file):
    with open(html_file,"r") as file:
        soup=BeautifulSoup(file,"html.parser")
        for sup in soup.find_all("sup"):
            sup.decompose()
        paragraphs=soup.find_all("p")
        paragraphs=[p.get_text() for p in paragraphs]
        paragraphs=" ".join(paragraphs)
        sentences=sent_tokenize(paragraphs)
        parser=SFParser(STANFORD_JAR,STANFORD_MODEL)
        parsed_sents=parser.raw_parse_sents(sentences)
        parsed_trees=[]
        for parsed_sent in parsed_sents:
            for i in parsed_sent:
                parsed_trees.append(i)

        for tree in parsed_trees:
            print(tree)
        # predicates=find_predicates(parsed_trees)
        #
        # answer_sents=[tree2string(pred) for pred in predicates]
        # for iter,sent in enumerate(answer_sents):
        #     answer_sents[iter]=" ".join(sent)
        # return answer_sents

# Wh-question
#   Ex: q-Who is John ? references-["John is a doctor","John plays sport","John ate potato",...]
#
# In some kind of wh-question, we should use a NER parser to determine where is the answer
# To do with Wh-question, we must:
#   + Have a function to specific type of question: How, Why, Who, Where
#   + Each type of question will have a different transformed question function. Ex: "Who is John?".
# This question is so short, so if we transformed it, we only get "John is".
# =>So must have method to get a best sentence in references
#   + After choosing best reference, each type of question must have a method to extract information needed
# Ex: "John is a doctor." is an answer. When parse this tree we get (ROOT(S (NP (NNP John)) (VP (VBZ is) (NP (DT a) (NN doctor))) (. .)))
# Depend on this structure, we can get a answer
