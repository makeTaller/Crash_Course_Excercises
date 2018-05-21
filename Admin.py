""" Privileges associated with Admin accounts """
from User import User
from Privileges import Privileges

class Admin(User):
    def __init__(self,first_name,last_name,department,office, p_number):
        super().__init__(first_name,last_name,department,office,p_number)
        # Initialize an empty set of privileges.
        self.privileges = Privileges([])

