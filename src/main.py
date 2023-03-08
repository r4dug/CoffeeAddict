import argparse
import csv
import urllib3 as urllib3
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
    #use urllib3 in order to get the http request of the provided URL
    http = urllib3.PoolManager()
    response = http.request('GET', args.shops_url)
    #check for the HTTP 200 OK status that indicates the request succeeded
    if response.status != 200:
        print(f"The URL you provided generated a code {response.status}: {response.reason}")
        exit()
    #read the csv file found at the particular location
    csv_file = csv.reader(response.data.decode('utf-8').split("\n"))
    #return the content of the csv file in a list
    coffee_shops = list(csv_file)
    #locate the three closest coffee shops from the user location
    coffee_shops = locate_closest_coffee_shops(user_loc, coffee_shops)
    #print the three closest coffee shops from the user location
    for shop in coffee_shops:
        print(f"{shop.name},{shop.distance}")