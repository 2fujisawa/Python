#THIS IS JUST A SPACE FOR ME TO LEARN GENERAL PYTHON SYNTAX 
print("Welcome to my Python Syntax Learning Space")

#BASIC SYNTAX

#Variables and Data Types
def variables_datatypes():
    age = 22 #int
    name = "Linus" #string
    is_student = True #boolean
    pi = 3.1415 #float
    favorite_letter = "L" #char
    print("My name is " + name + " and I am " + str(age) + " years old.") #str() converts int to string because you can't concatenate(link) int and string
    print(f"My favorite letter is {favorite_letter} and the short formula for pi is {pi}") #f-string formatting

#CONTROL STRUCTURES 
def control_structures():
    test_input = input("Enter yes if you want to see how the conditional statements work no if you want to skip: ") #taking in an input

    #Conditional Statements

    #if, elif, and else Statements
    if test_input.lower() == "yes":
        print("You are continuing with the conditional statements!")
    elif test_input.lower() == "no":
        return #exits the function, you would use break to exit a loop
    else:
        print("Invalid input")

    #Loops(for and while)
    input_number = int(input("Enter a number to see how the for loops work: ")) #taking in an input
    for i in range(input_number): #prints numbers from 0 to input_number
        print(i)
    for l in "loop": #prints each letter in the string
        print(l, end="")
    print() # this print statement is needed to create a new line

    #Testing the while loop
    length = "Length of the while loop"
    count = 0
    while count < len(length): #loops through the length of the string starting from 0
        print(length[count], end="")
        count += 1


#Core Data Structures used in Python
def list_syntax(user_list):
    
    #Lists
    new_list = user_list #creating a list from user input
    print(new_list[0], " - printing first element in list") #accessing first elemnt in list(remember it start from the 0 )

    new_list.append("appended element") #adding element to end of list
    new_list.insert(1,"inserted element at index 1") #inserting element at index 1
    print(new_list)

    popped_variable = new_list.pop() # removes the the last element and creates a return value
    new_list.remove(new_list[0]) #removes whatever gets defined in the parenthesis, Remember you cannot index using .remove method, you must use pop
    print(new_list)

    test_list2 = [] #empty list
    test_list2.append(popped_variable) #appends the last element in the list as it was popped
    print(test_list2, " - popped element")

#tuples 
names = ("Linus", "jacob") #tuples are immutable, meaning you cannot change the values in them
our_numbers = "2", "24" #you can create tuples without the parenthesis
print(names, our_numbers, our_numbers[1:]) # the last portion just slices the tuple from index 1 to the end

#Dictionaries
empty_dict = {} #creating empty dictionary
family = {"Mom": "Akiko", "Dad": "Ted", "Older Brother": "John", "Friend": "Sean"} #creating dictionary
print(family["Mom"]) #you can access the value of the key this way as well however if there is no key it will throw an error
print(family.get("Mom")) #second method to accessing the value of a key, this will return None if the key does not exist

family["Friend"] = "Jacob" #changing the value of a key
print(family.get("Friend"))

#Sets - unordered collection of unique items - They are good for mathematical operations like union, intersection, difference, and symmetric difference
empty_set = set() #creating empty set
fruits = {"apple", "banana", "orange", "apple"} #creating set
print(fruits) #second apple is not printed because sets do not allow duplicates

fruits.add("grape") #adding element to set
fruits.update(["grape","mango"])# to add multiple items
fruits.remove("banana") #removing element from set

print(fruits)




menu = int(input("Please enter a number for the topic you want to output: ")) #have to convert to integer to correctly process the string
if (menu == 1):
    print("Variables and Data Types")
    variables_datatypes()
elif (menu == 2):
    print("Control Structures")
    control_structures()
elif (menu == 3):
    print("List Syntax")
    user_input = input("Enter a list of elements separated by commas: ")
    user_list = user_input.split(",") #splitting user input into a list
    print("Your list is: ", user_list)
    list_syntax(user_list)