from math import radians, sin, cos, atan2, sqrt

lat1 = float(input("Insert latitude of city 1: "))
lon1 = float(input("Insert longitude of city 1: "))
lat2 = float(input("Insert latitude of city 2: "))
lon2 = float(input("Insert longitude of city 2: "))

phi1 = radians(lat1)
phi2 = radians(lat2)
delta_phi = radians(lat2 - lat1)
delta_lambda = radians(lon2 - lon1)

a = sin(delta_phi / 2)**2 + cos(phi1) * cos(phi2) * sin(delta_lambda / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

r = 6371.0
d = r * c

print(f"The distance is {d:.2f} km") #advance way to print exactly 2 number after the dot 
