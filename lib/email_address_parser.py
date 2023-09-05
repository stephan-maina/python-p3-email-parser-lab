# your code goes here!
import re

class EmailAddressParser:
    def __init__(self, addresses_string):
        self.addresses_string = addresses_string

    def parse(self):
        # Updated regular expression pattern for email addresses
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b'

        extracted_addresses = re.findall(email_pattern, self.addresses_string, re.IGNORECASE)

        unique_addresses = sorted(set(extracted_addresses))
        return unique_addresses
