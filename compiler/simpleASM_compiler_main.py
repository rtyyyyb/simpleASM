
types = ["core","basic","advanced"]
type_pass = False
while type_pass == False:
    type = input("what translation level should the compiler use? 'core' 'basic' 'advanced': ")
    if type.lower() not in types:
        print("invalid level ")
        type_pass = False
    else:
        type_pass = True
def startup(type):
    if type.lower() == "core":
        with open("core translations.txt","r") as file:
            translations = file.readlines()
            core(translations)
    if type.lower() == "basic":
        with open("basic translations.txt","r") as file:
            translations = file.readlines()
            basic(translations)
    if type.lower() == "advanced":
        with open("advanced translations.txt","r") as file:
            translations = file.readlines()
            advanced(translations)
def core(translations):
    with open("program.txt","r") as program:
        lines = program.readlines()
def basic(translations):
    with open("program.txt","r") as program:
        lines = program.readlines()
def advanced(translations):
    with open("program.txt","r") as program:
        lines = program.readlines()
