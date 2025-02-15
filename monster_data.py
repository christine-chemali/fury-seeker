import json
from monster import Monster 

monsters = [

#Vampire
    Monster({
        "name": {"en": "Count Dracula", "fr": "Comte Dracula"},
        "species": {"en": "Vampire", "fr": "Vampire"},
        "health": 250,
        "level": 5,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Bite", "fr": "Morsure"},
                {"en": "Blood Drain", "fr": "Drain de Sang"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Charm", "fr": "Charme"}
            ]}
        ],
        "weaknesses": {"en": ["Humanoids", "Ghouls"], "fr": ["Humanoïdes", "Ghoules"]},
        "resistances": {"en": ["Angels", "Spiritual Entities"], "fr": ["Anges", "Entités Spirituelles"]},
        "description": {"en": "A legendary vampire, master of the night, feared for his intelligence and cruelty. He charms his victims before devouring them.", 
                        "fr": "Un vampire légendaire, maître de la nuit, craint pour son intelligence et sa cruauté. Il charme ses victimes avant de les dévorer."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 20, "speed": 15, "intelligence": 25
    }),
    Monster({
        "name": {"en": "Nosferatu", "fr": "Nosferatu"},
        "species": {"en": "Vampire", "fr": "Vampire"},
        "health": 230, "level": 4,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Suck Blood", "fr": "Suce le Sang"},
                {"en": "Shadow Step", "fr": "Pas de l'Ombre"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Hypnotic Gaze", "fr": "Regard Hypnotique"}
            ]}
        ],
        "weaknesses": {"en": ["Humanoids", "Ghouls"], "fr": ["Humanoïdes", "Ghoules"]},
        "resistances": {"en": ["Angels", "Spiritual Entities"], "fr": ["Anges", "Entités Spirituelles"]},
        "description": {"en": "A nocturnal creature, stealthy and terrifying, capable of blending into the shadows to surprise its enemies.", 
                        "fr": "Une créature nocturne, furtive et terrifiante, capable de se fondre dans les ombres pour surprendre ses ennemis."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 18, "speed": 20, "intelligence": 22
    }),
    Monster({
        "name": {"en": "Vlad the Impaler", "fr": "Vlad l'Empaleur"},
        "species": {"en": "Vampire", "fr": "Vampire"},
        "health": 240, "level": 5,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Blood Feast", "fr": "Festin de Sang"},
                {"en": "Mist Form", "fr": "Forme de Brume"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Darkness", "fr": "Obscurité"}
            ]}
        ],
        "weaknesses": {"en": ["Humanoids", "Ghouls"], "fr": ["Humanoïdes", "Ghoules"]},
        "resistances": {"en": ["Angels", "Spiritual Entities"], "fr": ["Anges", "Entités Spirituelles"]},
        "description": {"en": "A cruel prince known for his bloody methods. He inspires fear and devotion, manipulating those around him.", 
                        "fr": "Un prince cruel connu pour ses méthodes sanglantes. Il inspire la peur et la dévotion, manipulant ceux qui l'entourent."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 25, "speed": 18, "intelligence": 28
    }),
    Monster({
        "name": {"en": "Bloodsucker", "fr": "Sangsue"},
        "species": {"en": "Vampire", "fr": "Vampire"},
        "health": 220, "level": 4,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Vampiric Touch", "fr": "Toucher Vampirique"},
                {"en": "Chilling Embrace", "fr": "Étreinte Glaciale"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Scream", "fr": "Cri"}
            ]}
        ],
        "weaknesses": {"en": ["Humanoids", "Ghouls"], "fr": ["Humanoïdes", "Ghoules"]},
        "resistances": {"en": ["Angels", "Spiritual Entities"], "fr": ["Anges", "Entités Spirituelles"]},
        "description": {"en": "A bloodthirsty vampire, wandering in the darkness searching for innocent victims to devour.", 
                        "fr": "Un vampire assoiffé de sang, errant dans l'obscurité à la recherche de victimes innocentes à dévorer."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 16, "speed": 17, "intelligence": 14
    }),
    Monster({
        "name": {"en": "Bat Lord", "fr": "Seigneur des Chauves-souris"},
        "species": {"en": "Vampire", "fr": "Vampire"},
        "health": 210, "level": 3,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Screech", "fr": "Cri"},
                {"en": "Wing Slash", "fr": "Coup d'Aile"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Bat Swarm", "fr": "Essaim de Chauves-souris"}
            ]}
        ],
        "weaknesses": {"en": ["Humanoids", "Ghouls"], "fr": ["Humanoïdes", "Ghoules"]},
        "resistances": {"en": ["Angels", "Spiritual Entities"], "fr": ["Anges", "Entités Spirituelles"]},
        "description": {"en": "A vampire capable of transforming into a swarm of bats to escape his enemies or attack them.", 
                        "fr": "Un vampire capable de se transformer en essaim de chauves-souris pour échapper à ses ennemis ou les attaquer."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 14, "speed": 22, "intelligence": 12
    }),
    Monster({
        "name": {"en": "Shadow Stalker", "fr": "Traqueur des Ombres"},
        "species": {"en": "Vampire", "fr": "Vampire"},
        "health": 200, "level": 4,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Shadow Strike", "fr": "Frappe de l'Ombre"},
                {"en": "Cloak of Shadows", "fr": "Cape des Ombres"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Hypnotic Gaze", "fr": "Regard Hypnotique"}
            ]}
        ],
        "weaknesses": {"en": ["Humanoids", "Ghouls"], "fr": ["Humanoïdes", "Ghoules"]},
        "resistances": {"en": ["Angels", "Spiritual Entities"], "fr": ["Anges", "Entités Spirituelles"]},
        "description": {"en": "A shadow vampire, moving stealthily to attack its prey without warning.", 
                        "fr": "Un vampire des ombres, se déplaçant furtivement pour attaquer sa proie sans avertir."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 15, "speed": 18, "intelligence": 16
    }),
    Monster({
        "name": {"en": "Night Hunter", "fr": "Chasseur de Nuit"},
        "species": {"en": "Vampire", "fr": "Vampire"},
        "health": 215, "level": 5,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Nightmare", "fr": "Cauchemar"},
                {"en": "Blood Dart", "fr": "Flèche de Sang"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Veil of Darkness", "fr": "Voile des Ténèbres"}
            ]}
        ],
        "weaknesses": {"en": ["Humanoids", "Ghouls"], "fr": ["Humanoïdes", "Ghoules"]},
        "resistances": {"en": ["Angels", "Spiritual Entities"], "fr": ["Anges", "Entités Spirituelles"]},
        "description": {"en": "A vampire who stalks his victims in the darkness of night, using terror to paralyze them.", 
                        "fr": "Un vampire qui traque ses victimes dans l'obscurité de la nuit, utilisant la terreur pour les paralyser."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 17, "speed": 20, "intelligence": 18}),
    