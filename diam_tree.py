class Treenode:
    def __init__(self,val):
        self.val=val 
        self.right=None
        self.left=None
def buildTreenode(arr,i=0):
    if i>=len(arr) or arr[i] is None:
        return None
    node=Treenode(arr[i])
    node.left=buildTreenode(arr,2*i+1)
    node.right=buildTreenode(arr,2*i+2)
    return node

def preorder(root):
    if root is None:
        return 
    print(root.val,end=" ")
    preorder(root.left)
    preorder(root.right)

arr=[1,2,3,4,5,None,6]
root=buildTreenode(arr)
preorder(root)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val,end=" ")
    inorder(root.right)

inorder(root)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val,end=" ")

postorder(root)

from collections import deque


def levelOrder(root):
    if root is None:
        return
    q=deque([root])
    while q:
        node=q.popleft()
        print(node.val,end=" ")
        if node.left:   
            q.append(node.left)         
        if node.right:
            q.append(node.right)    

levelOrder(root)

def height(root):
    if root is None:
        return -1


    lHeight = height(root.left)
    rHeight = height(root.right)

    return max(lHeight, rHeight) + 1

print(height(root))

def getLevel(root,target,level):
    if root is None:
        return -1
    if root.val==target:
        return level
    leftLevel=getLevel(root.left,target,level+1)
    if leftLevel!=-1:
        return leftLevel
    return getLevel(root.right,target,level+1)
print("Level of 5:", getLevel(root,5,0))


def ifNodeExists(root,key):
    if root is None:
        return False
    if root.val==key:
        return True
    res1=ifNodeExists(root.left,key)
    if res1:
        return True
    res2=ifNodeExists(root.right,key)
    return res2
print("Node exists:", ifNodeExists(root,5))