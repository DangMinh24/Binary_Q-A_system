
SIMPLE_PREDICATE=("ROOT",(("S",("NP","VP",".")),) )
def if_match(tree,pattern):
    if not isinstance(pattern,tuple):
        return tree.label()==pattern
    else:
        parent=pattern[0]
        child=pattern[1]
        if tree.label()==parent and len(tree)==len(child):
            for i in range(len(tree)):
                subtree=tree[i]
                if not if_match(subtree,child[i]):
                    return False
            return True


def find_predicates(parsed_trees):
    result=[]
    for parsed_tree in parsed_trees:
        if if_match(parsed_tree,SIMPLE_PREDICATE):
            result.append(parsed_tree[0])
    return result
def tree2string(tree):
    return tree.leaves()

def check_auxiliary(word):
    auxiliary_list=["be","is","isn't","are","aren't",
                    "can","can't","could","couldn't",
                    "should","shouldn't",
                    "may","might","will","would"]
    if word in auxiliary_list:
        return True
    return  False

def bin_q2sent(question_tree):
    assert question_tree[0].label()=="SQ"
    head_verb=question_tree[0][0]
    aux=head_verb.leaves()[0].lower()
    subj=question_tree[0][1]
    obj=question_tree[0][2]
    if check_auxiliary(aux):
        sent=subj.leaves()+[aux]+obj.leaves()
        return " ".join(sent)
    # else:

# def