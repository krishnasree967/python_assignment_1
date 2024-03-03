# Print characters from a string that are present at an even index number.

string = input("Enter a string: ")

print("Characters at even index:", end=" ")
for i in range(0, len(string), 2):
    print(string[i], end=" ")