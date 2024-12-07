import re

# Initialize the list to store multiplication results
multiplation = []

# Initialize the count variable
count = True

# Open and read the input file
with open('input.txt', 'r') as file:
    data = file.read()

# Find all occurrences of mul(x, y), do(), and don't() using regular expression
pattern = r'(do\(\))|(don\'t\(\))|(mul\((\d+),\s*(\d+)\))'
matches = re.findall(pattern, data)

# Iterate over the matches and perform the multiplication
for match in matches:
    if match[0] == 'do()':
        count = True
    elif match[1] == "don't()":
        count = False
    elif match[2]:  # This is a mul(x,y) match
        x = int(match[3])
        y = int(match[4])
        if count:
            result = x * y
            multiplation.append(result)

# Print the results
print("Multiplication results:", multiplation)

# Sum the multiplied parts
total_sum = sum(multiplation)

# Print the total sum
print("Total sum of multiplied parts:", total_sum)