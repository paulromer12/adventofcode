# Open the file and read its content
file_path = 'dec1.txt'  # Update with the correct file path
with open(file_path, 'r') as calibration_document:
    content = calibration_document.readlines()

def calculate_calibration_sum(content):
    total_sum = 0

    for line in content:
        # Find the first and last digits
        first_digit = next(char for char in line if char.isdigit())
        last_digit = next(char for char in reversed(line) if char.isdigit())

        # Combine the first and last digits to form a two-digit number
        calibration_value = int(first_digit + last_digit)

        # Add the calibration value to the total sum
        total_sum += calibration_value

    return total_sum

# Calculate the sum of all calibration values
result = calculate_calibration_sum(content)

print(f"The sum of all calibration values is: {result}")
