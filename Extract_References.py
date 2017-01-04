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

        predicates=find_predicates(parsed_trees)

        answer_sents=[tree2string(pred) for pred in predicates]
        for iter,sent in enumerate(answer_sents):
            answer_sents[iter]=" ".join(sent)
        return answer_sents