from math import acos, sin, cos, radians

def input_points():
    print("Enter the names, latitudes and longitudes of two points on the Earth in degrees!")
    name1 = input("Point one name: ")
    lat_1 = radians(float(input("Point one latitude: ")))
    long_1 = radians(float(input("Point one longitude: ")))
    name2 = input("Point two name: ")
    lat_2 = radians(float(input("Point two latitude: ")))
    long_2 = radians(float(input("Point two longitude: ")))
    return name1, lat_1, long_1, name2, lat_2, long_2

def calc(lat_1, long_1, lat_2, long_2, speed):
    distance = 6371.01 * acos(sin(lat_1) * sin(lat_2) + cos(lat_1) * cos(lat_2) * cos(long_1-long_2))
    duration = distance / speed
    return distance, duration

def print_results(name1, name2, distance, duration, speed):
    print("The distance between", name1, "and", name2, "is", round(distance, 2), "kilometers.")
    print("A plane flying at", speed, "km/h would cover this distance in", round(duration, 2), "hours.")

speed = 740

name1, lat_1, long_1, name2, lat_2, long_2 = input_points()
distance, duration = calc(lat_1, long_1, lat_2, long_2, speed)
print_results(name1, name2, distance, duration, speed)
