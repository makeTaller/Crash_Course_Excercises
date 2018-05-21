""" Provide privileges for User class"""
class Privileges():
    def __init__(self,privileges):
        self.privileges = privileges

    def show_privileges(self):
        for p in self.privileges:
            print(":: " + p)

