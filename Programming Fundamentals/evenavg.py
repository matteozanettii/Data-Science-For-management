mylist=[]
for i in range(11):
    mylist.append(i)
evenlist=[]
for i in mylist:
    if mylist[i]%2==0:
        evenlist.append(i)
avg=sum(evenlist)/len(evenlist)
print("Even numbers are: {}\n the average of even numbers are: {}".format(evenlist,avg))
