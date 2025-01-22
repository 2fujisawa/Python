#OOP - Programming paradigm to model real world entities as object in code.
# Class - Blueprint

class Person: #when creating an class you also have to create object which you must initialize

    #Class Variable
    gender = "male" #this is a class variable, it is shared by all instances of the class

    def __init__(self, name, age, is_student): #this is the constructor method, it initializes the object(sets the attributes)
        #Instance Variables - maintains the state of multiple different objects(can easily manage the state of an object)
        self.name = name
        self.age = age
        self.is_student = is_student

    #Instance Method
    def greet(self): #the self is needed in the parameter so the method knows which object to work with
        return (f"Hello my name is {self.name} and I am {self.age} years old. I am a student: {self.is_student}")
    
'''
Inhertiance - Mechanism to define a new class based on an existing class
    - allows you to create a new class that inherits attributes and methods from a existing class(subclasses and superclasses)
'''

class Student(Person): #Student class inherits from Person class
    def __init__(self,name, age, is_student, student_id):
        self.student_id = student_id
        super().__init__(name, age, is_student) #super() method is used here to call in the constuctor of the person class so you dont have to redefine the instance variables

    def greet_as_student(self):
        return(f"{self.greet()} My student id is {self.student_id}") #greet has () since it is a method





def main():
# Object - Instance of the class
    #Creating object of the class, instantiating the class
    firstperson = Person(name = "Linus", age = 22, is_student = True) #You need to declare all of the attributes in the object
    print(firstperson.greet())

    secondperson = Person(name = "John", age = 27, is_student = False)
    print(secondperson.greet())

    #Accessing class variable - so we can see that class variables are used to store data that is shared by all instances of the class as to instance variables that are unique to each instance of the class
    print(f"{firstperson.name}'s gender is {firstperson.gender}") 
    print(f"{secondperson.name}'s gender is {secondperson.gender}")

    firststudent = Student(name = "Jacob", age = 22, is_student = True, student_id = 1234)
    print(firststudent.greet_as_student())


if __name__ =="__main__":
    main()

