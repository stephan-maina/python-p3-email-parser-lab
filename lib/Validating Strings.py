import re

# Define a regular expression pattern
pattern = r'^[A-Za-z0-9]+$'  # This pattern matches alphanumeric strings

# Function to validate a string
def validate_string(input_string):
    if re.match(pattern, input_string):
        return True
    else:
        return False

# Test the validation function
input_string = "Hello123"
if validate_string(input_string):
    print(f"'{input_string}' is a valid string.")
else:
    print(f"'{input_string}' is not valid.")
