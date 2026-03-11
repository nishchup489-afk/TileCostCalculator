import math

tiles_price = float(input("Enter your preferred tile price (each): "))
tile_area = float(input("Enter tile area (sq ft): "))
room_width = float(input("Enter room width (ft): "))
room_height = float(input("Enter room height (ft): "))


def calculate_cost(tile_price, tile_area, room_width, room_height):

    room_area = room_width * room_height

    tiles_needed = math.ceil(room_area / tile_area)

    total_cost = tiles_needed * tile_price

    return tiles_needed, total_cost


tiles, cost = calculate_cost(
    tiles_price,
    tile_area,
    room_width,
    room_height
)

print(f"\nTiles Needed: {tiles}")
print(f"Total Cost: ${cost}")