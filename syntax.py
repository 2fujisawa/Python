#THIS IS JUST A SPACE FOR ME TO LEARN GENERAL PYTHON SYNTAX AND TO PRACTICE MY CODING SKILLS

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

#tuples - immutable, meaning you cannot change the values in them
def tuples():
    names = ("Linus", "jacob") 
    our_numbers = "2", "24" #you can create tuples without the parenthesis
    print("Your tupes are ", names, " with numbers", our_numbers, " and we sliced through index 1 to the end:", our_numbers[1:]) 

#Dictionaries - unordered collection of data in key:value pairs
def dictionaries():
    empty_dict = {} #creating empty dictionary
    school = {"GPA": 4.0, "Degree": "Computer Science", "Favorite Language": "Python", "Future": "computers"} #creating dictionary
    print("The highest score gpa you can get in school is", school["GPA"]) #you can access the value of the key this way as well however if there is no key it will throw an error
    print("My favorite coding language is", school.get("Favorite Language")) #second method to accessing the value of a key, this will return None if the key does not exist

    school["Future"] = "AI" #changing the value of a key
    print("The future of technology is changing to",school.get("Future"))

#Sets - unordered collection of unique elements
def sets():
    empty_set = set() #creating empty set
    cars = {"Lambo", "Ferrari", "Rolls Royce", "Bently", "Bently"} #creating set
    print("You cannot have duplicate values in sets", cars)  #

    cars.add("Mclaren") #adding element to set
    cars.update(["Tesla","Porsche"])# to add multiple items
    cars.remove("Tesla") #removing element from set
    print("Some set cars you might want in the future are", cars)


def main():
    while True:
        menu = int(input("Please enter a number for the topic you want to output: \n1.Variables and DataTypes \n2.Control Sturctures\n3.Lists\n4.Tuples\n5.Dictionaries\n6.Sets\n7.Stop Script\n")) #have to convert to integer to correctly process the string
        if (menu == 1):
            print("Welcome to Variables and Data Types!")
            variables_datatypes()
        elif (menu == 2):
            print("Welcome to Control Structures!")
            control_structures()
        elif (menu == 3):
            print("Welcome to Lists!")
            user_input = input("Enter a list of elements separated by commas: ")
            user_list = user_input.split(",") #splitting user input into a list
            print("Your list is: ", user_list)
            list_syntax(user_list)
        elif(menu == 4):
            print("Welcome to Tuples!")
            tuples()
        elif(menu == 5):
            print("Welcome to Dictionaries!")
            dictionaries()
        elif(menu == 6):
            print("Welcome to Sets!")
            sets()
        elif(menu == 7):
            print("Goodbye!")
            break # break the loop closing program
        else: 
            print("Invalid input")
            continue # this is will restart the look until a valid input is entered
        

if __name__ == "__main__":
    main() #calling the main function