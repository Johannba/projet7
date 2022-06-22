import bruteforce
import json

def modif_key(data: list) -> list:
    for dictionary in data:
        dictionary["name"] = dictionary["nom"]
        del dictionary["nom"]
        dictionary["price"] = dictionary["cout_par_action"]
        del dictionary["cout_par_action"]
        dictionary["profit"] = dictionary["bénéfice"]
        del dictionary["bénéfice"]
    return data


data_brute_force = bruteforce.data
call_modif_key = modif_key(data_brute_force)







# faire l'optimiser avec video
# faire fichier cvv donner open classeroum
# l'ance avec optimiser
# faire l'analyse.
