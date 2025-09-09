def digits(number):
digits = 0
while number > 0:
digits = number % 10  # Get the last digit
digits += digits  # Add it to the sum
number = number // 10  # Remove the last digit
int(input("Enter a number: "))

# Calculate the sum of digits
result = digits(number)

# Print the result
print(f"The sum of the digits of {number} is {result}.")
