petlist = ['cats.txt', 'dogs.txt']

def show_pets():
    for pet in petlist:
        print("Reading file:....")
        try:
            with open(pet) as file_object:
                my_pet = file_object.read()
        except FileNotFoundError:
            print(" Sorry the file doesn't exist to me! ")
        else:
            if pet == 'cats.txt':
                print(" The cat's name is: " + my_pet )
            elif pet == 'dogs.txt':
                print(" The dog's name is: " + my_pet )

show_pets()

