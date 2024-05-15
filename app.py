import random
import string

# Define the length of the password
password_length = 12

# Define the characters to include in the password
chars = string.ascii_letters + string.digits + string.punctuation

# Use a list comprehension to generate the password
password = [random.choice(chars) for _ in range(password_length)]

# Join the list into a single string
password = ''.join(password)

# Print the generated password
print(password)