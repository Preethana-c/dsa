class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    # Public insert method
    def insert(self, data):
        self.root = self._insert(self.root, data)

    # Recursive insert helper
    def _insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)
        return root

    # Preorder traversal
    def preorder(self):
        self._preorder(self.root)
        print()  # for newline

    def _preorder(self, root):
        if root:
            print(root.data, end=" ")
            self._preorder(root.left)
            self._preorder(root.right)

    # Count good nodes
    def good_nodes(self):
        return self._good_nodes(self.root, float('-inf'))

    def _good_nodes(self, node, max_so_far):
        if node is None:
            return 0
        count = 0
        if node.data >= max_so_far:
            count = 1
        # Update max_so_far for children
        max_so_far = max(max_so_far, node.data)
        count += self._good_nodes(node.left, max_so_far)
        count += self._good_nodes(node.right, max_so_far)
        return count

# Example usage:
t = Tree()
for value in [3, 1, 4, 3, 1, 5]:
    t.insert(value)

print("Preorder traversal:")
t.preorder()
print("Number of good nodes:", t.good_nodes())