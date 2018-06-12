filename= 'guest.txt'
guest = input("Enter your name:\n ")

with open(filename,'a') as file_object:
    file_object.write(guest)

