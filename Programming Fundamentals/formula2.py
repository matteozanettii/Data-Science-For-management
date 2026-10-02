def formula(a,b,c,d,e,f,g):
    x=((((a-b)**0.5)*d)/(c+e)+((abs(f))/g))**3
    print(x)
a,b,c,d,e,f,g=[int(x) for x in input("insert numbers here: ").split()]
formula(a,b,c,d,e,f,g)
    
