from nltk.parse.stanford import StanfordParser
STANFORD_JAR="/home/dang/Desktop/stanford-corenlp-full-2016-10-31/stanford-corenlp-3.7.0.jar"
STANFORD_MODEL="/home/dang/Desktop/stanford-corenlp-full-2016-10-31/stanford-corenlp-3.7.0-models.jar"
def SFParser(jar_path,model_path):
    return StanfordParser(jar_path,model_path)