guest_list = [ 'Fela Kuti', 'Adolf Hilter', ' Martin Luther', 'david Bright']

print("Welcome, " + guest_list[0] + " to the year 2018. Have mercy on us all!")
print("Welcome, " + guest_list[1] + " to the year 2018. Have mercy on us all!")
print("Welcome, " + guest_list[2] + " to the year 2018. Have mercy on us all!")
print("Welcome, " + guest_list[3].title() + " to the year 2018. Have mercy on us all!")

change_guest = guest_list.pop(1)

print("Sorry, " + change_guest + " can not make it. He is dead.")
guest_list.append('Practice Lamumba')
print("I will be inviting, " + guest_list[-1] + " instead")

print("Welcome, " + guest_list[0] + " to the year 2018. Have mercy on us all!")
print("Welcome, " + guest_list[1] + " to the year 2018. Have mercy on us all!")
print("Welcome, " + guest_list[2].title() + " to the year 2018. Have mercy on us all!")
print("Welcome, " + guest_list[3].title() + " to the year 2018. Have mercy on us all!")
print("It has just come to mind that I have a new table for us to have dinner")

guest_list.insert(0,'John Lothe')
guest_list.insert(0,'Jason Black')

guest_list.append('Kirk Tolliver')

print(guest_list)
