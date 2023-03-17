def core(translations):
    print(f"core translations: {translations}")

def basic(translations):
    print(f"basic translations: {translations}")

def advanced(translations):
    print(f"advanced translations: {translations}")

types = {
    "core": {"filename": "core_translations.txt", "function": core},
    "basic": {"filename": "basic_translations.txt", "function": basic},
    "advanced": {"filename": "advanced_translations.txt", "function": advanced},
}

def get_translation_level():
    while True:
        type = input(
            "what translation level should the compiler use? 'core' 'basic' 'advanced': "
        )
        if type.lower() in types:
            break
        print("invalid level ")
    return type.lower()

def start_compiler_type(type):
    with open(f"src\\translations\\{types[type]['filename']}", "r") as file:
        translations = file.readlines()
        types[type]["function"](translations)

start_compiler_type(get_translation_level())
