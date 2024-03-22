# Function to validate data during data entry

import re

# Regular expression pattern for validating email addresses
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# Function to validate email address
def validate_email(email):
    if re.match(email_pattern, email):
        return True
    else:
        return False

# Regular expression pattern for validating phone numbers

phone_pattern = r'^\+?1?\d{9,15}$'

def validate_phone(phone_number):
    if re.match(phone_pattern, phone_number):
        return True
    else:
        return False