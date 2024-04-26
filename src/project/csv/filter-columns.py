# Filter a csv file based on specified column values
# - Set the filters in the column_values variables, filters could be rangers, values
# - Print out filtered data that match those column values
import pandas as pd

def filter_data(df, column_values):
    for column, values in column_values.items():
        if isinstance(values, list):
            if isinstance(values[0], int) or isinstance(values[0], float):
                df = df[df[column].between(values[0], values[1])]
            else:
                df = df[df[column].isin(values)]
        else:
            df = df[df[column] == values]
    return df

def main():
    # Load data from a CSV file into a DataFrame
    df = pd.read_csv('examples/data.csv')

    # Define the columns and their possible values
    column_values = {
        # 'column1': ['value1', 'value2', 'value3'],
        'Rank': [1, 3],  # This is a range
        'Search Engine': 'google'
    }

    # Filter the data
    filtered_df = filter_data(df, column_values)

    # Print the filtered data
    print(filtered_df)

if __name__ == '__main__':
    main()
