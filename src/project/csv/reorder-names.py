# Read a CSV file and reformat the names in the file
# The first column of the CSV file contains the full names of the people
# Order names so that it is last name, then first name followed by an custom identifier

# For each line in the CSV file:
# - Split the name into first and last name
# - Reverse the names, add a comma in between the names and append a custom string
# - Write changes to a new CSV file

# The script:
# - Uses the csv module to read and write the CSV files.
# - Input: names.csv file 
# - Output file new_names.csv

# Sample output:
# Doe, John (MOH)
# Smith, Jane (MOH)
# Williams, Mary (MOH)
# Brown, Bob (MOH)

import csv

# custom identifier
custom_identifier = " (MOH)"

with open('names.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    with open('new_names.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in reader:
            name = row[0]
            first_name = name.split()[0]
            last_name = name.split()[1]
            new_name = last_name + ", " + first_name + custom_identifier
            writer.writerow([new_name])