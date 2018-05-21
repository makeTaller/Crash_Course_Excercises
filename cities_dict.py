
cities = {
    'Chicago' : {
    'state':'Illinois', 
    'population' :'3 million',
    'facts': '1st in murders',
    },

    'San Diego' : {
        'state' :'California',
        'population':'4 million', 
        'facts':'1st Tech',
    },


    'Fresno' : {
        'state' :'California',
        'population':'5 million', 
        'facts':'1st Metrosexual',
    },
}

for city,info in cities.items():
    print("\n City: " + city )
    information = info['state'] + info['population']+info['facts']
    print(information)
