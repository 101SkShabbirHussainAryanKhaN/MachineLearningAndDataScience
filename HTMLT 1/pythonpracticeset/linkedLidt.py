class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
                current.next = newNode
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

    def display(self):
        current = self.head
        while (current is not None):
            print(current.data)
            current =current.next

    def search(self,data):
        current = self.head
        while (current is not None):
            if current.data == data:
                return True
            current =current.next
        return False

    def delete_list(self):
        self.head = None

twoD = LinkedList()
twoD.insert(12)
twoD.insert(34)
twoD.insert(56)
twoD.insert(67)
twoD.insert(12)
twoD.insert(34)
twoD.insert(56)
twoD.insert(67)
twoD.insert(12)
twoD.insert(34)
twoD.insert(56)
twoD.insert(67)
twoD.insert(12)
twoD.insert(34)
twoD.insert(56)
twoD.insert(67)
twoD.display()



