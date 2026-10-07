name = input("Enter your name: ")
age = input("Enter your age: ")
hobby = input("Enter your hobby: ")

line_title = "USER PROFILE"
line_name = f"Name: {name}"
line_age = f"Age: {age} years old"
line_hobby = f"Hobby: {hobby}"

max_len = max(
    len(line_title),
    len(line_name),
    len(line_age),
    len(line_hobby)
)

separator = "=" * max_len

print(separator)
print(line_title)
print(separator)
print(line_name)
print(line_age)
print(line_hobby)
print(separator)

#second advance method with list

#direct input in a list (assuming in this case eerything as a string)
lines = [
    "USER PROFILE",
    f"Name: {input('Enter your name: ')}",
    f"Age: {input('Enter your age: ')} years old",
    f"Hobby: {input('Enter your hobby: ')}"
]

#Find the longest line and create matching '=' separator, like the separator
#above but using map as element per element function
sep = "=" * max(map(len, lines))

#Print header and remaining lines joined by newlines, join concatenates the return
#on every line of the list
print(f"{sep}\n{lines[0]}\n{sep}\n" + "\n".join(lines[1:]) + f"\n{sep}")
