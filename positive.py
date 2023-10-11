# Input list of numbers
list1 = [12, -7, 5, 64, -14]

# Initialize an empty list to store positive numbers
positive_numbers = []

# Iterate through the list and add positive numbers to the new list
for num in list1:
    if num > 0:
        positive_numbers.append(num)

# Print the positive numbers
print("Input:", list1)
print("Output:", positive_numbers)
