import math
from collections import namedtuple

ProximateCoffeeShop = namedtuple("CoffeeShop", "name distance")

"""
Function that calculates the distance between two points, which is an application of the Pythagorean theorem.
:param x1: represents X coordinate of the 1st point
:param x2: represents X coordinate of the 2nd point
:param y1: represents Y coordinate of the 1st point
:param y2: represents Y coordinate of the 2nd point
:return: the result of the distance between two points
"""
def get_distance_between_two_points(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

"""
Function that locates the closest coffee shop locations from the user's location.
:param user_x: represents user's X coordinate
:param user_y: represents user's Y coordinate
:param coffee_shops: represents the coffee shop's name along it's X and Y coordinates in a tuple
:return: the closest 3 coffee shops
"""
def locate_closest_coffee_shops(user_x, user_y, coffee_shops):
    shops = []
    for shop in coffee_shops:
        try:
            # find distance between two points
            shop_distance = get_distance_between_two_points(user_x, user_y, shop[1], shop[2])
            shops.append(ProximateCoffeeShop(shop[0], shop_distance))
        except ValueError as err:
            print(f"Execution stopped. The following error occurred: {err}")
    # sort the coffee shops by distance
    shops.sort(key=lambda asc: asc.distance)
    return shops[:3]
