
rivers = {
    'nile': 'egypt',
    'missisippi': 'America',
    'Danub':'europe',
}

for key,value in rivers.items():
    print("The "+ key.title() + " river runs through " + value.title())

for key in rivers.keys():
    print(key.title() + " is a river.")

for value in rivers.values():
    print(value.title() + " is a county.")
