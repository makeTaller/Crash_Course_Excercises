home = "Chicago"
print("Do you live in chicago?")
print(home == "Chicago")

love = "no"
print("Do you have a love?")
print(love == "yes")

money = "no"
drugs = "yes"
print("Do you have any money or drugs")
print( money == "yes" or drugs == "yes")

books = ["Ralph Emerson", "james Allen", "jndrew carnege"]
books = [book.lower() for book in books]
print(books)

print("ralph emerson" in books)

if 'James allen' not in books:
    print("James Allen is not your library")

