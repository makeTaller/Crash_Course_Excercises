## Teaches me how to automatically make a dictionary with a fuction
def build_car(manufacturer,model, **user_info):
    """Build a dictionary containing everthing we know about a user."""
    car ={}
    car['manufacturer_name'] = manufacturer
    car['model_name'] = model
    for key, value in user_info.items():
        car[key] = value
    return car

user_car = build_car('Dodge', 'Intrepid',owner = 'kirk', Engine='3.5')
print(user_car)
user_car = build_car('Chevorolet', 'Impala',owner = 'Jason Black', Engine='3.5')
print(user_car)
