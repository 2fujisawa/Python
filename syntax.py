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