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
    def greet(self):
        return (f"Hello my name is {self.name} and I am {self.age} years old. I am a student: {self.is_student}")
    

def main():
# Object - Instance of the class
    #Creating object of the class 
    firstperson = Person(name = "Linus", age = 22, is_student = True) #You need to declare all of the attributes in the object
    print(firstperson.greet())

if __name__ =="__main__":
    main()

