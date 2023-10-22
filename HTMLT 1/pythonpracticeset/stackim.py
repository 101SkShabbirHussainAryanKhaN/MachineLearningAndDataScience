class Stack:
    def __init__(self):
        self.items =[]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

st = Stack()
st.push(1)
st.push(3)
st.push(5)
print(st.pop())
print(st.pop())
print(st.pop())
print(st.pop())