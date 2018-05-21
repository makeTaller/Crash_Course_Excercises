"""A local Dictionary of what I learned in Python Crash Course"""

from collections import OrderedDict

#OrderedDict — Remember the Order Keys are Added to a Dictionary
#
# How to use a same structured list.
glossary = OrderedDict()

glossary['list'] = 'A collection of objects that can be used'
glossary['if-elif'] = 'Conditional test for multiple tries'
glossary['assign_op'] = 'Assign value to a variable'
glossary['equal_equal'] = 'Comparison operator used with if statment'
glossary['tuple'] = 'immutable list'
glossary['set'] = 'a list that must be unique'
glossary['for-loop'] = 'Repeat an action until loop is finished'

def show_glossary():
    for word, define in glossary.items():
        print(word.title()+  " is a : " + define)

show_glossary()

#print("List     : " + glossary['list'] + '\n')
#print("if-elif  : " + glossary['if-elif'] + '\n')
#print("assign_op: " + glossary['assign_op'] + '\n')
#print(" ==      : " + glossary['equal_equal'] + '\n')
#print("for-loop : " + glossary['for-loop'] + '\n')
#print("tuple : " + glossary['tuple'] + '\n')
#print("set : " + glossary['set'] + '\n')
