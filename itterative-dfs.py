class Node :
    def __init__(self, data) :
        self.data = data
        self.right = None
        self.left = None
    
    def insert(self, data) :
        if self.data :
            if data < self.data :
                if self.left is None :
                    self.left = Node(data)
                else :
                    self.left.insert(data)

            elif data > self.data :
                if self.right is None :
                    self.right = Node(data)
                else :
                    self.right.insert(data)
        else :
            self.data = data

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