'''
Task: Read a text file input.txt, capitalize every word, and write the modified text to output.txt.
'''
import os

# Method to capitalize words that are read from file
def capitalize_words(input_file, output_file):
    try:
        # Check if the input file exists
        if not os.path.exists(input_file):
            print(f"The file {input_file} does not exist.")
            return
        # with statement ensures that the file is properly closed when the block inside the with statement is exited.
        # Open the input file in read mode
        with open(input_file, 'r') as infile:
            content = infile.read()
            print(f"Before modification, the file content in {input_file} is: {content}")
        
        # Capitalize the first letter of each word
        capitalized_content = content.title()
        
        # Open the output file in write mode and write the capitalized content
        with open(output_file, 'w') as outfile:
            outfile.write(capitalized_content)

        # Open the output file in read mode to check content is capitalized or not
        with open(output_file, 'r') as ropfile:
            modified_content = ropfile.read()
            print(f"After modification, the file content in {output_file} is: {modified_content}")
        
        print(f"Successfully written to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Define input and output file names
    input_file = 'input.txt'
    output_file = 'output.txt'
    
    # Call the function to capitalize words in the file
    capitalize_words(input_file, output_file)

