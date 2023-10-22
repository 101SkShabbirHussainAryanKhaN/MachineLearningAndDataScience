class Node:
    def __init__(self , data = None):
        self.data = data
        self. next = None

    def linklist(matrix):
        sentinel = Node()
        current = sentinel
        for row in  matrix:
            for col in row:
                newNode = Node(col)
                current.next = newNode
                current = current.next
        return sentinel.next

    def showitem(head):
        while head is not None:
            print(head.data, end=' ')
            head = head.next
        print()
    
    if __name__ == "__main__":
    
        matrix = [[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12]]

        head = linklist(matrix)

        showitem(head)