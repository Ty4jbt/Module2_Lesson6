# Objective: The aim of this assignment is to process and format user input data.
# Task 1
def validate_name_length(first_name, last_name):
    # Initialize an empty list to store errors
    errors = []

    # Check if the first name is less than 2 characters long
    if len(first_name) < 2:
        errors.append("First name must be at least 2 characters long.")
    
    # Check if the last name is less than 2 characters long
    if len(last_name) < 2:
        errors.append("Last name must be at least 2 characters long.")

    # Return the list of errors
    return errors if errors else ["Name is valid."]

# Prompt the user to enter their first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Call the validate_name_length function and print the results
results = validate_name_length(first_name, last_name)
for result in results:
    print(result)