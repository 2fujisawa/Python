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


