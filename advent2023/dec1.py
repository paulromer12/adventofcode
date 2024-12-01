import re


# Open the file and read its content
file_path = 'dec1.txt'  # Update with the correct file path
with open(file_path, 'r') as calibration_document:
    content = calibration_document.readlines()

# Mapping of typed out numbers to digits
number_mapping = {
    'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}


def calculate_calibration_sum(content):
    total_sum = 0

    for line in content:
        for word, digit in number_mapping.items():
            line = line.replace(word, digit)

        digits = re.findall('\d', line)

        if digits:
            first_number = digits[0]
            last_number = digits[-1]

            # Concatenate the first and last numbers
            concatenated_number = int(first_number + last_number)

            # Add the concatenated number to the total sum
            total_sum += concatenated_number

    return total_sum

# Calculate the sum of all calibration values
result = calculate_calibration_sum(content)
print(result)