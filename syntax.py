#THIS IS JUST A SPACE FOR ME TO LEARN GENERAL PYTHON SYNTAX 
print("Welcome to my Python Syntax Learning Space")

#BASIC SYNTAX

#Variables and Data Types
age = 22 
name = "Linus" 
is_student = True
print("My name is " + name + " and I am " + str(age) + " years old.") #str() converts int to string because you can't concatenate(link) int and string

#User Input
verify = input("Are you Linus? (yes/no): ")

#CONTROL STRUCTURES 

#if, elif, and else Statements
if verify.lower() == "yes":
    print("You are Linus")
elif verify.lower() == "no":
    print("You are not Linus")
else:
    print("Invalid input")

#Loops(for and while)
for i in range(3): #prints 0 to 2 through iteration
    print(i)
for l in "printing": #prints each letter in Linus
    print(l, end="")
print()

length = "Length of the while loop"
count = 0
while count < len(length):
    print(length[count], end="")
    count += 1

#Core Data Structures used in Python

#Lists
test_list1 = [1,"This element is being accessed",True,3.1415] #creating list
print(test_list1)
print(test_list1[1]) #accessing elemnts in list(remember it start from the 0 )

test_list1.append("final element") #adding element to end of list
test_list1.insert(1,"inserted element") #inserting element at index 1
print(test_list1)

popped_variable = test_list1.pop() # removes the the last element and creates a return value
test_list1.remove("This element is being accessed") #removes whatever gets defined in the parenthesis, Remember you cannot index using .remove method, you must use pop
print(test_list1)

test_list2 = []
test_list2.append(popped_variable) #appends the last element in the list as it was popped
print(test_list2)