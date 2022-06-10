import re

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self) -> str:
        return "Self:{V}, (L:{ L}, R:{ R}".format(V=self.value, L=str(self.left), R=str(self.right))

#  (5 (4 (11 (7 () ()) (2 () ()) ) ()) (8 (13 () ()) (4 () (1 () ()) ) ) )
# treeString = treeString[1:-1].strip().strip('\n')
def parse(treeString : str):
    print(treeString)
    if treeString == "()" or treeString == "":
        return None
    n = Node(treeString[0])
    treeString = treeString[1:-1]

    (i,j) = BracketGroup(treeString)
    (f,k) = BracketGroup(treeString[j:])

    n.left = parse(treeString[i:j])
    n.right = parse(treeString[j:][f:k])

    return n

def BracketGroup(string: str):
    brackets = 0
    i = 0
    j = 0
    for c,char in enumerate(string): # hello -> [(0,h), (1,e), (2,l)..]
        if char == "(":
            if brackets == 0:
                i = c
            brackets += 1
        if char == ")":
            brackets -= 1
            if brackets == 0:
                j = c
    return (i,j+1)


# def main(treeString):
#     treeString = treeString[1:-1].replace(" ","").replace("\n", "")
#     print(treeString)
#     tree = parse(treeString)
#     print()

# main("(5 (4 (11 (7 () ()) (2 () ()) ) ()) (8 (13 () ()) (4 () (1 () ()) ) ) )")

# When there's a number outside a bracket, add to the numbers inside the bracket. (or put inside the empty bracket)