import json

class Localization:
    def __init__(self, default_language='en'):
        self.current_language = default_language
        self.translations = {}
        self.load_translations('en')  
        self.load_translations('fr')

    def load_translations(self, language):
        """Load translations from a JSON file for the specified language."""
        try:
            with open(f'translations_{language}.json', 'r', encoding='utf-8') as file:
                self.translations[language] = json.load(file)
                # print(f"Loaded translations for {language}: {self.translations[language]}")  # Debug
        except FileNotFoundError:
            # print(f"Translation file for '{language}' not found.")  # Debug
            pass
        except json.JSONDecodeError:
            # print(f"Error decoding JSON from the translation file for '{language}'.")  # Debug
            pass

    def switch_language(self, language):
        """Switch to a different language and load its translations."""
        if language in self.translations:
            self.current_language = language
            # print(f"Switched to language: {language}.")  # Debug
        else:
            # print(f"Language '{language}' not loaded.")  # Debug
            pass

    def get_translation(self, key):
        """Get the translation for a given key, supporting nested keys."""
        keys = key.split('.')
        translation = self.translations.get(self.current_language, {})

        for subkey in keys:
            if isinstance(translation, dict):
                translation = translation.get(subkey)
                if translation is None:
                    # print(f"Key '{subkey}' not found in translations.")  # Debug
                    return key 
            elif isinstance(translation, list):
                try:
                    index = int(subkey)
                    translation = translation[index]
                except (ValueError, IndexError):
                    # print(f"Key '{subkey}' is not a valid index for the list.")  # Debug
                    return key 
            else:
                # print(f"Unexpected type for translation: {type(translation)}")  # Debug
                return key 

        if isinstance(translation, str):
            return translation 
        elif translation is None:
            # print(f"Translation for '{key}' is None.")  # Debug
            return key  
        else:
            # print(f"Final translation is not a string: {translation}")  # Debug
            return key  

    def save_translations(self, language):
        """Save the current translations to a JSON file for the specified language."""
        with open(f'translations_{language}.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.translations, json_file, indent=4)
            # print(f"Saved translations for {language}.")  # Debug

"""
# To use
localization = Localization()
localization.save_translations('en') # To save english translation
localization.switch_language('fr') #To switch
localization.save_translations('fr') # to save french translation

"""