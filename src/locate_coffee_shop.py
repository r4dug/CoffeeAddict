from scipy.spatial import distance
from collections import namedtuple

ProximateCoffeeShop = namedtuple("CoffeeShop", "name distance")

"""
Function that locates the closest coffee shop locations from the user's location.
:param user_location: is a tuple of 2 floats representing the x and y coordinates
:param coffee_shops: represents the coffee shop's name along it's X and Y coordinates in a tuple
:return: the closest 3 coffee shops
"""
def locate_closest_coffee_shops(user_location, coffee_shops):
    shops = []
    for row, shop_data in enumerate(coffee_shops, 1):
        try:
            shop_name, user_x, user_y = shop_data
            x = float(user_x)
            y = float(user_y)
            # find distance between two points
            shop_distance = round(distance.euclidean(user_location, [x, y]), 4)
            shops.append(ProximateCoffeeShop(shop_name, shop_distance))
        except ValueError as err:
            print(f"Execution stopped. The following error occurred: {err} at row {row}")
    # sort the coffee shops by distance
    sorted_shops = sorted(shops, key=lambda asc: asc.distance)
    return sorted_shops[:3]