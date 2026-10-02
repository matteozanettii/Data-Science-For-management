x1 = True
x2 = True
y1 = True
y2 = True
k=1

if x1 == x2 and y1 == y2:
    print("True")
    k=0
if x1 != x2 and y1 != y2:
    print("True")
    k=0
if (x1 == x2) != (y1 == y2):
    print("False")
    k=0
if k==1:
    print("False")
