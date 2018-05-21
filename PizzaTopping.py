P_topping = input("Enter the pizza toppings you want: ")
pizza = []

active = True
toppings = ['extra cheese', 'peporoni', 'sausage','jalepeno']
while  active==True:
    if  P_topping in toppings:
        print("We're adding " + P_topping + " to your pizza.\n")
        print("Enter another topping or type quit to exit.\n")
        pizza.append(P_topping)
        P_topping = input("Enter the topping: ")

    elif P_topping == "quit":
        print("Thank you, for choosing a pizza with: " + str(pizza) )
        active = False
