import sys

import pandas as pd

from typing import List

# Get the CSV file and columns from the command line arguments
csv_file = sys.argv[1]
columns = sys.argv[2:]


def check_csv_encoding(csv_file: str) -> None:
    """
    Checks the encoding of a CSV file by attempting to decode each line with UTF-8.

    Parameters:
    -----------
    csv_file : str
        The path to the CSV file to check for encoding issues.

    Returns:
    --------
    None
        This function prints error messages directly if there are encoding issues but does not return any value.

    """

    # Open the file in binary mode to detect the encoding at specific positions
    with open(csv_file, "rb") as f:
        for line_num, line in enumerate(f, start=1):
            try:
                # Try decoding each line (assuming UTF-8 initially)
                line.decode("utf-8")
            except UnicodeDecodeError as e:
                print(f"Error at line {line_num}: {e}")
                print(
                    f"Problematic line in raw bytes: {line[:100]}"
                )  # Print first 100 bytes of the line for inspection
                break


def find_duplicates_sort_data(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Find duplicate rows based on the specified columns

    Parameters:
    -----------
    df : pd.DataFrame
        The DataFrame in which duplicates need to be identified.
    columns : List[str]
        The list of column names to consider when identifying duplicates.

    Returns:
    --------
    pd.DataFrame
        A DataFrame containing the sorted duplicate rows based on the specified columns.
    """
    # Find duplicate rows based on the specified columns
    duplicates: pd.DataFrame = df.loc[df.duplicated(subset=columns, keep=False)]

    # Sort the duplicates by the specified columns
    sorted_duplicates: pd.DataFrame = duplicates.sort_values(by=columns)

    return sorted_duplicates


check_csv_encoding(csv_file)

# Read the CSV file
df = pd.read_csv(csv_file)
# If further encoding issues, suggest alternative encodings, for example:
# df = pd.read_csv(csv_file, encoding="ISO-8859-1")

# remove rows with empty values in the specified columns
df = df.dropna(subset=columns)

sorted_duplicates: pd.DataFrame = find_duplicates_sort_data(df, columns)

print(sorted_duplicates)

print("Creating CSV for inspection")
sorted_duplicates.to_csv("sortedduplicates.csv", index=False)
