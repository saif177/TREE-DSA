from node import Node

#tree traversal using DFS
def dfs(root) :
    if root is None :
        return
    
    st = [root]
    while st :
        node  = st.pop()
        print(node.data)
        if node.left :
            st.append(node.left)
        if node.right :
            st.append(node.right)

    

root = Node('a')
root.insert('b')
root.insert('c')
root.insert('d')
root.insert('e')
root.insert('f')

Node.dfs(root)