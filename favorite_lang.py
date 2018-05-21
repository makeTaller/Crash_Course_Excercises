
favorite_lang = {
    'carl': 'python',
    'david': 'c++',
    'kirk': 'vb-script',
    'sam' : 'java',
    'jen' : 'python',
    'sarah' : 'C',
    'edward': 'ruby',
    'phil' : 'python',
}

taken_poll = ['david','kirk']

for name,lang in favorite_lang.items():
    if name in taken_poll:
        print("Thank You, " + name.title() + " for taking this poll!")
    else:
        print(name.title() + ", please take the poll!")
