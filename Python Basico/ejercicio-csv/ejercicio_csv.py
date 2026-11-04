import csv

def get_amount_games():
    while True:
        try:
            return int(input("Digite cuántos videojuegos desea registrar: "))
        except ValueError:
            print("Error: debe ingresar un número entero.")


def get_text(prompt):

    while True:
        text = input(prompt)
        if text.isdigit():
            print("Error: debe ingresar letras.")
        else:
            return text


def save_games_to_csv(file_name):
    amount_games = get_amount_games()
    file = open(file_name, "w", newline="")
    writer = csv.writer(file)
    writer.writerow(["nombre", "genero", "desarrollador", "clasificacion"])

    for index in range(amount_games):
        print(f"\nVideojuego #{index + 1}")

        name = get_text("Nombre: ")
        genre = get_text("Genero: ")
        developer = get_text("Desarrollador: ")
        esrb = get_text("Clasificacion ESRB: ")

        writer.writerow([name, genre, developer, esrb])

    file.close()

    print("\nRegistro creado correctamente!!!")


def save_games_to_tsv(file_name):
    amount_games = get_amount_games()
    file = open(file_name, "w", newline="")
    writer = csv.writer(file, delimiter="\t")
    writer.writerow(["nombre", "genero", "desarrollador", "clasificacion"])

    for index in range(amount_games):
        print(f"\nVideojuego #{index + 1}")

        name = get_text("Nombre: ")
        genre = get_text("Genero: ")
        developer = get_text("Desarrollador: ")
        esrb = get_text("Clasificacion ESRB: ")

        writer.writerow([name, genre, developer, esrb])

    file.close()

    print("\nRegistro con tabulaciones creado correctamente!!!")


save_games_to_csv("video_games.csv")

save_games_to_tsv("video_games_tab.tsv")