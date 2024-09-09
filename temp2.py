class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        
        if self.key == data:
            return
        
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self,data):
        if self.key == data:
            print("Node is found")
            return
        
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present")

    def preorder(self):
        print(self.key)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
        
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key)
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key)

    def DeleteNode(self,data):
        if self.key is None:
            print("Tree is empty")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.DeleteNode(data)
            else:
                print("Given Node doesn't exist")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.DeleteNode(data)
            else:
                print("Given node doesn't exist")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node = self.lchild
            while node.rchild :
                node = node.rchild
            self.key = node.key
            self.lchild = self.lchild.DeleteNode(node.key)
        return self
    
    def count(node):
        if node is None:
            return 0
        return 1 + count(node.lchild) + count(node.rchild)




    

    
root = BST(20)
List = [10,8,49,40,20,78]
for i in List:
    root.insert(i)

# root.preorder()
# print()
# root.inorder()
print(count(root))
# root.postorder()
root.DeleteNode(40)
# root.inorder()
print(count(root))

