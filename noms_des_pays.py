country_name = input("Tell me a country: ")
vowels=["AEOUIYÉ"]
plural=["Etats-Unis","Pays-Bas"]
exception=["Belize","Cambodge","Mexique","Mozabique","Zaïre","Zimbabwe"]
if country_name[0] in vowels and country_name not in plural:
    print(f"l'{country_name}")
elif country_name[-1] == "e" and country_name not in exception:
    print(f"la {country_name}")
elif country_name in plural:
    print(f"les {country_name}")
else:
    print(f"le {country_name}")