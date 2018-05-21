## Teaches me how to automatically make a dictionary with a fuction
def build_profile(first,last, **user_info):
    """Build a dictionary containing everthing we know about a user."""
    profile ={}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('kirk', 'einstein',location = 'chicago', field='Engineering')
print(user_profile)
