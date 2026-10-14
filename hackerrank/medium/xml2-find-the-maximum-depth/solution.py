
maxdepth = 0
def depth(elem, level):
    global maxdepth
    maxdepth=max(maxdepth,level+1)
    for i in elem:
        depth(i,level+1)
    

