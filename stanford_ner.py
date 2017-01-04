from nltk.tag.stanford import StanfordNERTagger

NER_CF="/home/dang/Desktop/stanford-ner-2015-12-09/classifiers/english.all.3class.distsim.crf.ser.gz"
NER_JAR="/home/dang/Desktop/stanford-ner-2015-12-09/stanford-ner.jar"
def SFNer(classifier_path,jar_path):
    return StanfordNERTagger(classifier_path,jar_path)
from nltk.tokenize import word_tokenize
tagger=SFNer(NER_CF,NER_JAR)
