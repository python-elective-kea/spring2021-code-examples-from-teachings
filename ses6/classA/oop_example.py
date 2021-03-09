class Person:
    
    spicies = 'Mammal' # class variable

    def __init__(self, *args):
        #self.name = name      # instance variable
        
        if len(args) == 1:
            self.name = args[0]
            self.age = 123

        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]

    def name_age(self):
        return self.name + str(self.age)



class Instructor:
    def __init__(self, course):
        self.course = course




class Student(Person, Instructor):

    def __init__(self, *args):
        Person.__init__(self, args[0], 444)
        Instructor.__init__(self, args[1])
        # super().__init__(name)

