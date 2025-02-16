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
    
    def switch_language(self, language):
        """To switch to a different language and load the correct translations."""
        if language in self.translations:
            self.current_language = language
            # print(f"Switched to language: {language}.") # debug
        else:
            #print (f"Language {language} not loaded.") # debug
            pass
    
    def get_translation(self, key):
        """To get the translation for a given key, supporting nested keys."""
        keys = key.split('.')
        translation = self.translations.get(self.current_language, {})

        for subkey in keys:
            if isinstance(translation, dict):
                translation = translation.get(subkey)
                if translation is None:
                    # print(f"key {subkey} not found in translations.") # debug
                    return key
                elif isinstance(translation, list):
                    try:
                        index = int(subkey)
                        translation = translation [index]
                    except (ValueError, IndexError):
                        # print(f"key {subkey} is not a valid index for the list.") # debug
                        return key    
                else:
                    #print (f"Unexpected type for translation: {type(translation)}") # debug
                    return key

        if isinstance(translation, str):
            return translation
        elif translation is None:
            #print(f"Translation for {key} is None.") # debug
            return key
        else:
            #print("Final translation is not a string : {translation}") # debug
            return key               