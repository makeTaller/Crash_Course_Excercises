filename= 'guest.txt'
guest = input("Enter your name: ")
on = True

with open(filename,'a') as file_object:

        while on == True:
            if guest == 'q':
               on= False
            else:
                file_object.write(guest + '\n')

