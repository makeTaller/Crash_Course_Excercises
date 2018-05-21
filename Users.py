""" A class of User profiles and Privileges for Users"""
class Users():

    def __init__(self,first_name, last_name,department,office,p_number):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.office = office
        self.p_number = p_number


    def describe_user(self):
        print(" Hello "+ self.first_name + ' '+ self.last_name )
        print(" is in " + self.department + " at the " + self.office + "locaation \n ")
        print(" can be contacted at " + self.p_number + " ")

""" Provide privileges for User class"""
class Privileges():
    def __init__(self,privileges):
        self.privileges = privileges

    def show_privileges(self):
        for p in self.privileges:
            print(":: " + p)

""" Privileges associated with Admin accounts """
class Admin(Users):
    def __init__(self,first_name,last_name,department,office, p_number):
        super().__init__(first_name,last_name,department,office,p_number)
        
        # Initialize an empty set of privileges.
        self.privileges = Privileges([])


