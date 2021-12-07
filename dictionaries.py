def user_profile(**details):
    for k,v in details.items():
        print(f"{k}: {v}".title())
user_profile(name="abasiubong",surname="effiong",occupation="lawyer",city="abuja")
