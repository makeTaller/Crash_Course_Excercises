
current_users = ['bsodot', 'dsmith', 'pmocormick', 'dransom','etolliver']

new_users = ['efraser', 'dbright', 'dsmith', 'bsodot', 'tpain']

for user in  new_users:
    if user in current_users:
         print("This username is already taken.")
    else:
         print("This username is availible.")
