# Monster Class


class Monster:
    def __init__(self, data):
        self.name = data["name"]
        self.species = data["species"]
        self.health = data["health"]
        self.level = data["level"]
        self.attack_types = data["attack_types"]
        self.weaknesses = data["weaknesses"]
        self.resistances = data["resistances"]
        self.description = data["description"]
        self.rarity = data["rarity"]
        self.defense = data["defense"]
        self.speed = data["speed"]
        self.intelligence = data["intelligence"]

    def get_stats(self):
        """Return monster stats as a dictionary."""
        return {
            "name": self.name,
            "species": self.species,
            "health": self.health,
            "level": self.level,
            "attack_types": self.attack_types,
            "weaknesses": self.weaknesses,
            "resistances": self.resistances,
            "description": self.description,
            "rarity": self.rarity,
            "defense": self.defense,
            "speed": self.speed,
            "intelligence": self.intelligence
        }