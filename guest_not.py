filename= 'guest.txt'
on = True

with open(filename,'a') as file_object:
    while on == True:
        guest = input("Enter your name: ")
        file_object.write(guest + '\n')

