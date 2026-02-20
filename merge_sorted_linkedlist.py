def merge_sorted_linkedlist(head1,head2):
    currentnode1=head1
    currentnode2=head2
    if not head1:
        return head2
    if not head2:
        return head1
    if not head1 and not head2:
        return None
    if head1.data<head2.data:
        mergedhead=head1
        currentnode1=head1.next
    else:
        mergedhead=head2
        currentnode2=head2.next
    currentmergednode=mergedhead
    #print("first merged head node",currentmergednode.data)
   
    
    while currentnode1 and currentnode2:
        print("current node l1 ")
        print(currentnode1.data)
        print("current node  l2 ")
        print(currentnode2.data)
        print("merged list current node ")
        print(currentmergednode.data)
        
        if currentnode1.data<currentnode2.data:
            currentmergednode.next=currentnode1
            currentnode1=currentnode1.next
            '''print(currentmergednode.data)'''
        else:
            currentmergednode.next=currentnode2
            currentnode2=currentnode2.next
        currentmergednode=currentmergednode.next
    if currentnode1 is None:
        currentmergednode.next=currentnode2
    else:
        currentmergednode.next=currentnode1
        
    return mergedhead
            
        

   


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def traverse(head):
    currentnode=head
    while currentnode:
        print(currentnode.data)
        currentnode=currentnode.next

nodeone1=Node(2)
nodeone2=Node(3)
nodeone3=Node(7)           
nodeone4=Node(9)
#nodeone5=Node(12)       
#nodeone6=Node(16)
nodeone1.next=nodeone2
nodeone2.next=nodeone3
nodeone3.next=nodeone4
#nodeone4.next=nodeone5
#nodeone5.next=nodeone6

nodetwo1=Node(1)
nodetwo2=Node(5)    
nodetwo3=Node(6)
nodetwo4=Node(10)
nodetwo1.next=nodetwo2
nodetwo2.next=nodetwo3
nodetwo3.next=nodetwo4

currenthead=merge_sorted_linkedlist(nodeone1,nodetwo1)
#print(traverse(nodeone1))
#print(traverse(nodetwo1))
print("resultant merged linked list")
print(traverse(currenthead))



    

'''2 3 7 9
4 5 6 8 10'''
