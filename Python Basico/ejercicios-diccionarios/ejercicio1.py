##1. Cree un diccionario que guarde la siguiente información sobre un hotel:


hotel = {
    "name": "Fiesta Resort",
    "quality_stars": 4,
    "rooms": [
        {"number": 12, "floor": 15, "price_night": 2500},
        {"number": 13, "floor": 17, "price_night": 2700},
        {"number": 14, "floor": 16, "price_night": 3000}
    ]
}

for room in hotel["rooms"]:
    print(f'Habitación : {room["number"]}, piso : {room["floor"]}, precio por noche : {room["price_night"]}')
