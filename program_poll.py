filename= 'programming_poll.txt'
responses = []

while True:
    response = input("Why do you like programing?: ")
    responses.append(response)

    second_response = input("Would you like anyone else to go? y/n ")
    if second_response != 'y':
        break


with open(filename, 'a') as f:
    for response in responses:
        f.write(response + "\n")
