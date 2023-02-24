import os
import sys

# Set first argument of script as the path to keywords file
keywords_file_path = os.path.join(os.getcwd(), sys.argv[1])

# Set first argument of script as text files to scan
scan_files_path = os.path.join(os.getcwd(), sys.argv[2])

def get_keywords():
    """Read keywords from file and return as a list."""
    with open(keywords_file_path) as f:
        return f.read().splitlines()
      
def scan_file(file_path, keywords):
    """Scan a file with a keywords list and when there is a match in the keyword, return the line number and full line."""
    
    # filename is path in a string format relative to current directory   
    # Open the file and read it line by line
    print("==============================================================")
    print("Scanning file: " + file_path)
    with open(file_path, "r") as f:
        
        lines = f.readlines()
        
        # Iterate over the lines and check if the line contains any of the keywords
        for i, line in enumerate(lines):
            for keyword in keywords:
                if keyword in line:
                    print("Keyword: ", keyword, "| Line: " + str(i+1) + " | " + line)
                    break
           
    print("==============================================================")
# keywords list                    
keywords_list = get_keywords()

# Get a list of all the files in the current directory
files = os.listdir(scan_files_path)

# Iterate over the list of files and call scan_file function with the keywords list
for file_name in files:
    scan_file(os.path.join(scan_files_path, file_name), keywords_list)
