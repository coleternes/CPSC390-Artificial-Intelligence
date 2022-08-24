# Group members:
# Andrew Dillon
# Michael Lewson
# Cole Ternes

# References:
# https://github.com/aimacode/aima-python/blob/master/search.ipynb

# Node Class
class Node():
    def __init__(self, state, edgeWeight=0):
        self.state = state # Letter
        self.edgeWeight = edgeWeight # Cost from parent to self
        self.children = []

    # Assigns the child's parent & edgeweight + appends childNode to self.children
    def addChild(self, childNode, edgeWeight):
        childNode.parent = self
        childNode.edgeWeight = edgeWeight
        self.children.append(childNode)

# Tree Class
class Tree():
    def __init__(self):
        self.root = None
        self.path = []
        self.visited = []
        self.destinationFound = False

    # Adds the root to the tree
    def addRoot(self, rootNode):
        self.root = rootNode

    # Adds the childNode to the tree under the parent node
    def addNode(self, childNode, parentNode, edgeWeight):
        parentNode.addChild(childNode, edgeWeight)

    # Depth-first search
    def dfs(self, currNode, destination):
        # Skipping function if destination already found
        if(self.destinationFound):
            return

        # Append the currNode to visited and path
        self.visited.append(currNode.state)
        self.path.append(currNode.state)

        # Check if currNode is the destination
        if(currNode.state == destination.state):
            self.destinationFound = True
            return

        #adding children to frontier
        for n in currNode.children:
            # Recursively search tree
            self.dfs(n, destination)
            # Remove currNode if not in the path
            if(not self.destinationFound):
                self.path.pop()

# Create the tree
tree = Tree()

# Define the nodes
root = Node("S")
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
g = Node("G")

# Adding nodes to tree
tree.addRoot(root)
tree.addNode(a, tree.root, 3)
tree.addNode(b, tree.root, 1)
tree.addNode(c, tree.root, 8)
tree.addNode(d, a, 3)
tree.addNode(e, a, 7)
tree.addNode(g, a, 15)
tree.addNode(g, b, 20)
tree.addNode(g, c, 5)

# Depth-first search through tree
tree.dfs(tree.root, g)

# Print the path and all nodes visited
print("Expanded nodes:\n" + str(tree.visited))
print("Path:\n" + str(tree.path))
