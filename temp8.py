class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def Print_LL(self):
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    def Add_Begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def Add_End(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    def After_Node(self,data,x):
        New_Node = Node(data)
        n = self.head
        while n.ref != None:
            if(n.data != x):
                n = n.ref
            else:
                break
        New_Node.ref = n.ref
        n.ref = New_Node
    
    def Before_Node(self,data,x):
        New_Node = Node(data)
        n = self.head
        k = Node
        while n.ref != None:
            if n.data != x:
                k = n
                n = n.ref
            else:
                break
        New_Node.ref = n
        k.ref = New_Node
    
    def Delete_Begin(self):
        if self.head != None:
            self.head = self.head.ref
        else:
            print("Empty LL")
    
    def Delete_Last(self):
        n = self.head
        k = None
        while n.ref != None:
            k = n
            n = n.ref
        k.ref = None
    
    def Delete_Given(self,value):
        n = self.head
        k = None
        while n.ref != None:
            if(n.data != value):
                k = n
                n = n.ref
            else:
                break
        k.ref = n.ref
        
 

LL1 = LinkedList()
LL1.Print_LL()
LL1.Add_Begin(30)
LL1.Add_Begin(20)
LL1.Add_Begin(10)
LL1.Add_End(100)
LL1.Add_End(300)
LL1.After_Node(200,100)
LL1.After_Node(400,300)
LL1.Before_Node(350,400)
LL1.Before_Node(50,100)
# LL1.Delete_Begin()
# LL1.Delete_Begin()
# LL1.Delete_Last()
LL1.Delete_Given(100)
LL1.Print_LL()