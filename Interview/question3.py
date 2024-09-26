#Interview question

f={'a':['a','b','c','d'],
    'b':['e','c','d'],
    'c':['f','b','k'], 
    'd':['g','b','y','d']
}

def uniqueset(x):
    empty=[]
    for i in f.values():
        empty.extend(i)
    return set(empty)


uniqueset(f)