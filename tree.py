from collections import deque


class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def buildTree(arr):

    if not arr:
        return None

    root = TreeNode(arr[0])

    queue = deque([root])

    i = 1

    while queue and i < len(arr):

        current = queue.popleft()

        if i < len(arr) and arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)

        i += 1

        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)

        i += 1

    return root


def inorder(node):

    if node is None:
        return

    inorder(node.left)
    print(node.val, end=" ")
    inorder(node.right)


def preorder(node):

    if node is None:
        return

    print(node.val, end=" ")
    preorder(node.left)
    preorder(node.right)


def postorder(node):

    if node is None:
        return

    postorder(node.left)
    postorder(node.right)
    print(node.val, end=" ")


def levelorder(root):

    if root is None:
        return

    queue = deque([root])

    while queue:

        node = queue.popleft()

        print(node.val, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


def height(node):

    if node is None:
        return 0

    left = height(node.left)

    right = height(node.right)

    return 1 + max(left, right)


arr = input("Enter tree array: ").split()

for i in range(len(arr)):

    if arr[i] == "None":
        arr[i] = None

    else:
        arr[i] = int(arr[i])

root = buildTree(arr)

print("\nInorder Traversal:")
inorder(root)

print("\n\nPreorder Traversal:")
preorder(root)

print("\n\nPostorder Traversal:")
postorder(root)

print("\n\nLevel Order Traversal:")
levelorder(root)

print("\n\nHeight of Tree:")
print(height(root))