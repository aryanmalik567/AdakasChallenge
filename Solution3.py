import re

# Example input
# 22  (5 (4 (11 (7 () ()) (2 () ()) ) ()) (8 (13 () ()) (4 () (1 () ()) ) ) )

leaf = re.compile("\(\)")
parent = re.compile("\(\d+")
close = re.compile("\)")


def accumulatePath(treeString: str):
    treeString = treeString.replace(" ", "").replace("\n", "")
    path = []
    pathSum = 0
    results = set()

    i = 0
    while i < len(treeString)-1:
        string = treeString[i:]
        p = re.match(parent, string)
        l = re.match(leaf, string)
        cl = re.match(close, string)
        if p != None: # For parent nodes
            _, end = p.span()
            path.append(int(string[1:end]))
            pathSum += path[-1]
            i += end
        elif l != None: # For leaf nodes
            _, end = l.span()
            results.add(pathSum)
            i += end
        elif cl != None:
            _, end = cl.span()
            pathSum -= path.pop()
            i += end
    
    return results

if __name__ == "__main__":
    print(accumulatePath("(5 (4 (11 (7 () ()) (2 () ()) ) ()) (8 (13 () ()) (4 () (1 () ()) ) ) )"))
    #print(re.match(parent, "(5(2()()))").span())
