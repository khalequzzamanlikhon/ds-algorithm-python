class Node:
    def __int__(self):
        self.data=None
        self.next=None


def insertAtFront(head_ref,new_data):
    new_node=Node()
    new_node.data=new_data
    new_node.next=head_ref
    head_ref=new_node
    return head_ref

def push(head_ref,new_data):
    new_node=Node()
    new_node.data=new_data
    new_node.next=head_ref
    head_ref=new_node
    return head_ref

def printList(node):
    while node!=None:
        print(node.data,end=" ")
        node=node.next
    print("\n")

if __name__=="__main__":
    head =None
    head=push(head,1)
    head = push(head, 2)
    head = push(head, 3)
    head = push(head, 4)
    head = push(head, 5)
    print("crated linked list :\n")
    printList(head)
    #insert 10 at the front
    head=insertAtFront(head,10)
    print("after inserting {} at the front the new linked list is :".format(10))
    printList(head)
