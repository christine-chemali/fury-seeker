import json

class Localization:
    def __init__(self, default_language = 'en'):
        self.current_language = default_language
        self.translations = {}
        self.load_translation('en')
        self.load_translation('fr')
    
    def load_translations(self,language):
        """To load translatinons from Json file for the specified language"""
        try:
            with open(f"translations_{language}.json", 'r', encoding = 'utf-8') as file:
                self.translations[language] = json.load(file)
                # print(f"loaded translations for {language}: {self.translations[language]}") # debug
        except FileNotFoundError:
            # print(f"Translation file for '{language}' not found.")  # debug
            pass
        except json.JSONDecodeError:
            # print(f"Error decoding from the translation file for '{language}'.") # debug
            pass
            
