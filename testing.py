# a regular class called Person
class Person:                    

    def get_name(self):
        return "Joseph"

# a class that inherits from Person
class Student(Person):

    def get_number(self):
        return "0123456789"
    
# the student instance automatically has the get_name() method!
student = Student()
name = student.get_name()
number = student.get_number()
print(f'Name: {name} | Number: {number}')
