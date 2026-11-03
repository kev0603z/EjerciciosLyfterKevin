import json

def get_text(prompt):

    while True:
        text = input(prompt).strip()
        if text == "":
            print("Error: no puede dejar el campo vacío.")
        elif text.isdigit():
            print("Error: debe ingresar texto y no números.")
        else:
            return text
        

try:

    file = open("pokemon.json", "r")
    pokemons = json.load(file)
    file.close()
except FileNotFoundError:
    print("Archivo no encontrado. Se creará uno nuevo.")
    pokemons = []
except json.JSONDecodeError:
    print("El archivo JSON está vacío o tiene formato incorrecto.")
    pokemons = []


name = get_text("Nombre del Pokemon: ")

pokemon_type = get_text("Tipo del Pokemon: ")

new_pokemon = {
    "name": name,
    "type": pokemon_type
}

pokemons.append(new_pokemon)

try:

    file = open("pokemon.json", "w")

    json.dump(
        pokemons,
        file,
        indent=4
    )
    file.close()
    print("Pokemon agregado correctamente!! ")

except Exception as error:

    print(f"Ocurrió un error al guardar el archivo: {error}")