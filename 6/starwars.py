import requests
import json

url_to_name = {"https://swapi.co/ai/species/1":"Human",
"https://swapi.co/ai/species/2":"Droid"}

def get_name_from_url(url):
    if url in url_to_name:
        return url_to_name[url]
    else:
        return "Other"

class Character:
        def __init__(self,nm = "Luke",sp = "Human", json_dict= None):
            if json_dict is not None:
                self.nm = json_dict[0]["name"]
                self.sp = json_dict[0]["species"]

            else:
                self.name = name #why does nm not work - because nm has to be defined in
                self.species = species #why does sp not work

        def __str__(self):
            return "I am " + self.name + "and I am a " + self.species

class Human(Character):
    def __init__(self, nm = "Luke",sp = "Human", eyes = "Brown", json_dict = None):
        super().__init__(nm,sp,json_dict)
        if json_dict is not None:
            self.eye_color = json_dict["eye_color"]

    def __str__(self):
        return super().__str__() + "and I have" + self.eye_color + "eyes"

base_people_url = "https://swapi.co/api/people"

r = requests.get(base_people_url)
#print (r.text)
json_dict = json.loads(r.text)
character_list = json_dict["results"]
characters = []
for character_dict in character_list:
    #get specifies info out of the character_dict
    species = character_dict["species"][0]
    if species == "Human":
        c= Human(json_dict = character_dict)
    else:
        c = Character(json_dict = character_list)
        characters.append(c)


#luke = Character(name = 'Luke Skywalker', species = 'Human')
#print(luke)
