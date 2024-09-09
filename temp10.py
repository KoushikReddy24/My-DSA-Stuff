class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def InsertNode(self,data):
        if self.key is None:
            self.key = data
            return
        
        if self.key == data:
            return
        
        if self.key > data:
            if self.lchild:
                self.lchild.InsertNode(data)
            else:
                self.lchild = BST(data)

        elif self.key < data:
            if self.rchild:
                self.rchild.InsertNode(data)
            else:
                self.rchild = BST(data)
    
    def InOrder(self):
        if self.lchild:
            self.lchild.InOrder()
        print(self.key)
        if self.rchild:
            self.rchild.InOrder()

    def DeleteNode(self,data):
        if self.key is None:
            print("Tree is empty")
        
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.DeleteNode(data)
            else:
                print("node doesn't exist")

        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.DeleteNode(data) 
            else:
                print("node doesn't exist")

        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp

            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp

            n = self.lchild
            while n.rchild:
                n = n.rchild
            
            self.key = n.key
            self.lchild = self.lchild.DeleteNode(n.key)
        return self
        

root = BST(20)
root.InsertNode(10)
root.InsertNode(30)
root.InsertNode(40)
root.InsertNode(0)

root.InOrder()
root.DeleteNode(20)
print()
root.InOrder()
