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


def load_pokemons(file_name):

    try:

        file = open(file_name, "r")
        pokemons = json.load(file)
        file.close()
        return pokemons

    except FileNotFoundError:
        print("Archivo no encontrado. Se creará uno nuevo.")
        return []

    except json.JSONDecodeError:
        print("El archivo JSON está vacío o tiene formato incorrecto.")
        return []


def create_pokemon():
    name = get_text("Nombre del Pokemon: ")
    pokemon_type = get_text("Tipo del Pokemon: ")
    return {
        "name": name,
        "type": pokemon_type
    }


def save_pokemons(file_name, pokemons):

    try:
        file = open(file_name, "w")
        json.dump(
            pokemons,
            file,
            indent=4
        )
        file.close()
        print("Pokemon agregado correctamente!!")

    except Exception as error:
        print(f"Ocurrió un error al guardar el archivo: {error}")


def main():

    file_name = "pokemon.json"
    pokemons = load_pokemons(file_name)
    new_pokemon = create_pokemon()
    pokemons.append(new_pokemon)
    save_pokemons(file_name, pokemons)


main()