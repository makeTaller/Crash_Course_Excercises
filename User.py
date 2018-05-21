""" A class of User profiles and Privileges for Users"""
class User():

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

