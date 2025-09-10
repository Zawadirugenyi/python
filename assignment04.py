# File Read & Write Challenge with Error Handling

def modify_content(content):
    """
    Modify the file content.
    For example: convert all text to uppercase.
    You can customize this function as needed.
    """
    return content.upper()

# Ask the user for the filename
filename = input("Enter the name of the file to read: ")

try:
    # Open the file for reading
    with open(filename, "r") as file:
        content = file.read()

    # Modify the content
    modified_content = modify_content(content)

    # Create a new filename for the modified file
    new_filename = f"modified_{filename}"

    # Write the modified content to the new file
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)

    print(f"Modified content has been written to '{new_filename}'.")

# Handle file not found error
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")

# Handle permission errors
except PermissionError:
    print(f"Error: Permission denied to read '{filename}' or write the new file.")

# Handle other I/O errors
except IOError as e:
    print(f"An I/O error occurred: {e}")
