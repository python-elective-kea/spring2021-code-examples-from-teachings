class Person:

    spicies = 'Mammal' # class varible

    def __init__(self, *args):
        
        if len(args) == 1:
            self.name = args[0] # instance variable
        
        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]

    def name_age(self):
        return self.name + ' ' + self.age
 

class Instructor:
    def __init__(self, course):
        self.course = course




class Student(Person, Instructor):
    def __init__(self, name, course):
        Person.__init__(self, name)
        Instructor.__init__(self, course)
        # super().__init__(name)



