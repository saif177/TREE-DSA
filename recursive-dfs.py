from node import Node

#alternative method
def dfs(root) :
    if root is None :
        return
    print(root.data)
    
    if root.left :
        dfs(root.left)

    if root.right :
        dfs(root.right)

root = Node('5')

root.insert('1')
root.insert('2')
root.insert('3')
root.insert('6')
root.insert('7')

dfs(root)
#root.DFS()
