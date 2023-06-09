from sys import maxsize  #returns empty when stack is empty
#create a stack
def createStack():
    stack=[]
    return stack
#stack is empty when stack size is zero
def isEmpty(stack):
    return len(stack)==0

#function to add an item
def push(stack,item):
    stack.append(item)
    print(item," pushed to stack")

#function to remove an item
def pop(stack):
    #check if stack has items
    if isEmpty(stack):
        return str(-maxsize -1) #return minus infinite
    return stack.pop()
#funciton to remove the top item from the stack
def peek(stack):
    #check if stack has value
    if isEmpty(stack):
        return str(-maxsize -1)
    return stack[len(stack)-1]

#driver program to test the above program
stack=createStack()
push(stack,str(10))
push(stack,str(20))
push(stack,str(30))
print(pop(stack),"popped from stack")
#check if stack is empty
if isEmpty(stack):
    print("the stack is empty")
else:
    print("the values in the stack are: \n")
    while not(isEmpty(stack)):
        print(peek(stack),end=" ")
        pop(stack)


