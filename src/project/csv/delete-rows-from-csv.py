# Given a list of strings, it will go into a csv file and:
# - Find rows which contain those strings
# - Print the rows
# - Remove the rows from the csv file
#
# Usage:
# python delete-rows-from-csv.py examples/users.csv Laura.lee@email.com john.smith@email.com
import csv
import os
import argparse

def delete_rows(file_path, strings_to_delete):
    # Read the CSV file
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)

    # Iterate over the rows
    for row in rows[:]:  # Use a slice to iterate over a copy of the list
        if any(string in row for string in strings_to_delete):
            print(f"Deleting row: {row}")
            rows.remove(row)

    # Write the modified rows back to the CSV file
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Delete rows from a CSV file.')
    parser.add_argument('file_path', help='The path to the CSV file.')
    parser.add_argument('strings_to_delete', nargs='+', help='The strings to delete.')
    args = parser.parse_args()

    delete_rows(args.file_path, args.strings_to_delete)