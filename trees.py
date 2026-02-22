class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    # ---------------- INSERT ----------------
    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)

        return root

    # ---------------- PREORDER ----------------
    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, root):
        if root:
            print(root.data, end=" ")
            self._preorder(root.left)
            self._preorder(root.right)

    # ---------------- DELETE ----------------
    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, root, data):
        if root is None:
            return root

        # Search for node
        if data < root.data:
            root.left = self._delete(root.left, data)

        elif data > root.data:
            root.right = self._delete(root.right, data)

        else:
            # Case 1: No child
            if root.left is None and root.right is None:
                return None

            # Case 2: One child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: Two children
            min_larger_node = self._get_min(root.right)
            root.data = min_larger_node.data
            root.right = self._delete(root.right, min_larger_node.data)

        return root

    def _get_min(self, root):
        while root.left:
            root = root.left
        return root


# ---------------- TESTING ----------------
if __name__ == "__main__":
    t = Tree()

    t.insert(50)
    t.insert(30)
    t.insert(70)
    t.insert(20)
    t.insert(40)
    t.insert(60)
    t.insert(80)

    print("Preorder traversal:")
    t.preorder()

    print("\nAfter deleting 30:")
    t.delete(30)
    t.preorder()