# test_localization.py
from localization import Localization

localization = Localization()

for i in range(126):  
    name_key = f"monsters.{i}.name"
    species_key = f"monsters.{i}.species"
    description_key = f"monsters.{i}.description"
    
    name = localization.get_translation(name_key)
    species = localization.get_translation(species_key)
    description = localization.get_translation(description_key)
    
    print(f"Name: {name}, Species: {species}, Description: {description}")

localization.switch_language('fr')
for i in range(126):  
    name_key = f"monsters.{i}.name"
    species_key = f"monsters.{i}.species"
    description_key = f"monsters.{i}.description"
    
    name = localization.get_translation(name_key)
    species = localization.get_translation(species_key)
    description = localization.get_translation(description_key)
    
    print(f"Name: {name}, Species: {species}, Description: {description}")