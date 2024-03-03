# Remove first n characters from a string.

def remove_chars(string, n):
    if n < len(string):
        return string[n:]
    else:
        return "error"


result1 = remove_chars("pynative", 4)
print(result1)  

result2 = remove_chars("pynative", 2)
print(result2)  