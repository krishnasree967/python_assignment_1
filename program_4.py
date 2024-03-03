# Check if the first and last number of a list is the same.

def check_first_and_last(number):

    if number[0] == number[-1]:
        return True
    else:
        return False
    
list1 = [1,2,3,4,5,1]
list2 = [1,2,3,4,5,7]

result1 = check_first_and_last(list1)
result2 = check_first_and_last(list2)

print(f" {list1}. output is : {result1}")
print(f" {list2}. optput is: {result2}")