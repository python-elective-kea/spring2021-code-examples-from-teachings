
""" Bank Exercise 

Create a 

* Bank class
* Account Class
* Customer class

The bank class should be able to hold many account.
You should be able to add new accounts.
The Account class should have relevant details.
The Customer class Should also have relevant details.

Stick to the techniques we have covered so far.


"""

class Bank:
    def __init__(self):
        self.accounts = []

class Account:
    def __init__(self, no, cust):
        self.no = no
        self.cust = cust

class Customer:
    def __init__(self, *args):
        self.name =  args[0]
        self.age = args[1]

    def __str__(self):
        return self.name + str(self.age)

    def __repr__(self):
        return str(self.__dict__)
