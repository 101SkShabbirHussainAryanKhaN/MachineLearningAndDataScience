class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Linklist:
    def __init__(self):
        self.head = None

        # Adding data elements
    def insert(self, val):
        newNode = Node(val)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    def delete(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        
        else:
            current = self.head

            while current.next is not None:
                if current.next.data == data:
                  current.next = current.next.next
                  return 
                else:
                    current = current.next   
        
    def display(self , node):
        while (node is not None):
            print(node.data)
            last = node
            node = node.next

twoD = Linklist()
twoD.insert(12)
twoD.insert(10)
twoD.insert(56)
twoD.insert(67)
twoD.insert(12)
twoD.insert(34)
twoD.delete(10)


twoD.display(twoD.head)
