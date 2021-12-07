def user_profile(country, **details):
    """display user's profile"""
    details["country"] = country
    return details
    # for k,v in details.items():
    #     print(f"{k}: {v}".title())
profile = user_profile("Nigeria", name="abasiubong",surname="effiong",occupation="lawyer",city="abuja")
print (profile)