# User Input Data Processor
# Objective: The aim of this assignment is to process and format user input data.

# Task 1: Input Length Validator Write a script that asks for and checks the length 
# of the user's first name and last name. Both should be at least 2 characters long. 
# If not, print an error message.

def validate_name_length(first_name, last_name):
    if len(first_name) < 2 or len(last_name) < 2:
        return "Error: Both first name and last name must be at least 2 characters long."
    else:
        return "Name length is valid."

# Ask for user input
user_first_name = input("Please enter your first name: ")
user_last_name = input("Please enter your last name: ")

# Validate the length of the names
validation_result = validate_name_length(user_first_name, user_last_name)

# Print the result
print(validation_result)
