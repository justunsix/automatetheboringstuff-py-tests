# Goes through the CSV file and extracts a column's values that match a certain value
# and stores them in an array.
# Then goes through the array and for each value in the array
# get lines in a csv file that contain the value and store them in a new csv file
import csv

csv_with_values_to_be_searched = 'examples/users-db.csv'
csv_to_be_filtered = 'examples/users.csv'
csv_results_file = 'examples/example_results_output.csv'

values_from_csv = []

COLUMN_NAME_FILTER = 'email'
COLUMN_VALUE_FILTER = "email.com"


def get_values_from_csv(csvfile, emails):
    with open(csvfile, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if COLUMN_VALUE_FILTER in row[COLUMN_NAME_FILTER]:
                values_from_csv.append(row[COLUMN_NAME_FILTER])        

get_values_from_csv(csv_with_values_to_be_searched, values_from_csv);


def search_csv_file(csv_file, search_values, output_file):
    results = []
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for value in search_values:
                if value in row.values():
                    results.append(row)
                    break
    
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = results[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    return

search_csv_file(csv_to_be_filtered, values_from_csv, csv_results_file)