from math import pi,cos
while True:
    angle=float(input("insert the angle in grad: "))
    if 0<= angle <= 360:
        anglerad= angle * (pi/180)
        cosine=cos(anglerad)
        print("The cosine of {} is {}".format(angle,cosine))
        break
    else:
        print("wrong angle retry!\n")
    