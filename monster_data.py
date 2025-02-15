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

    # Beasts
    Monster({
        "name": {"en": "Wild Beast", "fr": "Bête Sauvage"},
        "species": {"en": "Beast", "fr": "Bête"},
        "health": 250, "level": 5,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Pounce", "fr": "Saut"},
                {"en": "Furious Charge", "fr": "Charge Furieuse"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Bite", "fr": "Morsure"}
            ]}
        ],
        "weaknesses": {"en": ["Ghosts", "Fairies"], "fr": ["Fantômes", "Fées"]},
        "resistances": {"en": ["Vampires", "Elementals"], "fr": ["Vampires", "Éléments"]},
        "description": {"en": "A wild beast, fast and fierce, attacking with uncontrollable rage. It is the terror of the weak.", 
                        "fr": "Une bête sauvage, rapide et féroce, attaquant avec une rage incontrôlable. C'est la terreur des faibles."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 22, "speed": 30, "intelligence": 10
    }),
    Monster({
        "name": {"en": "Spirit Wolf", "fr": "Loup Spirituel"},
        "species": {"en": "Beast", "fr": "Bête"},
        "health": 230, "level": 4,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Fang Strike", "fr": "Frappe de Crocs"},
                {"en": "Pack Mentality", "fr": "Mentalité de Meute"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Howl", "fr": "Hurlement"}
            ]}
        ],
        "weaknesses": {"en": ["Ghosts", "Fairies"], "fr": ["Fantômes", "Fées"]},
        "resistances": {"en": ["Vampires", "Elementals"], "fr": ["Vampires", "Éléments"]},
        "description": {"en": "A spirit wolf, loyal and protective, able to gather a pack to hunt its enemies.", 
                        "fr": "Un loup spirituel, loyal et protecteur, capable de rassembler une meute pour chasser ses ennemis."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 18, "speed": 25, "intelligence": 12
    }),
    Monster({
        "name": {"en": "Feral Cat", "fr": "Chat Sauvage"},
        "species": {"en": "Beast", "fr": "Bête"},
        "health": 180, "level": 3,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Scratch", "fr": "Griffer"},
                {"en": "Pounce", "fr": "Saut"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Quick Escape", "fr": "Évasion Rapide"}
            ]}
        ],
        "weaknesses": {"en": ["Ghosts", "Fairies"], "fr": ["Fantômes", "Fées"]},
        "resistances": {"en": ["Vampires", "Elementals"], "fr": ["Vampires", "Éléments"]},
        "description": {"en": "A wild feline, agile and unpredictable, using its agility to escape predators.", 
                        "fr": "Un félin sauvage, agile et imprévisible, utilisant son agilité pour échapper aux prédateurs."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 13, "speed": 28, "intelligence": 9
    }),
    Monster({
        "name": {"en": "Mountain Lion", "fr": "Puma"},
        "species": {"en": "Beast", "fr": "Bête"},
        "health": 240, "level": 5,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Claw Slash", "fr": "Coup de Griffe"},
                {"en": "Ambush", "fr": "Embuscade"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Roar", "fr": "Rugissement"}
            ]}
        ],
        "weaknesses": {"en": ["Ghosts", "Fairies"], "fr": ["Fantômes", "Fées"]},
        "resistances": {"en": ["Vampires", "Elementals"], "fr": ["Vampires", "Éléments"]},
        "description": {"en": "A powerful mountain feline, a fearsome predator and agile hunter, capable of surprise attacks.", 
                        "fr": "Un puissant félin de montagne, un prédateur redoutable et un chasseur agile, capable d'attaques surprises."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 20, "speed": 27, "intelligence": 11
    }),
    Monster({
        "name": {"en": "Dire Wolf", "fr": "Loup Dire"},
        "species": {"en": "Beast", "fr": "Bête"},
        "health": 220, "level": 4,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Pack Attack", "fr": "Attaque de Meute"},
                {"en": "Bite", "fr": "Morsure"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Howl of Fury", "fr": "Hurlement de Furie"}
            ]}
        ],
        "weaknesses": {"en": ["Ghosts", "Fairies"], "fr": ["Fantômes", "Fées"]},
        "resistances": {"en": ["Vampires", "Elementals"], "fr": ["Vampires", "Éléments"]},
        "description": {"en": "A wolf of darkness, leader of a ruthless pack, capable of coordinating group attacks.", 
                        "fr": "Un loup des ténèbres, leader d'une meute impitoyable, capable de coordonner des attaques de groupe."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 17, "speed": 23, "intelligence": 13
    }),
    Monster({
        "name": {"en": "Giant Bear", "fr": "Ours Géant"},
        "species": {"en": "Beast", "fr": "Bête"},
        "health": 260, "level": 6,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Mighty Swipe", "fr": "Coup Puissant"},
                {"en": "Charge", "fr": "Charge"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Roar of the Wild", "fr": "Rugissement de la Nature"}
            ]}
        ],
        "weaknesses": {"en": ["Ghosts", "Fairies"], "fr": ["Fantômes", "Fées"]},
        "resistances": {"en": ["Vampires", "Elementals"], "fr": ["Vampires", "Éléments"]},
        "description": {"en": "A giant bear, a symbol of strength and power, capable of crushing its enemies with a single blow.", 
                        "fr": "Un ours géant, un symbole de force et de pouvoir, capable d'écraser ses ennemis d'un seul coup."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 35, "speed": 8, "intelligence": 12
    }),
    Monster({
        "name": {"en": "Saber-Toothed Tiger", "fr": "Tigre à Dents de Sabre"},
        "species": {"en": "Beast", "fr": "Bête"},
        "health": 240, "level": 5,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Fang Bite", "fr": "Morsure de Croc"},
                {"en": "Quick Strike", "fr": "Frappe Rapide"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Predator's Instinct", "fr": "Instinct de Prédateur"}
            ]}
        ],
        "weaknesses": {"en": ["Ghosts", "Fairies"], "fr": ["Fantômes", "Fées"]},
        "resistances": {"en": ["Vampires", "Elementals"], "fr": ["Vampires", "Éléments"]},
        "description": {"en": "A prehistoric feline with sharp fangs and lightning speed, hunting with deadly swiftness.", 
                        "fr": "Un félin préhistorique avec des crocs acérés et une vitesse fulgurante, chassant avec une rapidité mortelle."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 19, "speed": 29, "intelligence": 10
    }),

    # Humanoids    
    Monster({
        "name": {"en": "Knight", "fr": "Chevalier"},
        "species": {"en": "Humanoid", "fr": "Humanoïde"},
        "health": 210, "level": 4,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Sword Slash", "fr": "Coup d'Épée"},
                {"en": "Charge Forward", "fr": "Charge en Avant"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Shield Block", "fr": "Blocage de Bouclier"}
            ]}
        ],
        "weaknesses": {"en": ["Mechanical Monsters", "Spiritual Entities"], "fr": ["Monstres Mécaniques", "Entités Spirituelles"]},
        "resistances": {"en": ["Dragons", "Ghouls"], "fr": ["Dragons", "Ghoules"]},
        "description": {"en": "A brave knight, protector of his kingdom, wielding his sword with honor and determination. Always ready to defend the innocent.", 
                        "fr": "Un chevalier brave, protecteur de son royaume, maniant son épée avec honneur et détermination. Toujours prêt à défendre les innocents."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 22, "speed": 16, "intelligence": 14
    }),
    Monster({
        "name": {"en": "Rogue", "fr": "Voleur"},
        "species": {"en": "Humanoid", "fr": "Humanoïde"},
        "health": 190, "level": 3,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Dagger Thrust", "fr": "Poussée de Dague"},
                {"en": "Sneak Attack", "fr": "Attaque Sournoise"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Smoke Bomb", "fr": "Bombe Fumigène"}
            ]}
        ],
        "weaknesses": {"en": ["Mechanical Monsters", "Spiritual Entities"], "fr": ["Monstres Mécaniques", "Entités Spirituelles"]},
        "resistances": {"en": ["Dragons", "Ghouls"], "fr": ["Dragons", "Ghoules"]},
        "description": {"en": "An agile and stealthy thief, moving in the shadows to strike his enemies by surprise and escape unseen.", 
                        "fr": "Un voleur agile et furtif, se déplaçant dans l'ombre pour frapper ses ennemis par surprise et s'échapper sans être vu."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 15, "speed": 20, "intelligence": 15
    }),
    Monster({
        "name": {"en": "Paladin", "fr": "Paladin"},
        "species": {"en": "Humanoid", "fr": "Humanoïde"},
        "health": 220, "level": 5,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Holy Strike", "fr": "Frappe Sacrée"},
                {"en": "Smite", "fr": "Frappe Divine"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Divine Shield", "fr": "Bouclier Divin"}
            ]}
        ],
        "weaknesses": {"en": ["Mechanical Monsters", "Spiritual Entities"], "fr": ["Monstres Mécaniques", "Entités Spirituelles"]},
        "resistances": {"en": ["Dragons", "Ghouls"], "fr": ["Dragons", "Ghoules"]},
        "description": {"en": "A sacred paladin, defender of faith and justice, capable of channeling divine power to protect his allies.", 
                        "fr": "Un paladin sacré, défenseur de la foi et de la justice, capable de canaliser une puissance divine pour protéger ses alliés."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 24, "speed": 17, "intelligence": 18
    }),
    Monster({
        "name": {"en": "Archer", "fr": "Archer"},
        "species": {"en": "Humanoid", "fr": "Humanoïde"},
        "health": 200, "level": 4,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Arrow Shot", "fr": "Tir de Flèche"},
                {"en": "Multi-Shot", "fr": "Tir Multiple"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Eagle Eye", "fr": "Oeil d'Aigle"}
            ]}
        ],
        "weaknesses": {"en": ["Mechanical Monsters", "Spiritual Entities"], "fr": ["Monstres Mécaniques", "Entités Spirituelles"]},
        "resistances": {"en": ["Dragons", "Ghouls"], "fr": ["Dragons", "Ghoules"]},
        "description": {"en": "An expert archer, capable of firing arrows with great precision, striking his targets from a distance.", 
                        "fr": "Un archer expert, capable de tirer des flèches avec une grande précision, frappant ses cibles à distance."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 16, "speed": 22, "intelligence": 14
    }),
    Monster({
        "name": {"en": "Bard", "fr": "Barde"},
        "species": {"en": "Humanoid", "fr": "Humanoïde"},
        "health": 180, "level": 3,
        "attack_types": [
            {"type": {"en": "support", "fr": "soutien"}, "moves": [
                {"en": "Inspire", "fr": "Inspirer"},
                {"en": "Song of Courage", "fr": "Chanson de Courage"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Soothing Melody", "fr": "Mélodie Apaisante"}
            ]}
        ],
        "weaknesses": {"en": ["Mechanical Monsters", "Spiritual Entities"], "fr": ["Monstres Mécaniques", "Entités Spirituelles"]},
        "resistances": {"en": ["Dragons", "Ghouls"], "fr": ["Dragons", "Ghoules"]},
        "description": {"en": "A talented bard, using music to inspire his allies and soothe their fears during battle.", 
                        "fr": "Un barde talentueux, utilisant la musique pour inspirer ses alliés et apaiser leurs peurs pendant le combat."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 12, "speed": 18, "intelligence": 18
    }),
    Monster({
        "name": {"en": "Mage", "fr": "Mage"},
        "species": {"en": "Humanoid", "fr": "Humanoïde"},
        "health": 170, "level": 3,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Fireball", "fr": "Boulet de Feu"},
                {"en": "Arcane Blast", "fr": "Explosion Arcanique"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Frost Nova", "fr": "Nova de Gel"}
            ]}
        ],
        "weaknesses": {"en": ["Mechanical Monsters", "Spiritual Entities"], "fr": ["Monstres Mécaniques", "Entités Spirituelles"]},
        "resistances": {"en": ["Dragons", "Ghouls"], "fr": ["Dragons", "Ghoules"]},
        "description": {"en": "A powerful mage, wielding the arcane arts with skill, capable of casting devastating spells on his enemies.", 
                        "fr": "Un mage puissant, maniant les arts arcanes avec habileté, capable de lancer des sorts dévastateurs sur ses ennemis."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 14, "speed": 19, "intelligence": 22
    }),
    Monster({
        "name": {"en": "Warrior", "fr": "Guerrier"},
        "species": {"en": "Humanoid", "fr": "Humanoïde"},
        "health": 240, "level": 6,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Heavy Slam", "fr": "Écrasement Puissant"},
                {"en": "Battle Cry", "fr": "Cri de Guerre"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Warrior's Might", "fr": "Force du Guerrier"}
            ]}
        ],
        "weaknesses": {"en": ["Mechanical Monsters", "Spiritual Entities"], "fr": ["Monstres Mécaniques", "Entités Spirituelles"]},
        "resistances": {"en": ["Dragons", "Ghouls"], "fr": ["Dragons", "Ghoules"]},
        "description": {"en": "A hardened warrior, formidable in close combat, using his brute strength to crush his opponents.", 
                        "fr": "Un guerrier aguerri, redoutable au combat rapproché, utilisant sa force brute pour écraser ses adversaires."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 25, "speed": 18, "intelligence": 13
    }),

    # Ghosts
    Monster({
        "name": {"en": "Wraith", "fr": "Spectre"},
        "species": {"en": "Ghost", "fr": "Fantôme"},
        "health": 210, "level": 4,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Haunt", "fr": "Hanter"},
                {"en": "Ethereal Walk", "fr": "Marche Éthérée"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Soul Steal", "fr": "Vol d'Âme"}
            ]}
        ],
        "weaknesses": {"en": ["Undead", "Angels"], "fr": ["Morts-vivants", "Anges"]},
        "resistances": {"en": ["Demons", "Elemental Spirits"], "fr": ["Démons", "Esprits Élémentaires"]},
        "description": {"en": "A spectral wraith, wandering between worlds, capable of stealing the souls of its victims and moving through walls.", 
                        "fr": "Un spectre spectral, errant entre les mondes, capable de voler les âmes de ses victimes et de traverser les murs."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 18, "speed": 20, "intelligence": 22
    }),
    Monster({
        "name": {"en": "Phantom", "fr": "Fantôme"},
        "species": {"en": "Ghost", "fr": "Fantôme"},
        "health": 200, "level": 5,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Spectral Slash", "fr": "Coup Spectral"},
                {"en": "Haunting Melody", "fr": "Mélodie Hantée"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Possession", "fr": "Possession"}
            ]}
        ],
        "weaknesses": {"en": ["Undead", "Angels"], "fr": ["Morts-vivants", "Anges"]},
        "resistances": {"en": ["Demons", "Elemental Spirits"], "fr": ["Démons", "Esprits Élémentaires"]},
        "description": {"en": "A vengeful ghost, capable of entering the minds of the living to control them and torment them with its enchanting melody.", 
                        "fr": "Un fantôme vengeur, capable d'entrer dans l'esprit des vivants pour les contrôler et les tourmenter avec sa mélodie envoûtante."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 20, "speed": 19, "intelligence": 24
    }),
    Monster({
        "name": {"en": "Banshee", "fr": "Banshee"},
        "species": {"en": "Ghost", "fr": "Fantôme"},
        "health": 220, "level": 5,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Scream", "fr": "Cri"},
                {"en": "Wail of the Damned", "fr": "Gémissement des Damnés"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Lament", "fr": "Lamentation"}
            ]}
        ],
        "weaknesses": {"en": ["Undead", "Angels"], "fr": ["Morts-vivants", "Anges"]},
        "resistances": {"en": ["Demons", "Elemental Spirits"], "fr": ["Démons", "Esprits Élémentaires"]},
        "description": {"en": "A banshee, harbinger of death, whose piercing scream can paralyze with fear those who hear it.", 
                        "fr": "Une banshee, annonciatrice de mort, dont le cri perçant peut paralyser de peur ceux qui l'entendent."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 19, "speed": 18, "intelligence": 21
    }),
    Monster({
        "name": {"en": "Spirit", "fr": "Esprit"},
        "species": {"en": "Ghost", "fr": "Fantôme"},
        "health": 190, "level": 3,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Ethereal Touch", "fr": "Toucher Éthéré"},
                {"en": "Ghostly Grasp", "fr": "Saisie Fantomatique"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Frighten", "fr": "Effrayer"}
            ]}
        ],
        "weaknesses": {"en": ["Undead", "Angels"], "fr": ["Morts-vivants", "Anges"]},
        "resistances": {"en": ["Demons", "Elemental Spirits"], "fr": ["Démons", "Esprits Élémentaires"]},
        "description": {"en": "A wandering spirit, capable of instilling fear with its chilling touch and grasping its enemies in a spectral embrace.", 
                        "fr": "Un esprit errant, capable d'instiller la peur avec son toucher glacial et de saisir ses ennemis dans une étreinte spectrale."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 15, "speed": 16, "intelligence": 15
    }),
    Monster({
        "name": {"en": "Revenant", "fr": "Revenant"},
        "species": {"en": "Ghost", "fr": "Fantôme"},
        "health": 230, "level": 5,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Vengeful Strike", "fr": "Frappe Vengeresse"},
                {"en": "Spectral Shield", "fr": "Bouclier Spectral"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Curse", "fr": "Malédiction"}
            ]}
        ],
        "weaknesses": {"en": ["Undead", "Angels"], "fr": ["Morts-vivants", "Anges"]},
        "resistances": {"en": ["Demons", "Elemental Spirits"], "fr": ["Démons", "Esprits Élémentaires"]},
        "description": {"en": "A revenant, haunted by its desire for vengeance, capable of cursing its enemies and resisting physical attacks.", 
                        "fr": "Un revenant, hanté par son désir de vengeance, capable de maudire ses ennemis et de résister aux attaques physiques."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 22, "speed": 17, "intelligence": 20
    }),
    Monster({
        "name": {"en": "Haunting Specter", "fr": "Spectre Hanté"},
        "species": {"en": "Ghost", "fr": "Fantôme"},
        "health": 205, "level": 4,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Chilling Grasp", "fr": "Saisie Glaciale"},
                {"en": "Ghostly Howl", "fr": "Hurlement Fantomatique"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Nightmare", "fr": "Cauchemar"}
            ]}
        ],
        "weaknesses": {"en": ["Undead", "Angels"], "fr": ["Morts-vivants", "Anges"]},
        "resistances": {"en": ["Demons", "Elemental Spirits"], "fr": ["Démons", "Esprits Élémentaires"]},
        "description": {"en": "A haunted specter, capable of inducing nightmares and frightening those who dare approach it.", 
                        "fr": "Un spectre hanté, capable d'induire des cauchemars et d'effrayer ceux qui osent s'en approcher."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 16, "speed": 18, "intelligence": 18
    }),
    Monster({
        "name": {"en": "Ghostly Knight", "fr": "Chevalier Fantomatique"},
        "species": {"en": "Ghost", "fr": "Fantôme"},
        "health": 215, "level": 5,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Haunting Blade", "fr": "Lame Hantée"},
                {"en": "Eternal Vigilance", "fr": "Vigilance Éternelle"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Phantom Charge", "fr": "Charge Fantomatique"}
            ]}
        ],
        "weaknesses": {"en": ["Undead", "Angels"], "fr": ["Morts-vivants", "Anges"]},
        "resistances": {"en": ["Demons", "Elemental Spirits"], "fr": ["Démons", "Esprits Élémentaires"]},
        "description": {"en": "A ghostly knight, guardian of lost souls, wielding a spectral sword and eternally watching over its domain.", 
                        "fr": "Un chevalier fantomatique, gardien des âmes perdues, maniant une épée spectrale et veillant éternellement sur son domaine."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 21, "speed": 15, "intelligence": 23
    }),

    # Mechanical Monsters
    Monster({
        "name": {"en": "Iron Golem", "fr": "Golem de Fer"},
        "species": {"en": "Mechanical Monster", "fr": "Monstre Mécanique"},
        "health": 300, "level": 6,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Crush", "fr": "Écraser"},
                {"en": "Iron Grip", "fr": "Prise de Fer"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Guard", "fr": "Garde"}
            ]}
        ],
        "weaknesses": {"en": ["Cyborgs", "Beasts"], "fr": ["Cyborgs", "Bêtes"]},
        "resistances": {"en": ["Fairies", "Vampires"], "fr": ["Fées", "Vampires"]},
        "description": {"en": "A massive iron golem, relentless and resilient, capable of crushing its enemies with unmatched brute force.", 
                        "fr": "Un énorme golem de fer, implacable et résistant, capable d'écraser ses ennemis avec une force brute inégalée."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 40, "speed": 10, "intelligence": 15
    }),
    Monster({
        "name": {"en": "Clockwork Knight", "fr": "Chevalier à Remontage"},
        "species": {"en": "Mechanical Monster", "fr": "Monstre Mécanique"},
        "health": 280, "level": 5,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Blade Whirl", "fr": "Tourbillon de Lame"},
                {"en": "Precision Strike", "fr": "Frappe Précise"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Shield Bash", "fr": "Coup de Bouclier"}
            ]}
        ],
        "weaknesses": {"en": ["Cyborgs", "Beasts"], "fr": ["Cyborgs", "Bêtes"]},
        "resistances": {"en": ["Fairies", "Vampires"], "fr": ["Fées", "Vampires"]},
        "description": {"en": "A spring-loaded knight, fast and agile, wielding a sharp sword with precision while protecting its master.", 
                        "fr": "Un chevalier à ressort, rapide et agile, maniant une épée tranchante avec précision tout en protégeant son maître."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 30, "speed": 20, "intelligence": 18
    }),
    Monster({
        "name": {"en": "Steel Behemoth", "fr": "Béhémoth d'Acier"},
        "species": {"en": "Mechanical Monster", "fr": "Monstre Mécanique"},
        "health": 320, "level": 7,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Smash", "fr": "Écraser"},
                {"en": "Titan's Wrath", "fr": "Colère du Titan"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Iron Fist", "fr": "Poing de Fer"}
            ]}
        ],
        "weaknesses": {"en": ["Cyborgs", "Beasts"], "fr": ["Cyborgs", "Bêtes"]},
        "resistances": {"en": ["Fairies", "Vampires"], "fr": ["Fées", "Vampires"]},
        "description": {"en": "A colossal steel behemoth, capable of shaking the ground beneath its weight and destroying everything in its path.", 
                        "fr": "Un colossal béhémoth d'acier, capable de faire trembler le sol sous son poids et de détruire tout sur son passage."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 45, "speed": 8, "intelligence": 12
    }),
    Monster({
        "name": {"en": "Automaton", "fr": "Automate"},
        "species": {"en": "Mechanical Monster", "fr": "Monstre Mécanique"},
        "health": 250, "level": 4,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Laser Beam", "fr": "Faisceau Laser"},
                {"en": "Self-Repair", "fr": "Auto-Réparation"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Mechanized Strike", "fr": "Frappe Mécanisée"}
            ]}
        ],
        "weaknesses": {"en": ["Cyborgs", "Beasts"], "fr": ["Cyborgs", "Bêtes"]},
        "resistances": {"en": ["Fairies", "Vampires"], "fr": ["Fées", "Vampires"]},
        "description": {"en": "A sophisticated automaton, capable of firing lasers and self-repairing, making every battle more challenging.", 
                        "fr": "Un automate sophistiqué, capable de tirer des lasers et de s'auto-réparer, rendant chaque bataille plus difficile."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 25, "speed": 15, "intelligence": 20
    }),
    Monster({
        "name": {"en": "Robo-Warrior", "fr": "Guerrier Robot"},
        "species": {"en": "Mechanical Monster", "fr": "Monstre Mécanique"},
        "health": 270, "level": 5,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Rocket Punch", "fr": "Coup de Poing Fusée"},
                {"en": "Plasma Cutter", "fr": "Coupe Plasma"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Combat Maneuver", "fr": "Manœuvre de Combat"}
            ]}
        ],
        "weaknesses": {"en": ["Cyborgs", "Beasts"], "fr": ["Cyborgs", "Bêtes"]},
        "resistances": {"en": ["Fairies", "Vampires"], "fr": ["Fées", "Vampires"]},
        "description": {"en": "A robotic warrior, wielding advanced weapons and utilizing combat techniques to annihilate its foes.", 
                        "fr": "Un guerrier robot, maniant des armes avancées et utilisant des techniques de combat pour anéantir ses ennemis."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 28, "speed": 18, "intelligence": 19
    }),
    Monster({
        "name": {"en": "Battle Drone", "fr": "Drone de Combat"},
        "species": {"en": "Mechanical Monster", "fr": "Monstre Mécanique"},
        "health": 240, "level": 4,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Missile Barrage", "fr": "Barrages de Missiles"},
                {"en": "Overload", "fr": "Surcharge"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Target Lock", "fr": "Verrouillage de Cible"}
            ]}
        ],
        "weaknesses": {"en": ["Cyborgs", "Beasts"], "fr": ["Cyborgs", "Bêtes"]},
        "resistances": {"en": ["Fairies", "Vampires"], "fr": ["Fées", "Vampires"]},
        "description": {"en": "A combat drone, capable of launching missiles with great precision, causing massive destruction.", 
                        "fr": "Un drone de combat, capable de lancer des missiles avec une grande précision, causant une destruction massive."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 22, "speed": 22, "intelligence": 17
    }),

    # Dragons
    Monster({
        "name": {"en": "Fire Dragon", "fr": "Dragon de Feu"},
        "species": {"en": "Dragon", "fr": "Dragon"},
        "health": 350, "level": 7,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Fire Breath", "fr": "Souffle de Feu"},
                {"en": "Inferno Roar", "fr": "Rugissement d'Inferno"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Tail Swipe", "fr": "Coup de Queue"}
            ]}
        ],
        "weaknesses": {"en": ["Elementals", "Demons"], "fr": ["Éléments", "Démons"]},
        "resistances": {"en": ["Angels", "Ghouls"], "fr": ["Anges", "Ghoules"]},
        "description": {"en": "A majestic fire dragon, capable of breathing devastating flames and plunging its enemies into chaos.", 
                        "fr": "Un majestueux dragon de feu, capable de cracher des flammes dévastatrices et de plonger ses ennemis dans le chaos."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 35, "speed": 20, "intelligence": 25
    }),
    Monster({
        "name": {"en": "Ice Dragon", "fr": "Dragon de Glace"},
        "species": {"en": "Dragon", "fr": "Dragon"},
        "health": 340, "level": 6,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Frost Breath", "fr": "Souffle de Froid"},
                {"en": "Icicle Spear", "fr": "Pique de Glaçon"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Wing Attack", "fr": "Attaque de Aile"}
            ]}
        ],
        "weaknesses": {"en": ["Elementals", "Demons"], "fr": ["Éléments", "Démons"]},
        "resistances": {"en": ["Angels", "Ghouls"], "fr": ["Anges", "Ghoules"]},
        "description": {"en": "A formidable ice dragon, capable of freezing its enemies with a chilling breath and crushing them with its wings.", 
                        "fr": "Un redoutable dragon de glace, capable de geler ses ennemis avec un souffle glacial et de les écraser avec ses ailes."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 34, "speed": 22, "intelligence": 24
    }),
    Monster({
        "name": {"en": "Lightning Dragon", "fr": "Dragon de Foudre"},
        "species": {"en": "Dragon", "fr": "Dragon"},
        "health": 360, "level": 7,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Thunderstorm", "fr": "Tempête de Foudre"},
                {"en": "Static Charge", "fr": "Charge Statique"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Electric Breath", "fr": "Souffle Électrique"}
            ]}
        ],
        "weaknesses": {"en": ["Elementals", "Demons"], "fr": ["Éléments", "Démons"]},
        "resistances": {"en": ["Angels", "Ghouls"], "fr": ["Anges", "Ghoules"]},
        "description": {"en": "A fast and powerful lightning dragon, capable of unleashing electric storms upon its foes.", 
                        "fr": "Un dragon de foudre rapide et puissant, capable de libérer des tempêtes électriques sur ses ennemis."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 36, "speed": 25, "intelligence": 26
    }),
    Monster({
        "name": {"en": "Earth Dragon", "fr": "Dragon de Terre"},
        "species": {"en": "Dragon", "fr": "Dragon"},
        "health": 330, "level": 6,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Stone Breath", "fr": "Souffle de Pierre"},
                {"en": "Rock Slide", "fr": "Glissement de Roche"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Quake", "fr": "Tremblement"}
            ]}
        ],
        "weaknesses": {"en": ["Elementals", "Demons"], "fr": ["Éléments", "Démons"]},
        "resistances": {"en": ["Angels", "Ghouls"], "fr": ["Anges", "Ghoules"]},
        "description": {"en": "A sturdy earth dragon, capable of causing earthquakes and fighting with the strength of nature.", 
                        "fr": "Un dragon de terre robuste, capable de provoquer des tremblements de terre et de se battre avec la force de la nature."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 38, "speed": 18, "intelligence": 22
    }),
    Monster({
        "name": {"en": "Shadow Dragon", "fr": "Dragon des Ombres"},
        "species": {"en": "Dragon", "fr": "Dragon"},
        "health": 370, "level": 8,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Dark Flame", "fr": "Flamme Noire"},
                {"en": "Nightmare Breath", "fr": "Souffle de Cauchemar"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Shadow Strike", "fr": "Frappe des Ombres"}
            ]}
        ],
        "weaknesses": {"en": ["Elementals", "Demons"], "fr": ["Éléments", "Démons"]},
        "resistances": {"en": ["Angels", "Ghouls"], "fr": ["Anges", "Ghoules"]},
        "description": {"en": "A shadow dragon, mysterious and terrifying, capable of absorbing light and plunging its enemies into darkness.", 
                        "fr": "Un dragon des ombres, mystérieux et terrifiant, capable d'absorber la lumière et de plonger ses ennemis dans l'obscurité."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 40, "speed": 19, "intelligence": 27
    }),
    Monster({
        "name": {"en": "Gold Dragon", "fr": "Dragon d'Or"},
        "species": {"en": "Dragon", "fr": "Dragon"},
        "health": 380, "level": 9,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Radiant Breath", "fr": "Souffle Éblouissant"},
                {"en": "Treasure Hoard", "fr": "Trésor Accumulé"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Golden Shield", "fr": "Bouclier Doré"}
            ]}
        ],
        "weaknesses": {"en": ["Elementals", "Demons"], "fr": ["Éléments", "Démons"]},
        "resistances": {"en": ["Angels", "Ghouls"], "fr": ["Anges", "Ghoules"]},
        "description": {"en": "A golden dragon, symbol of wealth and wisdom, capable of protecting its allies with a golden shield and breathing radiant flames.", 
                        "fr": "Un dragon doré, symbole de richesse et de sagesse, capable de protéger ses alliés avec un bouclier doré et de respirer des flammes éclatantes."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 42, "speed": 21, "intelligence": 30
    }),
    Monster({
        "name": {"en": "Silver Dragon", "fr": "Dragon d'Argent"},
        "species": {"en": "Dragon", "fr": "Dragon"},
        "health": 375, "level": 8,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Silver Breath", "fr": "Souffle d'Argent"},
                {"en": "Shimmering Strike", "fr": "Frappe Scintillante"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Glittering Shield", "fr": "Bouclier Scintillant"}
            ]}
        ],
        "weaknesses": {"en": ["Elementals", "Demons"], "fr": ["Éléments", "Démons"]},
        "resistances": {"en": ["Angels", "Ghouls"], "fr": ["Anges", "Ghoules"]},
        "description": {"en": "A silver dragon, known for its kindness and bravery, capable of launching dazzling attacks and protecting the innocent.", 
                        "fr": "Un dragon d'argent, connu pour sa bonté et son courage, capable de lancer des attaques éblouissantes et de protéger les innocents."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 41, "speed": 20, "intelligence": 28
    }),

    # Fairies
    Monster({
        "name": {"en": "Pixie", "fr": "Pixie"},
        "species": {"en": "Fairy", "fr": "Fée"},
        "health": 150, "level": 3,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Pixie Dust", "fr": "Poussière de Pixie"},
                {"en": "Fairy Flight", "fr": "Vol de Fée"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Charmed Dance", "fr": "Danse Enchantée"}
            ]}
        ],
        "weaknesses": {"en": ["Spiritual Entities", "Beasts of the Forest"], "fr": ["Entités Spirituelles", "Bêtes de la Forêt"]},
        "resistances": {"en": ["Mechanical Monsters", "Vampires"], "fr": ["Monstres Mécaniques", "Vampires"]},
        "description": {"en": "A mischievous pixie, flying lightly, using her magical dust to charm and entertain those around her.", 
                        "fr": "Un pixie espiègle, volant légèrement, utilisant sa poussière magique pour charmer et divertir ceux qui l'entourent."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 10, "speed": 25, "intelligence": 18
    }),
    Monster({
        "name": {"en": "Nymph", "fr": "Nymphe"},
        "species": {"en": "Fairy", "fr": "Fée"},
        "health": 160, "level": 4,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Nature's Grasp", "fr": "Saisie de la Nature"},
                {"en": "Enchanted Song", "fr": "Chanson Enchantée"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Healing Touch", "fr": "Toucher de Guérison"}
            ]}
        ],
        "weaknesses": {"en": ["Spiritual Entities", "Beasts of the Forest"], "fr": ["Entités Spirituelles", "Bêtes de la Forêt"]},
        "resistances": {"en": ["Mechanical Monsters", "Vampires"], "fr": ["Monstres Mécaniques", "Vampires"]},
        "description": {"en": "A graceful nymph, protector of nature, capable of healing and singing enchanting melodies.", 
                        "fr": "Une nymphe gracieuse, protectrice de la nature, capable de guérir et de chanter des mélodies envoûtantes."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 12, "speed": 22, "intelligence": 20
    }),
    Monster({
        "name": {"en": "Fairy Queen", "fr": "Reine des Fées"},
        "species": {"en": "Fairy", "fr": "Fée"},
        "health": 170, "level": 5,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Royal Command", "fr": "Commande Royale"},
                {"en": "Fairy Blessing", "fr": "Bénédiction de Fée"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Enchantment", "fr": "Enchantement"}
            ]}
        ],
        "weaknesses": {"en": ["Spiritual Entities", "Beasts of the Forest"], "fr": ["Entités Spirituelles", "Bêtes de la Forêt"]},
        "resistances": {"en": ["Mechanical Monsters", "Vampires"], "fr": ["Monstres Mécaniques", "Vampires"]},
        "description": {"en": "The fairy queen, majestic and powerful, capable of blessing her allies and casting powerful enchantments.", 
                        "fr": "La reine des fées, majestueuse et puissante, capable de bénir ses alliés et de lancer de puissants enchantements."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 14, "speed": 20, "intelligence": 25
    }),
    Monster({
        "name": {"en": "Will-o'-the-Wisp", "fr": "Lueur Fantomatique"},
        "species": {"en": "Fairy", "fr": "Fée"},
        "health": 140, "level": 2,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Light Flicker", "fr": "Clignotement de Lumière"},
                {"en": "Mystic Glow", "fr": "Lueur Mystique"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Guide", "fr": "Guide"}
            ]}
        ],
        "weaknesses": {"en": ["Spiritual Entities", "Beasts of the Forest"], "fr": ["Entités Spirituelles", "Bêtes de la Forêt"]},
        "resistances": {"en": ["Mechanical Monsters", "Vampires"], "fr": ["Monstres Mécaniques", "Vampires"]},
        "description": {"en": "A mysterious will-o'-the-wisp, wandering in the night, capable of guiding lost travelers or leading them astray.", 
                        "fr": "Une lueur fantomatique mystérieuse, errant dans la nuit, capable de guider les voyageurs perdus ou de les égarer."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 8, "speed": 24, "intelligence": 15
    }),
    Monster({
        "name": {"en": "Grove Guardian", "fr": "Gardien du Bosquet"},
        "species": {"en": "Fairy", "fr": "Fée"},
        "health": 180, "level": 4,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Nature's Shield", "fr": "Bouclier de la Nature"},
                {"en": "Forest's Embrace", "fr": "Étreinte de la Forêt"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Vine Whip", "fr": "Fouet de Vigne"}
            ]}
        ],
        "weaknesses": {"en": ["Spiritual Entities", "Beasts of the Forest"], "fr": ["Entités Spirituelles", "Bêtes de la Forêt"]},
        "resistances": {"en": ["Mechanical Monsters", "Vampires"], "fr": ["Monstres Mécaniques", "Vampires"]},
        "description": {"en": "A grove guardian, protector of the forests, using nature's magic to defend its territory.", 
                        "fr": "Un gardien du bosquet, protecteur des forêts, utilisant la magie de la nature pour défendre son territoire."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 15, "speed": 18, "intelligence": 22
    }),
    Monster({
        "name": {"en": "Fey Spirit", "fr": "Esprit Fey"},
        "species": {"en": "Fairy", "fr": "Fée"},
        "health": 155, "level": 3,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Charm", "fr": "Charme"},
                {"en": "Fey Trickery", "fr": "Fourberie Fey"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Illusion", "fr": "Illusion"}
            ]}
        ],
        "weaknesses": {"en": ["Spiritual Entities", "Beasts of the Forest"], "fr": ["Entités Spirituelles", "Bêtes de la Forêt"]},
        "resistances": {"en": ["Mechanical Monsters", "Vampires"], "fr": ["Monstres Mécaniques", "Vampires"]},
        "description": {"en": "A fey spirit, capable of deceiving and delighting, using illusion to play tricks on its enemies.", 
                        "fr": "Un esprit fey, capable de tromper et de ravir, utilisant l'illusion pour jouer des tours à ses ennemis."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 11, "speed": 21, "intelligence": 19
    }),
    Monster({
        "name": {"en": "Briar Fairy", "fr": "Fée Épineuse"},
        "species": {"en": "Fairy", "fr": "Fée"},
        "health": 165, "level": 4,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Thorn Barrage", "fr": "Barrage d'Épines"},
                {"en": "Nature's Wrath", "fr": "Colère de la Nature"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Briar Shield", "fr": "Bouclier d'Épine"}
            ]}
        ],
        "weaknesses": {"en": ["Spiritual Entities", "Beasts of the Forest"], "fr": ["Entités Spirituelles", "Bêtes de la Forêt"]},
        "resistances": {"en": ["Mechanical Monsters", "Vampires"], "fr": ["Monstres Mécaniques", "Vampires"]},
        "description": {"en": "A briar fairy, using thorns to attack and defend, in harmony with the wild nature.", 
                        "fr": "Une fée épineuse, utilisant des épines pour attaquer et défendre, en harmonie avec la nature sauvage."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 13, "speed": 19, "intelligence": 21
    }),
 
    # Undeads
    Monster({
        "name": {"en": "Skeleton", "fr": "Squelette"},
        "species": {"en": "Undead", "fr": "Mort-vivant"},
        "health": 180, "level": 3,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Bone Slash", "fr": "Coup de Os"},
                {"en": "Cursed Strike", "fr": "Frappe Maudite"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Rattle", "fr": "Secouer"}
            ]}
        ],
        "weaknesses": {"en": ["Humanoids", "Ghouls"], "fr": ["Humanoïdes", "Ghoules"]},
        "resistances": {"en": ["Angels", "Elemental Spirits"], "fr": ["Anges", "Esprits Élémentaires"]},
        "description": {"en": "An animated skeleton, wandering in the night, using its bones to attack and frighten its enemies with unsettling sounds.", 
                        "fr": "Un squelette animé, errant dans la nuit, utilisant ses os pour attaquer et effrayer ses ennemis avec des sons troublants."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 12, "speed": 18, "intelligence": 10
    }),
    Monster({
        "name": {"en": "Zombie", "fr": "Zombie"},
        "species": {"en": "Undead", "fr": "Mort-vivant"},
        "health": 200, "level": 4,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Bite", "fr": "Morsure"},
                {"en": "Claw", "fr": "Griffe"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Undead Fury", "fr": "Fureur des Morts-vivants"}
            ]}
        ],
        "weaknesses": {"en": ["Humanoids", "Ghouls"], "fr": ["Humanoïdes", "Ghoules"]},
        "resistances": {"en": ["Angels", "Elemental Spirits"], "fr": ["Anges", "Esprits Élémentaires"]},
        "description": {"en": "A slow yet relentless zombie, drawn to fresh flesh, capable of striking with brutal force.", 
                        "fr": "Un zombie lent mais implacable, attiré par la chair fraîche, capable de frapper avec une force brutale."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 14, "speed": 15, "intelligence": 8
    }),
    Monster({
        "name": {"en": "Lich", "fr": "Liche"},
        "species": {"en": "Undead", "fr": "Mort-vivant"},
        "health": 250, "level": 6,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Necromancy", "fr": "Nécromancie"},
                {"en": "Life Drain", "fr": "Drain de Vie"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Dark Magic", "fr": "Magie Noire"}
            ]}
        ],
        "weaknesses": {"en": ["Humanoids", "Ghouls"], "fr": ["Humanoïdes", "Ghoules"]},
        "resistances": {"en": ["Angels", "Elemental Spirits"], "fr": ["Anges", "Esprits Élémentaires"]},
        "description": {"en": "A terrifying lich, master of necromancy, capable of draining the life from its enemies and controlling the undead.", 
                        "fr": "Une liche terrifiante, maître de la nécromancie, capable de drainer la vie de ses ennemis et de contrôler les morts-vivants."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 20, "speed": 16, "intelligence": 30
    }),
    Monster({
        "name": {"en": "Mummy", "fr": "Momie"},
        "species": {"en": "Undead", "fr": "Mort-vivant"},
        "health": 220, "level": 5,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Wrap", "fr": "Envelopper"},
                {"en": "Despair", "fr": "Désespoir"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Curse", "fr": "Malédiction"}
            ]}
        ],
        "weaknesses": {"en": ["Humanoids", "Ghouls"], "fr": ["Humanoïdes", "Ghoules"]},
        "resistances": {"en": ["Angels", "Elemental Spirits"], "fr": ["Anges", "Esprits Élémentaires"]},
        "description": {"en": "A cursed mummy, wrapped in bandages, capable of inflicting curses and plunging its enemies into despair.", 
                        "fr": "Une momie maudite, enveloppée dans des bandages, capable d'infliger des malédictions et de plonger ses ennemis dans le désespoir."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 18, "speed": 14, "intelligence": 15
    }),
    Monster({
        "name": {"en": "Ghast", "fr": "Ghast"},
        "species": {"en": "Undead", "fr": "Mort-vivant"},
        "health": 210, "level": 4,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Rotting Touch", "fr": "Toucher Pourrissant"},
                {"en": "Chilling Grip", "fr": "Prise Glaciale"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Fear", "fr": "Peur"}
            ]}
        ],
        "weaknesses": {"en": ["Humanoids", "Ghouls"], "fr": ["Humanoïdes", "Ghoules"]},
        "resistances": {"en": ["Angels", "Elemental Spirits"], "fr": ["Anges", "Esprits Élémentaires"]},
        "description": {"en": "A putrid ghast, capable of spreading fear and weakening its enemies with its decayed touch.", 
                        "fr": "Un ghast putride, capable de répandre la peur et d'affaiblir ses ennemis avec son toucher en décomposition."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 16, "speed": 17, "intelligence": 12
    }),
    Monster({
        "name": {"en": "Vampiric Skeleton", "fr": "Squelette Vampirique"},
        "species": {"en": "Undead", "fr": "Mort-vivant"},
        "health": 230, "level": 5,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Draining Strike", "fr": "Frappe Drainante"},
                {"en": "Bone Throw", "fr": "Lancer d'Os"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Life Siphon", "fr": "Siphon de Vie"}
            ]}
        ],
        "weaknesses": {"en": ["Humanoids", "Ghouls"], "fr": ["Humanoïdes", "Ghoules"]},
        "resistances": {"en": ["Angels", "Elemental Spirits"], "fr": ["Anges", "Esprits Élémentaires"]},
        "description": {"en": "A vampiric skeleton, capable of siphoning life from its foes while attacking with its sharp bones.", 
                        "fr": "Un squelette vampirique, capable de siphonner la vie de ses ennemis tout en attaquant avec ses os aiguisés."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 19, "speed": 18, "intelligence": 17
    }),
    Monster({
        "name": {"en": "Death Knight", "fr": "Chevalier de la Mort"},
        "species": {"en": "Undead", "fr": "Mort-vivant"},
        "health": 240, "level": 6,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Dark Blade", "fr": "Lame Sombre"},
                {"en": "Necrotic Blast", "fr": "Explosion Nécrotique"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Soul Harvest", "fr": "Récolte d'Âmes"}
            ]}
        ],
        "weaknesses": {"en": ["Humanoids", "Ghouls"], "fr": ["Humanoïdes", "Ghoules"]},
        "resistances": {"en": ["Angels", "Elemental Spirits"], "fr": ["Anges", "Esprits Élémentaires"]},
        "description": {"en": "A feared death knight, wielding a dark sword and capable of harvesting the souls of its enemies with necrotic attacks.", 
                        "fr": "Un chevalier de la mort redouté, maniant une épée sombre et capable de récolter les âmes de ses ennemis avec des attaques nécrotiques."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 22, "speed": 15, "intelligence": 24
    }),

    # Beast of the forest
    Monster({
        "name": {"en": "Forest Guardian", "fr": "Gardien de la Forêt"},
        "species": {"en": "Beast of the Forest", "fr": "Bête de la Forêt"},
        "health": 220, "level": 5,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Camouflage", "fr": "Camouflage"},
                {"en": "Forest's Fury", "fr": "Fureur de la Forêt"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Nature's Wrath", "fr": "Colère de la Nature"}
            ]}
        ],
        "weaknesses": {"en": ["Elemental Spirits", "Ghosts"], "fr": ["Esprits Élémentaires", "Fantômes"]},
        "resistances": {"en": ["Demons", "Dragons"], "fr": ["Démons", "Dragons"]},
        "description": {"en": "A forest guardian, protector of the woods, capable of camouflaging itself in its environment and unleashing nature's fury upon its enemies.", 
                        "fr": "Un gardien de la forêt, protecteur des bois, capable de se camoufler dans son environnement et de déchaîner la fureur de la nature sur ses ennemis."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 24, "speed": 16, "intelligence": 20
    }),
    Monster({
        "name": {"en": "Howling Lynx", "fr": "Lynx Hurleur"},
        "species": {"en": "Beast of the Forest", "fr": "Bête de la Forêt"},
        "health": 200, "level": 4,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Howl", "fr": "Hurlement"},
                {"en": "Pounce", "fr": "Saut"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Silent Stalk", "fr": "Traque Silencieuse"}
            ]}
        ],
        "weaknesses": {"en": ["Elemental Spirits", "Ghosts"], "fr": ["Esprits Élémentaires", "Fantômes"]},
        "resistances": {"en": ["Demons", "Dragons"], "fr": ["Démons", "Dragons"]},
        "description": {"en": "A howling lynx, agile and stealthy, capable of moving silently through the woods and pouncing on its prey.", 
                        "fr": "Un lynx hurleur, agile et furtif, capable de se déplacer silencieusement à travers les bois et de sauter sur sa proie."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 18, "speed": 22, "intelligence": 15
    }),
    Monster({
        "name": {"en": "Giant Elk", "fr": "Élan Géant"},
        "species": {"en": "Beast of the Forest", "fr": "Bête de la Forêt"},
        "health": 250, "level": 6,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Charge", "fr": "Charge"},
                {"en": "Stampede", "fr": "Stampede"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Nature's Call", "fr": "Appel de la Nature"}
            ]}
        ],
        "weaknesses": {"en": ["Elemental Spirits", "Ghosts"], "fr": ["Esprits Élémentaires", "Fantômes"]},
        "resistances": {"en": ["Demons", "Dragons"], "fr": ["Démons", "Dragons"]},
        "description": {"en": "A massive elk, powerful and majestic, capable of charging at its enemies with crushing force.", 
                        "fr": "Un énorme élan, puissant et majestueux, capable de charger ses ennemis avec une force écrasante."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 26, "speed": 14, "intelligence": 12
    }),
    Monster({
        "name": {"en": "Shadow Panther", "fr": "Panthère des Ombres"},
        "species": {"en": "Beast of the Forest", "fr": "Bête de la Forêt"},
        "health": 210, "level": 5,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Stealth Attack", "fr": "Attaque Furtive"},
                {"en": "Claw", "fr": "Griffe"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Shadow Leap", "fr": "Saut des Ombres"}
            ]}
        ],
        "weaknesses": {"en": ["Elemental Spirits", "Ghosts"], "fr": ["Esprits Élémentaires", "Fantômes"]},
        "resistances": {"en": ["Demons", "Dragons"], "fr": ["Démons", "Dragons"]},
        "description": {"en": "A shadow panther, quick and silent, capable of striking its enemies by surprise and disappearing into the night.", 
                        "fr": "Une panthère des ombres, rapide et silencieuse, capable de frapper ses ennemis par surprise et de disparaître dans la nuit."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 20, "speed": 23, "intelligence": 18
    }),
    Monster({
        "name": {"en": "Elder Tree", "fr": "Arbre Ancien"},
        "species": {"en": "Beast of the Forest", "fr": "Bête de la Forêt"},
        "health": 300, "level": 7,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Root Bind", "fr": "Liaison de Racine"},
                {"en": "Wooden Grasp", "fr": "Prise en Bois"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Nature's Shield", "fr": "Bouclier de la Nature"}
            ]}
        ],
        "weaknesses": {"en": ["Elemental Spirits", "Ghosts"], "fr": ["Esprits Élémentaires", "Fantômes"]},
        "resistances": {"en": ["Demons", "Dragons"], "fr": ["Démons", "Dragons"]},
        "description": {"en": "An ancient tree, alive and powerful, capable of immobilizing its enemies with its roots and protecting the forest.", 
                        "fr": "Un arbre ancien, vivant et puissant, capable d'immobiliser ses ennemis avec ses racines et de protéger la forêt."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 35, "speed": 8, "intelligence": 16
    }),
    Monster({
        "name": {"en": "Fae Fox", "fr": "Renard Fey"},
        "species": {"en": "Beast of the Forest", "fr": "Bête de la Forêt"},
        "health": 180, "level": 3,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Illusion", "fr": "Illusion"},
                {"en": "Fey Trick", "fr": "Truc de Fey"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Quick Strike", "fr": "Frappe Rapide"}
            ]}
        ],
        "weaknesses": {"en": ["Elemental Spirits", "Ghosts"], "fr": ["Esprits Élémentaires", "Fantômes"]},
        "resistances": {"en": ["Demons", "Dragons"], "fr": ["Démons", "Dragons"]},
        "description": {"en": "A fey fox, cunning and agile, using illusions to deceive its enemies and strike quickly.", 
                        "fr": "Un renard fey, rusé et agile, utilisant des illusions pour tromper ses ennemis et frapper rapidement."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 10, "speed": 25, "intelligence": 21
    }),
    Monster({
        "name": {"en": "Vine Beast", "fr": "Bête de Vigne"},
        "species": {"en": "Beast of the Forest", "fr": "Bête de la Forêt"},
        "health": 230, "level": 5,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Vine Whip", "fr": "Fouet de Vigne"},
                {"en": "Thorny Barrage", "fr": "Barrage Épineux"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Entangle", "fr": "Enchevêtrer"}
            ]}
        ],
        "weaknesses": {"en": ["Elemental Spirits", "Ghosts"], "fr": ["Esprits Élémentaires", "Fantômes"]},
        "resistances": {"en": ["Demons", "Dragons"], "fr": ["Démons", "Dragons"]},
        "description": {"en": "A vine beast, capable of attacking with vines and ensnaring its enemies with thorny strikes.", 
                        "fr": "Une bête de vigne, capable d'attaquer avec des vignes et d'engluer ses ennemis avec des frappes épineuses."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 22, "speed": 15, "intelligence": 17
    }),

    # Demons
    Monster({
        "name": {"en": "Infernal Demon", "fr": "Démon Infernal"},
        "species": {"en": "Demon", "fr": "Démon"},
        "health": 350, "level": 8,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Hellfire", "fr": "Feu de l'Enfer"},
                {"en": "Infernal Wrath", "fr": "Colère Infernale"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Demonic Strike", "fr": "Frappe Démoniaque"}
            ]}
        ],
        "weaknesses": {"en": ["Angels", "Cyborgs"], "fr": ["Anges", "Cyborgs"]},
        "resistances": {"en": ["Fairies", "Mechanical Monsters"], "fr": ["Fées", "Monstres Mécaniques"]},
        "description": {"en": "An infernal demon, master of hellfire, capable of unleashing devastating wrath upon its enemies.", 
                        "fr": "Un démon infernal, maître du feu de l'enfer, capable de déchaîner une colère dévastatrice sur ses ennemis."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 35, "speed": 20, "intelligence": 28
    }),
    Monster({
        "name": {"en": "Shadow Demon", "fr": "Démon des Ombres"},
        "species": {"en": "Demon", "fr": "Démon"},
        "health": 300, "level": 7,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Nightmare", "fr": "Cauchemar"},
                {"en": "Cursed Shadow", "fr": "Ombre Maudite"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Shadow Strike", "fr": "Frappe des Ombres"}
            ]}
        ],
        "weaknesses": {"en": ["Angels", "Cyborgs"], "fr": ["Anges", "Cyborgs"]},
        "resistances": {"en": ["Fairies", "Mechanical Monsters"], "fr": ["Fées", "Monstres Mécaniques"]},
        "description": {"en": "A shadow demon, capable of plunging its enemies into nightmares and striking with stealthy attacks.", 
                        "fr": "Un démon des ombres, capable de plonger ses ennemis dans des cauchemars et de frapper avec des attaques furtives."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 30, "speed": 22, "intelligence": 25
    }),
    Monster({
        "name": {"en": "Succubus", "fr": "Succube"},
        "species": {"en": "Demon", "fr": "Démon"},
        "health": 280, "level": 6,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Seduction", "fr": "Séduction"},
                {"en": "Soul Drain", "fr": "Drain d'Âme"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Charm", "fr": "Charme"}
            ]}
        ],
        "weaknesses": {"en": ["Angels", "Cyborgs"], "fr": ["Anges", "Cyborgs"]},
        "resistances": {"en": ["Fairies", "Mechanical Monsters"], "fr": ["Fées", "Monstres Mécaniques"]},
        "description": {"en": "A seductive succubus, using her charm to manipulate and drain the life force from her victims.", 
                        "fr": "Une succube séduisante, utilisant son charme pour manipuler et drainer la force vitale de ses victimes."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 25, "speed": 24, "intelligence": 30
    }),
    Monster({
        "name": {"en": "Baal", "fr": "Baal"},
        "species": {"en": "Demon", "fr": "Démon"},
        "health": 400, "level": 9,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Doomsday", "fr": "Jour du Jugement"},
                {"en": "Destruction", "fr": "Destruction"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Dark Ritual", "fr": "Rituel Sombre"}
            ]}
        ],
        "weaknesses": {"en": ["Angels", "Cyborgs"], "fr": ["Anges", "Cyborgs"]},
        "resistances": {"en": ["Fairies", "Mechanical Monsters"], "fr": ["Fées", "Monstres Mécaniques"]},
        "description": {"en": "Baal, the supreme demon, capable of causing cataclysms and performing dark rituals to amplify his power.", 
                        "fr": "Baal, le démon suprême, capable de provoquer des cataclysmes et de réaliser des rituels sombres pour amplifier son pouvoir."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 40, "speed": 18, "intelligence": 35
    }),
    Monster({
        "name": {"en": "Fell Beast", "fr": "Bête Maudite"},
        "species": {"en": "Demon", "fr": "Démon"},
        "health": 320, "level": 7,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Claw", "fr": "Griffe"},
                {"en": "Dark Charge", "fr": "Charge Sombre"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Fury", "fr": "Fureur"}
            ]}
        ],
        "weaknesses": {"en": ["Angels", "Cyborgs"], "fr": ["Anges", "Cyborgs"]},
        "resistances": {"en": ["Fairies", "Mechanical Monsters"], "fr": ["Fées", "Monstres Mécaniques"]},
        "description": {"en": "A cursed beast, capable of striking with brute force and charging at its enemies in a frenzy of rage.", 
                        "fr": "Une bête maudite, capable de frapper avec force brute et de charger ses ennemis dans une frénésie de rage."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 28, "speed": 19, "intelligence": 18
    }),
    Monster({
        "name": {"en": "Hellspawn", "fr": "Enfant de l'Enfer"},
        "species": {"en": "Demon", "fr": "Démon"},
        "health": 290, "level": 6,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Fireball", "fr": "Boulet de Feu"},
                {"en": "Demonic Howl", "fr": "Hurlement Démoniaque"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Inferno", "fr": "Inferno"}
            ]}
        ],
        "weaknesses": {"en": ["Angels", "Cyborgs"], "fr": ["Anges", "Cyborgs"]},
        "resistances": {"en": ["Fairies", "Mechanical Monsters"], "fr": ["Fées", "Monstres Mécaniques"]},
        "description": {"en": "A child of darkness, capable of launching fireballs and howling to terrify its enemies.", 
                        "fr": "Un enfant des ténèbres, capable de lancer des boulets de feu et de hurler pour terrifier ses ennemis."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 22, "speed": 21, "intelligence": 16
    }),
    Monster({
        "name": {"en": "Cursed Spirit", "fr": "Esprit Maudit"},
        "species": {"en": "Demon", "fr": "Démon"},
        "health": 270, "level": 5,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Wail", "fr": "Gémissement"},
                {"en": "Dark Blessing", "fr": "Bénédiction Sombre"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Curse", "fr": "Malédiction"}
            ]}
        ],
        "weaknesses": {"en": ["Angels", "Cyborgs"], "fr": ["Anges", "Cyborgs"]},
        "resistances": {"en": ["Fairies", "Mechanical Monsters"], "fr": ["Fées", "Monstres Mécaniques"]},
        "description": {"en": "A cursed spirit, capable of cursing its enemies with piercing wails and invoking dark blessings.", 
                        "fr": "Un esprit maudit, capable de maudire ses ennemis avec des gémissements perçants et d'invoquer des bénédictions sombres."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 20, "speed": 17, "intelligence": 22
    }),

    # Angels
    Monster({
        "name": {"en": "Seraphim", "fr": "Séraphin"},
        "species": {"en": "Angel", "fr": "Ange"},
        "health": 400, "level": 9,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Divine Light", "fr": "Lumière Divine"},
                {"en": "Celestial Shield", "fr": "Bouclier Céleste"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Holy Smite", "fr": "Frappe Sacrée"}
            ]}
        ],
        "weaknesses": {"en": ["Demons", "Undead"], "fr": ["Démons", "Morts-vivants"]},
        "resistances": {"en": ["Elementals", "Beasts"], "fr": ["Éléments", "Bêtes"]},
        "description": {"en": "A majestic seraphim, bearer of divine light, capable of inflicting sacred blows and protecting the innocent with its celestial shield.", 
                        "fr": "Un séraphin majestueux, porteur de lumière divine, capable d'infliger des coups sacrés et de protéger les innocents avec son bouclier céleste."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 38, "speed": 22, "intelligence": 30
    }),
    Monster({
        "name": {"en": "Cherub", "fr": "Chérubin"},
        "species": {"en": "Angel", "fr": "Ange"},
        "health": 300, "level": 7,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Ethereal Shield", "fr": "Bouclier Éthéré"},
                {"en": "Divine Protection", "fr": "Protection Divine"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Healing Light", "fr": "Lumière de Guérison"}
            ]}
        ],
        "weaknesses": {"en": ["Demons", "Undead"], "fr": ["Démons", "Morts-vivants"]},
        "resistances": {"en": ["Elementals", "Beasts"], "fr": ["Éléments", "Bêtes"]},
        "description": {"en": "A playful cherub, capable of creating ethereal shields and spreading healing light to those in need.", 
                        "fr": "Un chérubin espiègle, capable de créer des boucliers éthérés et de répandre une lumière de guérison à ceux qui en ont besoin."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 30, "speed": 24, "intelligence": 26
    }),
    Monster({
        "name": {"en": "Archangel", "fr": "Archange"},
        "species": {"en": "Angel", "fr": "Ange"},
        "health": 350, "level": 8,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Holy Wrath", "fr": "Colère Sacrée"},
                {"en": "Light of Justice", "fr": "Lumière de la Justice"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Divine Intervention", "fr": "Intervention Divine"}
            ]}
        ],
        "weaknesses": {"en": ["Demons", "Undead"], "fr": ["Démons", "Morts-vivants"]},
        "resistances": {"en": ["Elementals", "Beasts"], "fr": ["Éléments", "Bêtes"]},
        "description": {"en": "A powerful archangel, capable of unleashing divine wrath and intervening in battles to bring justice.", 
                        "fr": "Un archange puissant, capable de déchaîner la colère divine et d'intervenir dans les batailles pour apporter la justice."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 36, "speed": 20, "intelligence": 32
    }),
    Monster({
        "name": {"en": "Guardian Angel", "fr": "Ange Gardien"},
        "species": {"en": "Angel", "fr": "Ange"},
        "health": 320, "level": 7,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Protective Aura", "fr": "Aura de Protection"},
                {"en": "Light Beam", "fr": "Faisceau de Lumière"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Rescue", "fr": "Sauvetage"}
            ]}
        ],
        "weaknesses": {"en": ["Demons", "Undead"], "fr": ["Démons", "Morts-vivants"]},
        "resistances": {"en": ["Elementals", "Beasts"], "fr": ["Éléments", "Bêtes"]},
        "description": {"en": "A guardian angel, protector of souls, capable of creating a protective aura and rescuing those in danger.", 
                        "fr": "Un ange gardien, protecteur des âmes, capable de créer une aura de protection et de sauver ceux en danger."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 34, "speed": 18, "intelligence": 28
    }),
    Monster({
        "name": {"en": "Celestial Being", "fr": "Être Céleste"},
        "species": {"en": "Angel", "fr": "Ange"},
        "health": 280, "level": 6,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Light Burst", "fr": "Éclat de Lumière"},
                {"en": "Radiant Shield", "fr": "Bouclier Radieux"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Heavenly Strike", "fr": "Frappe Céleste"}
            ]}
        ],
        "weaknesses": {"en": ["Demons", "Undead"], "fr": ["Démons", "Morts-vivants"]},
        "resistances": {"en": ["Elementals", "Beasts"], "fr": ["Éléments", "Bêtes"]},
        "description": {"en": "A celestial being, radiating light, capable of striking with the power of the heavens and protecting with a radiant shield.", 
                        "fr": "Un être céleste, rayonnant de lumière, capable de frapper avec la puissance des cieux et de protéger avec un bouclier radieux."},
        "rarity": {"en": "common", "fr": "commun"},
        "defense": 28, "speed": 19, "intelligence": 25
    }),
    Monster({
        "name": {"en": "Angel of Justice", "fr": "Ange de la Justice"},
        "species": {"en": "Angel", "fr": "Ange"},
        "health": 360, "level": 8,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Judgment", "fr": "Jugement"},
                {"en": "Divine Shield", "fr": "Bouclier Divin"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Smite", "fr": "Frappe"}
            ]}
        ],
        "weaknesses": {"en": ["Demons", "Undead"], "fr": ["Démons", "Morts-vivants"]},
        "resistances": {"en": ["Elementals", "Beasts"], "fr": ["Éléments", "Bêtes"]},
        "description": {"en": "An angel of justice, wielding the power of judgment, capable of striking its foes with divine attacks.", 
                        "fr": "Un ange de la justice, maniant le pouvoir du jugement, capable de frapper ses ennemis avec des attaques divines."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 37, "speed": 21, "intelligence": 29
    }),
    Monster({
        "name": {"en": "Lightbringer", "fr": "Porteur de Lumière"},
        "species": {"en": "Angel", "fr": "Ange"},
        "health": 370, "level": 8,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Radiant Shield", "fr": "Bouclier Radieux"},
                {"en": "Light of Hope", "fr": "Lumière d'Espoir"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Purifying Flame", "fr": "Flamme Purificatrice"}
            ]}
        ],
        "weaknesses": {"en": ["Demons", "Undead"], "fr": ["Démons", "Morts-vivants"]},
        "resistances": {"en": ["Elementals", "Beasts"], "fr": ["Éléments", "Bêtes"]},
        "description": {"en": "A bringer of light, capable of purifying darkness with sacred flames and inspiring hope in the oppressed.", 
                        "fr": "Un porteur de lumière, capable de purifier l'obscurité avec des flammes sacrées et d'inspirer l'espoir chez les opprimés."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 39, "speed": 20, "intelligence": 31
    }),

# Mythical creatures
    Monster({
        "name": {"en": "Unicorn", "fr": "Licorne"},
        "species": {"en": "Mythical Creature", "fr": "Créature Mythique"},
        "health": 300, "level": 7,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Healing Touch", "fr": "Toucher Guérisseur"},
                {"en": "Celestial Blessing", "fr": "Bénédiction Céleste"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Horn Charge", "fr": "Charge de Corne"}
            ]}
        ],
        "weaknesses": {"en": ["Dragons", "Elementals"], "fr": ["Dragons", "Éléments"]},
        "resistances": {"en": ["Aliens", "Ghosts"], "fr": ["Aliens", "Fantômes"]},
        "description": {"en": "A legendary unicorn, symbol of purity, capable of healing wounds and bringing celestial blessings to the worthy.", 
                        "fr": "Une licorne légendaire, symbole de pureté, capable de guérir les blessures et d'apporter des bénédictions célestes aux dignes."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 25, "speed": 22, "intelligence": 25
    }),
    Monster({
        "name": {"en": "Griffin", "fr": "Griffon"},
        "species": {"en": "Mythical Creature", "fr": "Créature Mythique"},
        "health": 320, "level": 6,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Claw Attack", "fr": "Attaque de Griffe"},
                {"en": "Talon Strike", "fr": "Coup de Serre"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Flight", "fr": "Vol"}
            ]}
        ],
        "weaknesses": {"en": ["Dragons", "Elementals"], "fr": ["Dragons", "Éléments"]},
        "resistances": {"en": ["Aliens", "Ghosts"], "fr": ["Aliens", "Fantômes"]},
        "description": {"en": "A majestic griffin, a blend of lion and eagle, capable of flying with agility and attacking with powerful claws.", 
                        "fr": "Un griffon majestueux, mélange de lion et d'aigle, capable de voler avec agilité et d'attaquer avec des griffes puissantes."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 30, "speed": 25, "intelligence": 22
    }),
    Monster({
        "name": {"en": "Phoenix", "fr": "Phoenix"},
        "species": {"en": "Mythical Creature", "fr": "Créature Mythique"},
        "health": 340, "level": 8,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Fire Rebirth", "fr": "Renaissance de Feu"},
                {"en": "Ember Burst", "fr": "Explosion de Braises"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Flame Wings", "fr": "Ailes de Flammes"}
            ]}
        ],
        "weaknesses": {"en": ["Dragons", "Elementals"], "fr": ["Dragons", "Éléments"]},
        "resistances": {"en": ["Aliens", "Ghosts"], "fr": ["Aliens", "Fantômes"]},
        "description": {"en": "A flamboyant phoenix, capable of rebirthing from its ashes, using fire to inflict damage and elevate its spirit into the skies.", 
                        "fr": "Un phoenix flamboyant, capable de renaître de ses cendres, utilisant le feu pour infliger des dégâts et élever son esprit dans les cieux."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 28, "speed": 24, "intelligence": 27
    }),
    Monster({
        "name": {"en": "Chimera", "fr": "Chimère"},
        "species": {"en": "Mythical Creature", "fr": "Créature Mythique"},
        "health": 350, "level": 9,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Fire Breath", "fr": "Souffle de Feu"},
                {"en": "Beastly Roar", "fr": "Rugissement Bestial"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Tail Swipe", "fr": "Coup de Queue"}
            ]}
        ],
        "weaknesses": {"en": ["Dragons", "Elementals"], "fr": ["Dragons", "Éléments"]},
        "resistances": {"en": ["Aliens", "Ghosts"], "fr": ["Aliens", "Fantômes"]},
        "description": {"en": "A terrifying chimera, a blend of multiple beasts, capable of breathing fire and attacking with beastly strength.", 
                        "fr": "Une chimère terrifiante, mélange de plusieurs bêtes, capable de cracher du feu et d'attaquer avec une force bestiale."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 32, "speed": 20, "intelligence": 24
    }),
    Monster({
        "name": {"en": "Hydra", "fr": "Hydre"},
        "species": {"en": "Mythical Creature", "fr": "Créature Mythique"},
        "health": 360, "level": 8,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Regenerate", "fr": "Régénérer"},
                {"en": "Hydra's Fury", "fr": "Fureur de l'Hydre"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Multiple Heads", "fr": "Têtes Multiples"}
            ]}
        ],
        "weaknesses": {"en": ["Dragons", "Elementals"], "fr": ["Dragons", "Éléments"]},
        "resistances": {"en": ["Aliens", "Ghosts"], "fr": ["Aliens", "Fantômes"]},
        "description": {"en": "A multi-headed hydra, capable of regenerating its wounds and inflicting devastating fury upon anyone who approaches.", 
                        "fr": "Une hydre à plusieurs têtes, capable de régénérer ses blessures et d'infliger une fureur dévastatrice à quiconque s'approche."},
        "rarity": {"en": "legendary", "fr": "légendaire"},
        "defense": 34, "speed": 19, "intelligence": 23
    }),
    Monster({
        "name": {"en": "Minotaur", "fr": "Minotaure"},
        "species": {"en": "Mythical Creature", "fr": "Créature Mythique"},
        "health": 330, "level": 7,
        "attack_types": [
            {"type": {"en": "physical", "fr": "physique"}, "moves": [
                {"en": "Charge", "fr": "Charge"},
                {"en": "Bull Rush", "fr": "Charge de Taureau"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Maze Mastery", "fr": "Maîtrise du Labyrinthe"}
            ]}
        ],
        "weaknesses": {"en": ["Dragons", "Elementals"], "fr": ["Dragons", "Éléments"]},
        "resistances": {"en": ["Aliens", "Ghosts"], "fr": ["Aliens", "Fantômes"]},
        "description": {"en": "A powerful minotaur, guardian of the labyrinths, capable of charging with force and mastering its environment with cunning.", 
                        "fr": "Un minotaure puissant, gardien des labyrinthes, capable de charger avec force et de maîtriser son environnement avec ruse."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 29, "speed": 18, "intelligence": 20
    }),
    Monster({
        "name": {"en": "Sphinx", "fr": "Sphinx"},
        "species": {"en": "Mythical Creature", "fr": "Créature Mythique"},
        "health": 310, "level": 6,
        "attack_types": [
            {"type": {"en": "magic", "fr": "magie"}, "moves": [
                {"en": "Riddle", "fr": "Devinette"},
                {"en": "Guardian's Challenge", "fr": "Défi du Gardien"}
            ]},
            {"type": {"en": "spiritual", "fr": "spirituel"}, "moves": [
                {"en": "Claw Attack", "fr": "Attaque de Griffe"}
            ]}
        ],
        "weaknesses": {"en": ["Dragons", "Elementals"], "fr": ["Dragons", "Éléments"]},
        "resistances": {"en": ["Aliens", "Ghosts"], "fr": ["Aliens", "Fantômes"]},
        "description": {"en": "An enigmatic sphinx, keeper of secrets, capable of posing riddles and attacking with its sharp claws.", 
                        "fr": "Un sphinx énigmatique, gardien des secrets, capable de poser des devinettes et d'attaquer avec ses griffes acérées."},
        "rarity": {"en": "rare", "fr": "rare"},
        "defense": 27, "speed": 21, "intelligence": 29
    }),
