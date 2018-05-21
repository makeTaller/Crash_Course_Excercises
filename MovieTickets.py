# Movie ticket pricing for  all ages 

age = int(input("Hello, Enter your age:"))
movie_opened = True
ticket_price = 0

while movie_opened==True:
    if age <=3:
        ticket_price = 0
        print("You are a baby! It is free!")
        print("Your price is: $" + str(ticket_price))
        age = int(input("Hello, Enter your age:"))
    if age >3 and age <=12:
        ticket_price = 10
        print("Your price is: $" + str(ticket_price))
        age = int(input("Hello, Enter your age:"))
    if age >12:
        ticket_price = 15
        print("Your price is: $" + str(ticket_price))
        age = int(input("Hello, Enter your age:"))
    else:
        print("Thank you for attending the movies!")
        movie_opened =False
