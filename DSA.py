#Arrays as a Python Lists
'''
- In python, lists acts as arrays also known as dynamic arrays since python doesnt have a built in array data structure
- Can contain different data types
- Can be resized

'''

#Arrays as a Module
'''
- If you bring in the array module you can create arrays that are more efficient than lists
- They are not as flexible as lists and not homogeneous therefore you can only store one data type in an array
- However, it is more efficient in terms of memory and performance

Ex. import array
'''

#Time Complexity for arrays
'''
- Accessing a element by an index - O(1)
- Inserting an element at the middle of the array - O(n)
- Deleting an element at the middle of the array - O(n)

'''

#Example of an array
array1 = [1,2,3,4,5]
print("The first element in the array is", array1[0])#Accessing an element in the array

array1.insert(2, 100)#Inserting an element in the middle of the array O(n)
print(array1[2])

#Both of these operations are O(n) since you have to shift the elements in the array
array1.remove(100)#Deleting an element specified by he value
del array1[2]#Deletes he element using the index value

print(array1)


#Stacks - Linear data structure that follows the Last In First Out (LIFO) principle
'''
Push: Add a element to the top of the stack
Pop: Remove the top element from the stack
Peek: Return the top element of the stack without removing it

Time Complexity for Stacks
- Accessing an element by an index - O(n)
- Inserting an element at the middle of the stack - O(1)
- Deleting an element at the middle of the stack - O(1)

'''

class Stack: 
    def __init__(self): #Constuctor method, the self parameter allows the object to refer to itself so that instead of the class variabe being shared by all instances of the class it is unique to each instance of the class
        self.items = [] #Creating a list to store the elements in the stack

    def push(self, item): #Method to add a element to the top of the stack
        self.items.append(item)

    def pop(self): #Method to remove the top element from the stack
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]#return the top element of the stack without removing it'
    
    def is_empty(self): #checks if the stack is empty
        return len(self.items) == 0
    
stack1 = Stack() #Making object for the stack class

stack1.push(1)#Adding first elements to the stack with runtime of O(1)
print("The top element currenly in the stack is", stack1.peek())
print("The stack is empty True or False:", stack1.is_empty()) #Checking if the stack is empty with runtime of O(1) - should be false

stack1.push(2)
stack1.push(3)
print("The top element currenly in the stack is", stack1.peek()) #checking the top element of the stack without removing it with runtime of O(1) - should be 3

stack1.pop() #Removes the top element of the stack with runtime of O(1)
print("The top element currenly in the stack is", stack1.peek())





#Linked Lists
'''
Linear data stucture where the elements are called nodes and are connected by pointers.
- Each node contains data and a reference to the next node in the sequence
- Two main types of linked lists
        1. Single Linked Lists 
        2. Double Linked Lists
'''
#Time Complexity for Linked Lists
'''
Accessing an element by an index - O(n)
Inserting an element at the middle of the linked list - O(1)
Deleting an element at the middle of the linked list - O(1)

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #Inserting a node at the beginning of the linked list
    def inserting_node(self,data):
        new_node = Node(data)
        new_node.next = self.head #the new node is pointing to the head of the linked list


