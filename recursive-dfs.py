class Node :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    
    def insert(self, data) :
        if self.data :
            if data > self.data :
                if self.right is None :
                    self.right = Node(data)
                else :
                    self.right.insert(data)

            elif data < self.data :
                if self.left is None :
                    self.left = Node(data)
                else :
                    self.left.insert(data)
        else :
            self.data = data

    #tree traversal using DFS
    def DFS(self) :
        if self.data is None :
            return
        print(self.data)

        if self.left : 
            self.left.DFS()
        if self.right : 
            self.right.DFS()


#alternative method
# def dfs(root) :
#     if root is None :
#         return
#     print(root.data)
    
#     if root.left :
#         dfs(root.left)

#     if root.right :
#         dfs(root.right)

root = Node('5')

root.insert('1')
root.insert('2')
root.insert('3')
root.insert('6')
root.insert('7')

#dfs(root)
root.DFS()
