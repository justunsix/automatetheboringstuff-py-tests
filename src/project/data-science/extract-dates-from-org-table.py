 # Extract and reformat dates from a table in a text string. 
 # The table is assumed to be in the "org table" format, 
 # which is a plain text format used by the Emacs Org mode.
 # The script uses the pandas library to handle the data.
import pandas as pd
from io import StringIO
import pyperclip

data = """
| Date of Run | End of Run |
|-------------+------------|
| JAN 04      | DEC 27     |
| JAN 18      | JAN 10     |
| FEB 01      | JAN 24     |
| FEB 15      | FEB 07     |
| FEB 29      | FEB 21     |
| MAR 14      | MAR 06     |
| MAR 28      | MAR 20     |
| APR 11      | APR 03     |
| APR 25      | APR 17     |
| MAY 09      | MAY 01     |
| MAY 23      | MAY 15     |
| JUN 06      | MAY 29     |
| JUN 20      | JUN 12     |
| JUL 04      | JUN 26     |
| JUL 18      | JUL 10     |
| AUG 01      | JUL 24     |
| AUG 15      | AUG 07     |
| AUG 29      | AUG 21     |
| SEP 12      | SEP 04     |
| SEP 26      | SEP 18     |
| OCT 10      | OCT 02     |
| OCT 24      | OCT 16     |
| NOV 07      | OCT 30     |
| NOV 21      | NOV 13     |
| DEC 05      | NOV 27     |
| DEC 19      | DEC 11     |
"""

# Remove lines that start with '|--'
data = '\n'.join([line for line in data.split('\n') if not line.startswith('|--')])

# Read the data into a pandas DataFrame
df = pd.read_table(StringIO(data), sep='|')

# Remove leading/trailing whitespace from column names and values
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
df.columns = df.columns.str.strip()

# Convert the 'Date of Run' column to datetime, assuming the year is 2024
df['Date of Run'] = pd.to_datetime(df['Date of Run'] + ' 2024', format='%b %d %Y')

# Convert the 'Date of Run' column to the desired format
df['Date of Run'] = df['Date of Run'].dt.strftime('%Y-%m-%d')

# Only print the dates back without index
printed_dates = df['Date of Run'].to_string(index=False)
print(f'These dates are copied to the system clipboard:\n{printed_dates}')
# Copy the output to the clipboard
pyperclip.copy(printed_dates)