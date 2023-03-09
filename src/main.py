import argparse
import csv
import requests
from contextlib import closing
from codecs import iterdecode
from locate_coffee_shop import locate_closest_coffee_shops


if __name__ == '__main__':

    #parser initialization in order to add custom arguments
    #parser creation
    parser = argparse.ArgumentParser()
    #added arguments (command line field name, variable type )
    parser.add_argument("user_x", type=float)
    parser.add_argument("user_y", type=float)
    parser.add_argument("shops_url", type=str)
    #parse the argument
    args = parser.parse_args()
    #save input user coordinates in user_loc variable
    user_loc = [args.user_x, args.user_y]
    #use requests in order to get the http request of the provided URL
    with requests.get(args.shops_url, stream=True) as r:
        lines = (line.decode('utf-8') for line in r.iter_lines())
        csv_coffee_shops = []
        for row in csv.reader(lines):
            csv_coffee_shops.append(row)
        # locate the three closest coffee shops from the user location
        coffee_shops = locate_closest_coffee_shops(user_loc,csv_coffee_shops)
    #print the three closest coffee shops from the user location
    for shop in coffee_shops:
        print(f"{shop.name},{shop.distance}")