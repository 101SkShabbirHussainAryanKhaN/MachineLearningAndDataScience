class BinaryTree:
    def __init__(self):
        self.tree = []

    def insert(self, data):
        self.tree.append(data)

    def find_parent(self, index ):
        if index == 0:
            return None
        parent_index = (index - 1)//2
        return self.tree[parent_index]

    def find_children(self, index):
        left_child_ind = 2*index + 1
        right_child_ind = 2*index + 2

        left_child = self.tree[left_child_ind] if left_child_ind < len(self.tree)  else None
        right_child = self.tree[right_child_ind] if right_child_ind < len(self.tree)  else None
        return left_child, right_child


    def find_root(self):
        if len(self.tree) >= 0:
            print("Root is :", self.tree[0])
        else:
            print("The Tree has No Root!")

    def find_leaves(self):
        leaves = []
        for node in self.tree:
            if node is not None:
                index = self.tree.index(node)
                left_child, right_child = self.find_children(index)
                if left_child is None and right_child is None:
                    leaves.append(node)

        if len(leaves) > 0:
            print("The Leaves are: ", leaves)
        else:
            print("There are no Leaves in the Tree:")


tree = BinaryTree()
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.insert(8)
tree.insert(9)
tree.insert(10)
tree.insert(14)
print("Parent of 7 is :",tree.find_parent(7))
left_child, right_child = tree.find_children(2)
print("childrens of 2 is :", left_child, right_child)
tree.find_root()
tree.find_leaves()