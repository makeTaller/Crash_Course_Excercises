
sandwich_orders = ['Ham','Pastrami','Roast Beef','Pastrami','Turkey','Salomi','Pastrami',]
finished_sandwiches = []
print(" Sorry we are all out of Pastrami :( ")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')
for sandwich in sandwich_orders:
    print(" Your " + sandwich + " is ready. \n" )
    finished_sandwiches.append(sandwich)

