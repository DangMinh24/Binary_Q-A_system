from nltk.corpus import wordnet

# Topology:
#   -hyponym: a word of more specific meaning than a general. Ex

def hyponym(word,pos):
    hypos=set()
    hypos.add(word)
    for synset in wordnet.synsets(word,pos):
        for hyponym in synset.hyponyms():
            for lemma in hyponym.lemmas():
                # print(lemma)
                hypos.add(lemma.name().replace("_"," "))
    return list(hypos)
def synonym(word,pos):
    synos=set()
    synos.add(word)
    for synset in wordnet.synsets(word,pos):
        for lemma in synset.lemmas():
            synos.add(lemma.name().replace("_"," "))
    return list(synos)

