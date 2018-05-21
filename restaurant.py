""" A class that displays characteristics of a Restaurant. """
import time
class Restaurant():
    """ A simple Restaurant class"""
    def __init__(self,name, cuisine):
        """ Initialize restaurantaurant instances"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name + ' ' + self.cuisine)

    def open_restaurant(self):
        print(time.ctime())
        print(self.name + " is now opened. ")

    def set_number_served(self, number_served):
        self.number_served = int(number_served)
        print(" # serverd: " + str(self.number_served))

    def incr_num_served(self,inc_num):
        self.number_served += inc_num

    def show_served(self):
        print(time.ctime())
        print("Total Served: " + str(self.number_served))

class IceCreamStand(Restaurant):

    def __init__(self,name,cuisine="icecream"):
        super().__init__(name,cuisine)
        self.flavors =[]

    def show_flavors(self):
            for flavor in self.flavors:
                print("- " + flavor)

