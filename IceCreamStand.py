
import time
class Restaurant():
    """ A simple Restaurant class"""
    def __init__(self,r_name, r_cuisine):
        """ Initialize restaurantaurant instances"""
        self.r_name = r_name
        self.r_cuisine = r_cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(self.r_name + ' ' + self.r_cuisine)

    def open_restaurant(self):
        print(time.ctime())
        print(self.r_name + " is now opened. ")

    def set_number_served(self, number_served):
        print(time.ctime())
        self.number_served = int(number_served)
        print(" # serverd: " + str(self.number_served))

    def incr_num_served(self,inc_num):
        self.number_served += inc_num

    def show_served(self):
        print(time.ctime())
        print("Total Served: " + str(self.number_served))

class IceCreamStand(Restaurant):

    def __init__(self,r_name,r_cuisine="icecream"):
        super().__init__(r_name,r_cuisine)
        self.flavors = []

    def show_flavors(self):
        for f in self.flavors:
            print("flavors: " + f)

my_restaurant = Restaurant("Portillos","Italian Beef")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.set_number_served(6)
my_restaurant.incr_num_served(4)
my_restaurant.show_served()

print(my_restaurant.r_name)
print(my_restaurant.r_cuisine)

ice = IceCreamStand("Luigis")
ice.flavors = ["strawberry","watermelon"," chocolate","vanilla"]
ice.describe_restaurant()
ice.show_flavors()



