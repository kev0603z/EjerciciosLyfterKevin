def read_songs(file_name):
    song_list = []

    file = open(file_name, "r")

    for text in file:
        song_list.append(text.strip())

    file.close()

    return song_list

def sort_songs(song_list):
    song_list.sort()
    return song_list

def save_songs(file_name, song_list):
    file = open(file_name, "w")

    for song in song_list:
        file.write(song + "\n")

    file.close()

def main(input_file, output_file):

    songs = read_songs(input_file)

    songs = sort_songs(songs)

    save_songs(output_file, songs)

main("canciones.txt", "canciones_ordenadas.txt")
