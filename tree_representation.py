class Node :
    #constructure
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
    
    #insert data
    def insertNode(self, data):
        if self.data :
            if data < self.data :
                if self.left is None :
                    self.left = Node(data)
                else :
                    self.left.insertNode(data)
            elif data > self.data :
                if self.right is None :
                    self.right = Node(data)
                else :
                    self.right.insertNode(data)
        else :
            self.data = data
    
    #print node data using in-order travesal
    def printNode(self) : 
        if self.left :
            self.left.printNode()
        print(self.data)
        if self.right :
            self.right.printNode()


root = Node(5)
root.insertNode(1)
root.insertNode(6)
root.insertNode(2)
root.insertNode(7)

root.printNode()
