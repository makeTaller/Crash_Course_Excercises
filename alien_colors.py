
alien_color = 'green'

if alien_color == 'green':
    print("You earned 5 points")

if alien_color == 'yellow':
    print("You lost 5 points")

alien_color = 'blue'

if alien_color != 'green':
    print("You earned 10 points")

if alien_color == 'yellow':
    print("You earned 10 points")
else:
    print("You lost 10 points")

# if elif statement
if alien_color == 'green':
    print("You earned 5 points")

elif alien_color == 'yellow':
    print("You earned 10 points")

elif alien_color == 'red':
    print("You earned 15 points")
else:
    print("Enter a color:")
