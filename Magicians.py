
def show_magicians(names):
    for n in names:
        print("name: " + n)

def make_great(name):
    for n in name:
        print("The Great "+ n)
        great_list.append("The Great " + n)

magician_names = ["Carl","Thomas","Sam"]
great_list = []

show_magicians(magician_names)

make_great(magician_names[:])

print(great_list)
