
filename = 'Macbeth.txt'
words = 0
with open(filename) as f:
    for content in f:
        words += content.count('the')
        
print("It appears " + str(words) + " times")

#for words in contents:
#    words.lower().count('to')
#    print(" This word occurs: " + words+ "times")
    
