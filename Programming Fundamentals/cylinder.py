import math
pi=math.pi
print("Volume of Cylinder calculator! \n")
while True:
    try:
        r=float(input("insert the radius:"))
        h=float(input("insert the height: "))
        break
    except ValueError:
        print("Wrong input inserted: ")

Cylinder=(2*pi*r*h)+(2*pi*r*r) #lazy way on using square power
print("The cylider with radius {} and height {} has surface: {}".format(r,h,Cylinder))
    
