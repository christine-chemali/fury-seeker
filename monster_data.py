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
    
    #Ghoul
    Monster({
        "name": {"en": "Flesh Eater", "fr": "Mangeur de Chair"},
        "species": {"en": "Ghoul", "fr": "Ghoule"},
        "health": 200, "level": 3,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Devour", "fr": "Dévorer"},
                {"en": "Claw", "fr": "Griffe"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Flesh Rend", "fr": "Déchirement de Chair"}
            ]}
        ],
        "weaknesses": {"en": ["Undead", "Beasts"], "fr": ["Morts-vivants", "Bêtes"]},
        "resistances": {"en": ["Elemental Spirits", "Mechanical Monsters"], "fr": ["Esprits Élémentaires", "Monstres Mécaniques"]},
        "description": {"en": "A hungry creature that devours everything in its path, leaving only bones behind. Its voracity is legendary.", 
                        "fr": "Une créature affamée qui dévore tout sur son passage, ne laissant que des os derrière elle. Sa voracité est légendaire."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 15, "speed": 12, "intelligence": 10
    }),
    Monster({
        "name": {"en": "Gravewalker", "fr": "Marcheur de Tombe"},
        "species": {"en": "Ghoul", "fr": "Ghoule"},
        "health": 220, "level": 4,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Terrorize", "fr": "Terroriser"},
                {"en": "Feast", "fr": "Festin"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Grave Grasp", "fr": "Saisie de Tombe"}
            ]}
        ],
        "weaknesses": {"en": ["Undead", "Beasts"], "fr": ["Morts-vivants", "Bêtes"]},
        "resistances": {"en": ["Elemental Spirits", "Mechanical Monsters"], "fr": ["Esprits Élémentaires", "Monstres Mécaniques"]},
        "description": {"en": "A ghoul that wanders between graves, feeding on the hearts of the living while spreading terror with every step.", 
                        "fr": "Une ghoule qui erre entre les tombes, se nourrissant des cœurs des vivants tout en répandant la terreur à chaque pas."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 17, "speed": 14, "intelligence": 12
    }),
    Monster({
        "name": {"en": "Rotting Corpse", "fr": "Cadavre en Décomposition"},
        "species": {"en": "Ghoul", "fr": "Ghoule"},
        "health": 210, "level": 3,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Flesh Gnaw", "fr": "Ronger Chair"},
                {"en": "Decay Touch", "fr": "Toucher de Décomposition"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Scream", "fr": "Cri"}
            ]}
        ],
        "weaknesses": {"en": ["Undead", "Beasts"], "fr": ["Morts-vivants", "Bêtes"]},
        "resistances": {"en": ["Elemental Spirits", "Mechanical Monsters"], "fr": ["Esprits Élémentaires", "Monstres Mécaniques"]},
        "description": {"en": "A decomposing corpse, animated by a dark force. Its touch causes disease and fear.", 
                        "fr": "Un cadavre en décomposition, animé par une force sombre. Son toucher cause maladie et peur."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 14, "speed": 11, "intelligence": 8
    }),
    Monster({
        "name": {"en": "Cannibal", "fr": "Cannibale"},
        "species": {"en": "Ghoul", "fr": "Ghoule"},
        "health": 230, "level": 4,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Savage Bite", "fr": "Morsure Sauvage"},
                {"en": "Flesh Feast", "fr": "Festin de Chair"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Ravage", "fr": "Ravage"}
            ]}
        ],
        "weaknesses": {"en": ["Undead", "Beasts"], "fr": ["Morts-vivants", "Bêtes"]},
        "resistances": {"en": ["Elemental Spirits", "Mechanical Monsters"], "fr": ["Esprits Élémentaires", "Monstres Mécaniques"]},
        "description": {"en": "A man-eating ghoul, mercilessly devouring its kin. Its thirst for human flesh is insatiable.", 
                        "fr": "Une ghoule anthropophage, dévorant sans pitié ses semblables. Sa soif de chair humaine est insatiable."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 18, "speed": 15, "intelligence": 11
    }),
    Monster({
        "name": {"en": "Shambling Horror", "fr": "Horreur Déambulante"},
        "species": {"en": "Ghoul", "fr": "Ghoule"},
        "health": 240, "level": 5,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Grasp", "fr": "Saisie"},
                {"en": "Lunge", "fr": "Fente"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Horrific Moan", "fr": "Gémissement Horrifique"}
            ]}
        ],
        "weaknesses": {"en": ["Undead", "Beasts"], "fr": ["Morts-vivants", "Bêtes"]},
        "resistances": {"en": ["Elemental Spirits", "Mechanical Monsters"], "fr": ["Esprits Élémentaires", "Monstres Mécaniques"]},
        "description": {"en": "A mass of decomposing flesh and bones, moving slowly but with terrifying strength.", 
                        "fr": "Une masse de chair et d'os en décomposition, se déplaçant lentement mais avec une force terrifiante."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 20, "speed": 13, "intelligence": 13
    }),
    Monster({
        "name": {"en": "Crypt Dweller", "fr": "Habitant de la Crypte"},
        "species": {"en": "Ghoul", "fr": "Ghoule"},
        "health": 215, "level": 4,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Gnaw", "fr": "Ronger"},
                {"en": "Shadow Lurk", "fr": "Guetter dans l'Ombre"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Creeping Fear", "fr": "Peur Rampante"}
            ]}
        ],
        "weaknesses": {"en": ["Undead", "Beasts"], "fr": ["Morts-vivants", "Bêtes"]},
        "resistances": {"en": ["Elemental Spirits", "Mechanical Monsters"], "fr": ["Esprits Élémentaires", "Monstres Mécaniques"]},
        "description": {"en": "A ghoul that haunts the crypts, emerging from the shadows to attack and frighten its prey.", 
                        "fr": "Une ghoule qui hante les cryptes, émergeant des ombres pour attaquer et effrayer sa proie."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 16, "speed": 16, "intelligence": 10
    }),
    Monster({
        "name": {"en": "Lurking Ghoul", "fr": "Ghoule Tapie"},
        "species": {"en": "Ghoul", "fr": "Ghoule"},
        "health": 205, "level": 3,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Slime Attack", "fr": "Attaque de Slime"},
                {"en": "Ghoul Rush", "fr": "Charge de Ghoule"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Maim", "fr": "Mutiler"}
            ]}
        ],
        "weaknesses": {"en": ["Undead", "Beasts"], "fr": ["Morts-vivants", "Bêtes"]},
        "resistances": {"en": ["Elemental Spirits", "Mechanical Monsters"], "fr": ["Esprits Élémentaires", "Monstres Mécaniques"]},
        "description": {"en": "A slimy, slippery ghoul that springs from the darkness to surprise and tear apart its victims.", 
                        "fr": "Une ghoule visqueuse et glissante qui surgit des ténèbres pour surprendre et déchirer ses victimes."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 15, "speed": 14, "intelligence": 9
    }),

    # Elementals
    Monster({
        "name": {"en": "Earth Spirit", "fr": "Esprit de la Terre"},
        "species": {"en": "Elemental", "fr": "Élémentaire"},
        "health": 180, "level": 4,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Rock Armor", "fr": "Armure de Pierre"},
                {"en": "Quake", "fr": "Tremblement"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Mudslide", "fr": "Glissement de Boue"}
            ]}
        ],
        "weaknesses": {"en": ["Beasts of the Forest", "Demons"], "fr": ["Bêtes de la Forêt", "Démons"]},
        "resistances": {"en": ["Dragons", "Cyborgs"], "fr": ["Dragons", "Cyborgs"]},
        "description": {"en": "A powerful spirit of the earth, capable of causing tremors and creating stone walls. Protector of forests.", 
                        "fr": "Un puissant esprit de la terre, capable de provoquer des tremblements et de créer des murs de pierre. Protecteur des forêts."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 30, "speed": 10, "intelligence": 20
    }),
    Monster({
        "name": {"en": "Water Wisp", "fr": "Lueur d'Eau"},
        "species": {"en": "Elemental", "fr": "Élémentaire"},
        "health": 160, "level": 3,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Drench", "fr": "Tremper"},
                {"en": "Water Shield", "fr": "Bouclier d'Eau"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Splash", "fr": "Éclaboussure"}
            ]}
        ],
        "weaknesses": {"en": ["Beasts of the Forest", "Demons"], "fr": ["Bêtes de la Forêt", "Démons"]},
        "resistances": {"en": ["Dragons", "Cyborgs"], "fr": ["Dragons", "Cyborgs"]},
        "description": {"en": "A light and elusive aquatic entity, capable of manipulating water for defense or attack.", 
                        "fr": "Une entité aquatique légère et insaisissable, capable de manipuler l'eau pour se défendre ou attaquer."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 12, "speed": 18, "intelligence": 14
    }),
    Monster({
        "name": {"en": "Fire Elemental", "fr": "Élémentaire de Feu"},
        "species": {"en": "Elemental", "fr": "Élémentaire"},
        "health": 190, "level": 4,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Flame Burst", "fr": "Éclatement de Flammes"},
                {"en": "Fire Whip", "fr": "Fouet de Feu"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Fire Shield", "fr": "Bouclier de Feu"}
            ]}
        ],
        "weaknesses": {"en": ["Beasts of the Forest", "Demons"], "fr": ["Bêtes de la Forêt", "Démons"]},
        "resistances": {"en": ["Dragons", "Cyborgs"], "fr": ["Dragons", "Cyborgs"]},
        "description": {"en": "A pure incarnation of fire, fast and destructive, leaving ashes and burns in its wake.", 
                        "fr": "Une incarnation pure du feu, rapide et destructive, laissant des cendres et des brûlures dans son sillage."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 20, "speed": 25, "intelligence": 15
    }),
    Monster({
        "name": {"en": "Air Spirit", "fr": "Esprit de l'Air"},
        "species": {"en": "Elemental", "fr": "Élémentaire"},
        "health": 170, "level": 3,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Gust", "fr": "Rafale"},
                {"en": "Whirlwind", "fr": "Tourbillon"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Tornado", "fr": "Tornade"}
            ]}
        ],
        "weaknesses": {"en": ["Beasts of the Forest", "Demons"], "fr": ["Bêtes de la Forêt", "Démons"]},
        "resistances": {"en": ["Dragons", "Cyborgs"], "fr": ["Dragons", "Cyborgs"]},
        "description": {"en": "An ethereal wind spirit, moving with the speed of breath, capable of creating storms.", 
                        "fr": "Un esprit éthéré du vent, se déplaçant à la vitesse du souffle, capable de créer des tempêtes."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 13, "speed": 22, "intelligence": 16
    }),
    Monster({
        "name": {"en": "Stone Guardian", "fr": "Gardien de Pierre"},
        "species": {"en": "Elemental", "fr": "Élémentaire"},
        "health": 200, "level": 5,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Rock Throw", "fr": "Lancer de Pierre"},
                {"en": "Earthquake", "fr": "Tremblement de Terre"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Stone Skin", "fr": "Peau de Pierre"}
            ]}
        ],
        "weaknesses": {"en": ["Beasts of the Forest", "Demons"], "fr": ["Bêtes de la Forêt", "Démons"]},
        "resistances": {"en": ["Dragons", "Cyborgs"], "fr": ["Dragons", "Cyborgs"]},
        "description": {"en": "A stone colossus, an impassable protector of nature, capable of withstanding all attacks.", 
                        "fr": "Un colosse de pierre, un protecteur impassable de la nature, capable de résister à toutes les attaques."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 35, "speed": 8, "intelligence": 18
    }),
    Monster({
        "name": {"en": "Lightning Wisp", "fr": "Lueur d'Éclair"},
        "species": {"en": "Elemental", "fr": "Élémentaire"},
        "health": 175, "level": 4,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Thunderbolt", "fr": "Foudre"},
                {"en": "Static Shock", "fr": "Choc Statique"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Electric Surge", "fr": "Vague Électrique"}
            ]}
        ],
        "weaknesses": {"en": ["Beasts of the Forest", "Demons"], "fr": ["Bêtes de la Forêt", "Démons"]},
        "resistances": {"en": ["Dragons", "Cyborgs"], "fr": ["Dragons", "Cyborgs"]},
        "description": {"en": "An electrical entity, fast and unpredictable, capable of releasing blazing discharges.", 
                        "fr": "Une entité électrique, rapide et imprévisible, capable de libérer des décharges brûlantes."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 15, "speed": 20, "intelligence": 15
    }),
    Monster({
        "name": {"en": "Wood Sprite", "fr": "Sprite de Bois"},
        "species": {"en": "Elemental", "fr": "Élémentaire"},
        "health": 165, "level": 3,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Vine Whip", "fr": "Fouet de Vigne"},
                {"en": "Nature's Grasp", "fr": "Saisie de la Nature"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Root Bind", "fr": "Liaison de Racine"}
            ]}
        ],
        "weaknesses": {"en": ["Beasts of the Forest", "Demons"], "fr": ["Bêtes de la Forêt", "Démons"]},
        "resistances": {"en": ["Dragons", "Cyborgs"], "fr": ["Dragons", "Cyborgs"]},
        "description": {"en": "A forest spirit that uses plants to capture its enemies and protect its territory.", 
                        "fr": "Un esprit de la forêt qui utilise les plantes pour capturer ses ennemis et protéger son territoire."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 14, "speed": 16, "intelligence": 12
    }),

  