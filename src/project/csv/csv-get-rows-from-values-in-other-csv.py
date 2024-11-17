"""
This script extracts values from a specified column in one CSV file called `csv_with_values_to_be_searched`
that match a certain filter value, and then searches for rows in another CSV file called
`csv_to_be_filtered` that contain any of these extracted values.
The matching rows are written to a new CSV file called `csv_results_file`.

Usage:
    Modify the `csv_with_values_to_be_searched`, `csv_to_be_filtered`, and `csv_results_file` variables
    to point to the appropriate CSV files before running the script.

Constants:
    COLUMN_NAME_FILTER (str): The name of the column to filter values from.
    COLUMN_VALUE_FILTER (str): The value to filter by in the specified column.
"""

import csv

csv_with_values_to_be_searched = "examples/users-db.csv"
csv_to_be_filtered = "examples/users.csv"
csv_results_file = "examples/example_results_output.csv"

values_from_csv = []

COLUMN_NAME_FILTER = "email"
COLUMN_VALUE_FILTER = "email.com"


def get_values_from_csv(csvfile, values_from_csv):
    """
    Extracts values from a specified column in a CSV file that match a certain filter value.

    Args:
        csvfile (str): The path to the CSV file to be read.
        values_from_csv (list): The list to store the extracted values.
    """
    with open(csvfile, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if COLUMN_VALUE_FILTER in row[COLUMN_NAME_FILTER]:
                values_from_csv.append(row[COLUMN_NAME_FILTER])


get_values_from_csv(csv_with_values_to_be_searched, values_from_csv)


def search_csv_file(csv_file, search_values, output_file):
    """
    Searches for rows in a CSV file that contain any of the specified values and writes them to a new CSV file.

    Args:
        csv_file (str): The path to the CSV file to be searched.
        search_values (list): The list of values to search for in the CSV file.
        output_file (str): The path to the output CSV file where the results will be written.
    """
    results = []
    with open(csv_file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for value in search_values:
                if value in row.values():
                    results.append(row)
                    break

    with open(output_file, "w", newline="") as csvfile:
        fieldnames = results[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    return


search_csv_file(csv_to_be_filtered, values_from_csv, csv_results_file)
