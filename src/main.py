import argparse
import csv
import response
import urllib3 as urllib3
from locate_coffee_shop import locate_closest_coffee_shops


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("X", type=float, help="Provide the user x coordinate")
    parser.add_argument("Y", type=float, help="Provide the user y coordinate")
    parser.add_argument("shops_url", type=str, help="Provide the shop data url")
    args = parser.parse_args()

    user_loc = [args.x, args.y]

    http = urllib3.PoolManager()
    response = http.request('GET', args.shops_url)
    if response.status != 200:  # checking for the OK status
        print(f"The URL you provided generated a code {response.status}: {response.reason}")
        exit()

    csv_file = csv.reader(response.data.decode('utf-8').split("\n"))
    coffee_shops = list(csv_file)
    coffee_shops = locate_closest_coffee_shops(user_loc, coffee_shops)

    for shop in coffee_shops:
        print(f"{shop.name},{shop.distance}")