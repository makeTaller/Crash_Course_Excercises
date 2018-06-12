filename = 'arecord.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

learned = ' '
for  line in  lines:
    learned += line.replace('python', 'C++')

print(learned)
print(len(learned))

#for line in lines:
#    line.replace('python','C++')
#    print(line.rstrip())

#contents = file_object.read()
#print(contents.rstrip())
