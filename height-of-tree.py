from node import Node

def getTreeHeight(node) :
    if node is None :
        return 0
    
    lDepth = getTreeHeight(node.left)
    rDepth = getTreeHeight(node.right)

    if lDepth > rDepth :
        return lDepth + 1
    else :
        return rDepth + 1


root = Node('5')

root.insert('1')
root.insert('2')
root.insert('3')
root.insert('6')
root.insert('7')
root.insert('8')
root.insert('9')
root.insert('4')
root.insert('11')
root.insert('12')

print(getTreeHeight(root))