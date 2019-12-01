1)Create a Python class called "Student" having "name","age" as attribute along with a list having the marks obtained for three subjects.
2)Create a constructor to initialize two objects of this class.
3)Create a member function called 'display' printing the details of a specific object.
4)Ask user to enter the values for an object through an 'accept' member function.
5)Display these details


class Student:
    def __init__(self):
        self.name=0
        self.age=0
    def display(self):
        print(self.name)
        print(self.age)
        print(self.marks)
    def accept(self):
        self.marks = input("Enter marks")
        self.marks=list((self.marks.split(' ')))
        name=input("Enter name")
        age=input("Enter age")

        self.name=name
        self.age=age

p1=Student()
p1.accept()
p1.display()
