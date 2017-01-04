
def is_NOUN(tag):
    if tag.startswith("N"):
        return True
    return False

def is_VERB(tag):
    if tag.startswith("V"):
        return True
    return False

def is_ADJ(tag):
    if tag.startswith("JJ"):
        return True
    return False

def is_ADV(tag):
    if tag.startswith("RB"):
        return True
    return False