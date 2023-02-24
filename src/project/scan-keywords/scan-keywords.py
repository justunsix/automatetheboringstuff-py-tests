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
    """Scan a file with a keywords list and when there is a match in the keyword (match is case insensitive), return the line number and full line. At end of file, return keywords and number of matches in the file for keywords that had a match."""   
    
    # filename is path in a string format relative to current directory   
    # Open the file and read it line by line
    print("+==============================================================================================================")
    print("|")
    print("| Scanning file: " + file_path)
    print("|")    
    with open(file_path, "r") as f:
        file_lines = f.readlines()
        for line_number, line in enumerate(file_lines, 1):
            for keyword in keywords:
                if keyword.lower() in line.lower():
                    print("| Keyword: " + keyword + " found in line " + str(line_number) + ": " + line)
        print("| ==============================================================")
        print("| Number of matches for each keyword:")
        for keyword in keywords:
            keyword_count = 0
            for line in file_lines:
                if keyword.lower() in line.lower():
                    keyword_count += 1
            if keyword_count > 0:
                # print found with ansi green color
                print("| \033[1;32;40m", keyword, " found " + str(keyword_count) + " times.\033[0;37;40m")
            else:
                # print found with ansi red color
                print("| \033[1;31;40m", keyword, " not found.\033[0;37;40m")

    print("|")           
    print("+==============================================================")
# keywords list                    
keywords_list = get_keywords()

# Get a list of all the files in the current directory
files = os.listdir(scan_files_path)

# Iterate over the list of files and call scan_file function with the keywords list
for file_name in files:
    scan_file(os.path.join(scan_files_path, file_name), keywords_list)
