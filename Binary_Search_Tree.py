'''
    Implementing a Binary search tree Using Pyhon programming language
'''

class Node():
    def __init__(self, data = None):
        self.data  = data
        self.right = None
        self.left  = None
'''
Implementing a Linked List In Python

class Linked_list():
    def __init__(self, data = None):
        self.head = Node(data)
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node
    def print_list(self):
        temp = self.head
        while temp.next != None:
            temp = temp.next
            print(temp.data, '-->', end = '')
        #print(temp.data)
    def elements (self):
        temp = self.head
        ele = []
        while temp.next != None:
            temp = temp.next
            ele.append(temp.data)
        return ele
        '''

class Binary_tree():
    
    #init is a constructur that calls when an instance of structure is created
    
    def __init__(self, head_val= None ):
        self.head = Node(head_val)  
        
    #insert method is used to insert a Node according to the proporty of Binary search tree  
        
    def insert(self, value):

        def add(value, phead):
            if value >= phead.data:
                if phead.right!= None:
                    add(value, phead.right)
                else:
                    new = Node(value)
                    phead.right = new
            else:
                if phead.left!= None:
                    add(value, phead.left)
                else:
                    new = Node(value)
                    phead.left = new
                    
        if self.head.data == None:
            self.head.data = value
            return
        #new_node = Node(value)
        elif value >= self.head.data:
            if self.head.right != None:
                phead = self.head.right
                add(value, phead)
            else:
                new = Node(value)
                self.head.right = new
        else:
            if self.head.left != None:
                phead = self.head.left
                add(value, phead)
            else:
                new = Node(value)
                self.head.left = new
    
    '''
           Tree Traversals 
           1. Inorder
           2.Preorder
           3.Postorder
    '''
    def pre_order(self,phead = None):
        if phead:
            print (phead.data)
            self.pre_order(phead.left )
            self.pre_order(phead.right)
            
    def in_order(self, phead ):
        #temp = 
        if phead:
            self.in_order(phead.left)
            print(phead.data)
            self.in_order(phead.right)
            
    def post_order(self, phead):
        if phead:
            self.post_order(phead.left)
            self.post_order(phead.right)
            print(phead.data)
            
    '''
    def add(self, value, phead):
        if value >= phead.data:
            if phead.right!= None:
                add(value, phead.right)
            else:
                new = Node(value)
                phead.right = new
        else:
            if phead.left!= None:
                add(value, phead.left)
            else:
                new = Node(values)
                phead.left = new
    def print_elements(self):
        temp = self.head
        
            
    

l = Linked_list()
l.insert(10)
l.insert(20)
l.insert(30)
l.insert(40)

l.print_list()
print(l.elements())
'''
