'''
Task: Try to read from a file non_existent.txt and handle the FileNotFoundError. Also, try to write to a file read_only.txt and handle the PermissionError.
'''

# method to open the file in read mode
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of {filename}:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# method to open the file in write mode 
def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print(f"Successfully wrote to {filename}.")
    except PermissionError:
        print(f"Error: You do not have permission to write to '{filename}'.")

if __name__ == "__main__":
    # Attempt to read from a non-existent file
    read_file('non_existent.txt')
    
    # Attempt to write to a read-only file
    write_file('read_only.txt', 'This is a test content.')