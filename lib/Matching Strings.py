import re

# Define a regular expression pattern
pattern = r'\d+'  # This pattern matches one or more digits

# Function to search for matching strings
def find_matching_strings(input_text):
    return re.findall(pattern, input_text)

# Test the search function
input_text = "There are 42 apples and 123 oranges in the basket."
matching_strings = find_matching_strings(input_text)
print("Matching strings:", matching_strings)
