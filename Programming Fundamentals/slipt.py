s=input("insert a phrase: ")
second= len(s) // 2
third= len(s) // 3
print("two part splitting")
print(s[:second])
print(s[second:])
print("Three part splitting")
print(s[:third])
print(s[third:2*third])
print(s[2*third:])
