import pandas as pd
import sys

# Get the CSV file and columns from the command line arguments
csv_file = sys.argv[1]
columns = sys.argv[2:]

# Read the CSV file
df = pd.read_csv(csv_file)
# remove rows with empty values in the specified columns
df = df.dropna(subset=columns)

# Find duplicate rows based on the specified columns
duplicates = df[df.duplicated(subset=columns, keep=False)]

# Sort the duplicates by the specified columns
sorted_duplicates = duplicates.sort_values(by=columns)

# Print the sorted duplicates
print(sorted_duplicates)