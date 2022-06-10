import re

"""
Thought about doing a Depth-First-Search with Heuristics with a node class.

Realised that if I had the same tree for multiple searches that might been better,
but since we have to construct the tree anyway, better to use the given format and work out
solution from there.


"""

# Example input
# 22  (5 (4 (11 (7 () ()) (2 () ()) ) ()) (8 (13 () ()) (4 () (1 () ()) ) ) )

leaf = re.compile("\(\)")
parent = re.compile("\(\d+")
close = re.compile("\)")


def find(treeString: str, goal: int):
    treeString = treeString.replace(" ", "").replace("\n", "")
    path = [] # Path leading to current node
    pathSum = 0 # Sum of numbers in said path

    i = 0 # Current index in treestring
    while i < len(treeString)-1:
        string = treeString[i:]
        p = re.match(parent, string) # Match for parent?
        l = re.match(leaf, string) # Match for leaf?
        cl = re.match(close, string) # Match for close bracket?
        if p != None: # For parent nodes
            length = p.span()[1] # length is index of last character of match
            path.append(int(string[1:length])) # Add the number to the path
            pathSum += path[-1] # Update path sum
            i += length # Set index to end of parent
        elif l != None: # For leaf nodes
            length = l.span()[1]
            if pathSum == goal: # Got to a leaf node, is the current sum the goal?
                return True
            i += length # Set index to end of leaf
        elif cl != None: # For close bracket
            length = cl.span()[1]
            pathSum -= path.pop() # Remove from path as we traverse up the tree and update path sum.
            i += length
    
    return False # goal was never equal the path sum at a leaf node


def parse(filename: str): # Returns a list of (int, str) pairs
    pairs = []
    with open(filename, "r") as file:
        openB = 0 # Number of open brackets so far
        closeB = 0 # Number of close brackets so far
        treeSoFar = '' # Initialise variable for tree string so far in a multiline pair
        goal = 0 # Initialise variable for target number of tree in multiline pair
        for line in file.readlines(): # Iterating through lines in test cases doc   
            if openB == 0 and closeB == 0 and line.count("(") == line.count(")"): # Two conditions in case that open and closed bracket count is equal on a line in the middle of the tree
                sep = line.find(" ") # Assumes always a space between target number and tree                                             
                pairs.append((int(line[:sep]),line[sep+1:])) # goal, tree
            
            elif openB == 0: # If instead the first line is unbalanced
                sep = line.find(" ")                                              
                goal = line[:sep] # Extract target number

                treeSoFar = line[sep+1:] # Now need to consider the next lines to complete the tree
                openB += line.count("(") # Now on next iteration, will go to else condition
                closeB += line.count(")")

            else: # Tree spilling over from line above
                treeSoFar += line
                openB += line.count("(")
                closeB += line.count(")")
                if openB == closeB: # Found complete tree
                    pairs.append((int(goal), treeSoFar))
                    openB, closeB, goal = 0,0,0 # Reset prior to moving on to next line which will be a new test case
                    treeSoFar = ''
    
    return pairs


def main(filename: str):
    for goal, treeString in parse(filename):
        print(goal, treeString)
        if find(treeString, goal):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main("TestCases.txt")
    #print(re.match(parent, "(5(2()()))").span())
