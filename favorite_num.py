
""" Program that takes in a number and stores it in a variable """
import json

favorite_number = input(" What is your favorite number? " )

with open('favorite_number.txt','w') as f:
    number =  json.dump(favorite_number,f)


with open('favorite_number.txt') as f:
    number =  json.load(f)
    print("I know your favorite number, it's " + str(number))



