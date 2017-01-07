import json
import os
from geopy.distance import vincenty
from geopy.geocoders import Nominatim

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath,'r') as json_file:
        return json.load(json_file)


def get_biggest_bar(data):
    max_bar = max(data, key=lambda item:item['SeatsCount'])
    return max_bar


def calc_distance(data):
    current_location = (latitude, longitude)
    bar_location = (float (data['Latitude_WGS84']), float(data['Longitude_WGS84']))
    distance = vincenty(current_location, bar_location).meters       
    return distance
    
    
def get_smallest_bar(data):
    min_bar = min(data, key =lambda item:item['SeatsCount'])
    return min_bar


def get_closest_bar(data, latitude, longitude):
    res = min(data, key = calc_distance)
    return res

    
if __name__ == '__main__':
    filepath = input("Введите путь к файлу: ")
    latitude = float(input("Введите широту: "))
    longitude = float(input ("Введите долготу: "))
    bars = load_data(filepath)
    
    if bars is None:
        print("Файла или папки с таким названием не существует.")
    else:
        geolocator = Nominatim()
        current_location = geolocator.reverse("{},{} ".format(latitude, longitude))
        closest_bar = get_closest_bar(bars,latitude, longitude)
        smallest_bar = get_smallest_bar(bars)
        biggest_bar = get_biggest_bar(bars)
        
        print("Введенный адрес: {}".format(current_location.address))
        print('Самый маленький бар: {} Адрес: {} '.format(smallest_bar['Name'],
                                                          smallest_bar['Address']))
        print('Самый большой бар: {} Адрес: {} '.format(biggest_bar['Name'],
                                                        biggest_bar['Address']))
        print('Ближайший бар: {} Адрес: {} '.format(closest_bar['Name'],
                                                    closest_bar['Address']))
        