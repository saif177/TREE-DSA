from collections import deque
from node import Node

def bfs(root) :
    if root is None :
        return 
    queue = deque([root])
    while queue :
        node = queue.popleft()
        print(node.data)

        if node.left :
            queue.append(node.left)
        if node.right :
            queue.append(node.right)

root = Node('5')

root.insert('1')
root.insert('2')
root.insert('3')
root.insert('6')
root.insert('7')


bfs(root)