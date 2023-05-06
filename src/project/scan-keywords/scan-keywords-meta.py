# Script to scan a list of keywords in a file and:
# - Parse the file line by line and check the presence a metadata on the line
# - If the line has the metadata, extract the keyword and print it
#   - Metadata:
#     - If line has # - Then it is a comment and print the comment
#     - If line has 1 or 2 in it but not 1 or 2 is not 
#       immediately followed by a number, 
#       extract the text keywords in the line and print it
# - Otherwise skip the line

# Import libraries
import os
import re
import sys

# Set first argument of script as the path to keywords file
keywords_file_path = os.path.join(os.getcwd(), sys.argv[1])

# Parse the file line by line and check the presence a metadata on the line
def parse_file(file_name):
    # Open the file
    with open(file_name, 'r') as file:
        # Read the file line by line
        for line in file:
            # If line has # - Then it is a comment and print the comment
            if re.search(r'^#', line):
                print(f'\n{line}\n')
            # If line has 1 or 2 but exclude lines
            # where 1 or 2 is followed by a number such as 12, 22, 300, etc.
            elif re.search(r'(?<!\d)[1-2](?!\d)', line):
                # Extract the text keywords in the line and print them as a string with spaces between words
                print(' '.join(re.findall(r'[a-zA-Z]+', line)))
            # Otherwise skip the line
            else:
                pass

parse_file(keywords_file_path)