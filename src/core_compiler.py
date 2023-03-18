def core_compile(translations):
    get_translations(translations)

translation_identifyers = [
    "ADD (A,B,RETURN) : {",
    "NOR (A,B,RETURN) : {",
    "LOAD (RAM ADDRESS,DESTINATION) : {",
    "STORE (SOURCE,RAM ADDRESS) : {",
    "JUMP IF GREATER (A,B,LABEL) : {",
    "IMM (VALUE,DESTINATION) : {",
    "RIGHT SHIFT (SOURCE,RETURN) : {"
]

final_translations = []
def get_translations(translations):
    for line in translations:
        if line in translation_identifyers and line != "}":
            final_translations.append(line)
    print(line)
