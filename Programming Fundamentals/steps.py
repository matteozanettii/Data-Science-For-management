a=10
b=7
c=3
d=5
e=2
f=12
g=14
h=20
#only one step
secret=(((a+b)**3-1)**2-(c**4+d))/((e-f)**5*((g/h)**0.3))
print("only one way step {}".format(secret))
step1=a+b
step2=step1**3
step3=step2-1
step4=step3**2
step5=c**4+d
step6=step4-step5
step7=e-f
step8=step7**5
step9=g/h
step10=step9**0.3
step11=step8*step10
final=step6/step11
print("using the steps: {}".format(final))

