pizzas = ["Cheese", "Suasage","Peperoni", "Olives", "Jalepeno"]

for pizza in pizzas:
    print("I have "+ pizza +" Pizzas.")

print("I Love Pizza!")

freinds_pizza = pizzas[:]

freinds_pizza.append("Macaroni")

my_pizzas = [pie for pie in pizzas]

print("My favorite pizza is " + str(my_pizzas))

friends = [pie for pie in freinds_pizza]
print("My friends favorite pizza is " + str(friends) )
