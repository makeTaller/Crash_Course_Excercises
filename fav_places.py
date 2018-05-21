
favorite_places = {
    'david' : ['mexico','afica','cuba'],
    'simon' : ['Afgnaistan','morroco'],
    'Richard' : ['england','france','russia'],
}

for n,p in favorite_places.items():
    print(n + "'s favorite places are " )
    for i in p:
        print("\t" + i.title())
