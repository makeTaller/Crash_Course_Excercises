petlist = ['cats.txt', 'dogs.txt']

def show_pets():
    for pet in petlist:
        print("Reading file:....")
        try:
            with open(pet) as file_object:
                contents = file_object.read()
        except FileNotFoundError:
            pass
            #print(" Sorry the file doesn't exist to me! ")
        else:
            if pet == 'cats.txt':
                print(" The cat's name is: " + contents )
            elif pet == 'dogs.txt':
                print(" The dog's name is: " + contents )

show_pets()

