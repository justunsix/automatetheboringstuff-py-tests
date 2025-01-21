import polars as pl
import datetime as dt

# Example data
df = pl.DataFrame(
    {
        "name": ["Alice Archer", "Ben Brown", "Chloe Cooper", "Daniel Donovan"],
        "birthdate": [
            dt.date(1997, 1, 10),
            dt.date(1985, 2, 15),
            dt.date(1983, 3, 22),
            dt.date(1981, 4, 30),
        ],
        "weight": [57.9, 72.5, 53.6, 83.1],  # (kg)
        "height": [1.56, 1.77, 1.65, 1.75],  # (m)
    }
)

print(df)

# Write to csv
df.write_csv("output.csv")

# Read a csv
df_csv = pl.read_csv("output.csv", try_parse_dates=True)
print(df_csv)

# Select certain columns
# Rename a column
# Calculate Body Mass Index using other columns
result = df.select(
    pl.col("name"),
    pl.col("birthdate").dt.year().alias("birth_year"),
    (pl.col("weight") / (pl.col("height") ** 2)).alias("bmi"),
)
print(result)

# Use "expression expansion" to change multiple columns
# Add a suffix to the name of the multiple columns
result = df.select(
    pl.col("name"),
    (pl.col("weight", "height") * 0.95).round(2).name.suffix("-5%"),
)
print(result)
