letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print("The list contains: {}".format(letters))

idx1 = int(input("Insert the first index: "))
idx2 = int(input("Insert the second index: "))

letters[idx1], letters[idx2] = letters[idx2], letters[idx1]

print("The list after the exchange became: {}".format(letters))
