danders = {
    'first_name': 'david',
    'last_name' : 'anderson',
    'department' : 'devOps',
    'number' : 1234,
    'location': 'Chicago',
}
ktolliv = {
    'first_name': 'Kirk',
    'last_name' : 'tolliver',
    'department' : 'devOps',
    'number' : 5654,
    'location': 'Chicago',
}
bthomson = {
    'first_name': 'bob',
    'last_name' : 'thomson',
    'department' : 'Accounting',
    'number' : 6732,
    'location': 'Alanta',
}
#usernames = [ "admin","david","foxmox","maketaller"]
users = [ ktolliv,danders,bthomson]

for user in users: 
    if user['location'] == 'Chicago':
        print(user['first_name'].title() +" we will meet at Lake Shore drive.")
    else:
        print(user['first_name'].title() +" you must come to Chicago.")
    #print(user)
#if 'admin' in usernames:
#    print("Hello admin, would you like to see a status report?")
#else:
#    for user in usernames:
#        print("Hello "+ user + " everyone!")
#
#usernames = []
#if usernames:
#    print("We have users.")
#else:
#    print("We need to find more users.")
