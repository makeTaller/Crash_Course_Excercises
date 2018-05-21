fav_num = {
    'mike': [23],
    'kirk': [23,14,9,6,10],
    'mark': [5,11,17],
}

print("My favorite number is: " + str(fav_num) )

for name, num in fav_num.items():
    print(name + "'s favorite numbers are: " )
    for n in num:
        print(n)
