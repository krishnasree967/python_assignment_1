# Print the sum of the current number and the previous number.

def current_previous(n):
    previous = 0
    for j in range(1, n + 1):
        current = j
        total = previous + current
        print(f"Current number: {current}, Previous number: {previous}, Total sum: {total}")
        previous = current

current_previous(10)