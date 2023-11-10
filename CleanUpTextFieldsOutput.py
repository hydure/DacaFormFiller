import re

# Define the input file name and output file name
input_file_name = 'TextFieldsAllForms.txt'
output_file_name = 'PossibleTextFieldsConsolidated.txt'

# Function to check if a string consists only of digits
def is_numeric(value):
    return value.isdigit()

# Function to process and clean the values
def clean_value(value):
    # Split the value by commas
    parts = value.split(',')
    
    # Process each part to extract the substring after the last underscore
    cleaned_parts = []
    for part in parts:
        # Split by underscore and take the last part
        last_part = part.rsplit('_', 1)[-1]
        
        # Remove brackets and their contents using regular expression
        cleaned_last_part = re.sub(r'\[.*?\]', '', last_part)
        
        # Remove single quotes
        cleaned_last_part = cleaned_last_part.replace("'", "")
        
        # Remove leading and trailing spaces
        cleaned_last_part = cleaned_last_part.strip()
        
        # Remove instances of the string "keys"
        cleaned_last_part = cleaned_last_part.replace("keys", "")
        
        # Check if the cleaned part is numeric and skip it if it is
        if not is_numeric(cleaned_last_part):
            cleaned_parts.append(cleaned_last_part)
    
    # Create a set to remove duplicates and join the cleaned parts
    cleaned_set = set(cleaned_parts)
    
    # Join the unique cleaned values back into a comma-separated string
    cleaned_value = ','.join(cleaned_set)
    
    # Remove any extra brackets or parentheses
    cleaned_value = re.sub(r'[\[\](){}]', '', cleaned_value)
    
    return cleaned_value

try:
    # Open the input file for reading
    with open(input_file_name, 'r') as input_file:
        # Read the content of the input file
        content = input_file.read()
        
        # Clean and modify the values
        cleaned_content = clean_value(content)
        
        # Write the cleaned content to the output file
        with open(output_file_name, 'w') as output_file:
            output_file.write(cleaned_content)
        
    print(f"Values have been cleaned and saved to {output_file_name}")

except FileNotFoundError:
    print(f"File '{input_file_name}' not found.")

except Exception as e:
    print(f"An error occurred: {e}")