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

print(f"base data: {df}")

# Write to csv
df.write_csv("output.csv")

# Read a csv
df_csv = pl.read_csv("output.csv", try_parse_dates=True)
# print(df_csv)

# Select certain columns
# Rename a column
# Calculate Body Mass Index using other columns
result = df.select(
    pl.col("name"),
    pl.col("birthdate").dt.year().alias("birth_year"),
    (pl.col("weight") / (pl.col("height") ** 2)).alias("bmi"),
)
# print(result)

# Use "expression expansion" to change multiple columns
# Add a suffix to the name of the multiple columns
result_select = df.select(
    pl.col("name"),
    (pl.col("weight", "height") * 0.95).round(2).name.suffix("-5%"),
)
print(f"select, expression expansion: {result_select}")

# Use with_columns to add data to existing DataFrame
# Named expressions set the column name instead of alias
result_with_columns = df.with_columns(
    birth_year=pl.col("birthdate").dt.year(),
    bmi=pl.col("weight") / (pl.col("height") ** 2),
)
print(f"with_colums: {result_with_columns}")

# Filter creates a second dataframe with matching
# the filter
result = df.filter(pl.col("birthdate").dt.year() < 1985)

# Filter dates with multiple predicate expressions
result_filter = df.filter(
    pl.col("birthdate").is_between(dt.date(1982, 12, 31), dt.date(1996, 1, 1)),
    pl.col("height") > 1.7,
)
print(f"filter: {result_filter}")

# Group values in rows with group_by that share same value
# across expressions
# maintain_order orders resulting groups in same order as original dataframe
result_group_by = df.group_by(
    (pl.col("birthdate").dt.year() // 10 * 10).alias("decade"),
    maintain_order=True,
).len()

print(f"group_by: {result_group_by}")

# Complex query with agg, select, exclude,
# with_columns
result_complex = (
    df.with_columns(
        (pl.col("birthdate").dt.year() // 10 * 10).alias("decade"),
        pl.col("name").str.split(by=" ").list.first(),
    )
    .select(
        pl.all().exclude("birthdate"),
    )
    .group_by(
        pl.col("decade"),
        maintain_order=True,
    )
    .agg(
        pl.col("name"),
        pl.col("weight", "height").mean().round(2).name.prefix("avg_"),
    )
)
print(f"complex: {result_complex}")

# Joining dataframes with join on a common column
df2 = pl.DataFrame(
    {
        "name": ["Ben Brown", "Daniel Donovan", "Alice Archer", "Chloe Cooper"],
        "parent": [True, False, False, False],
        "siblings": [1, 2, 3, 4],
    }
)

print(f"Join: {df.join(df2, on='name', how='left')}")

# Concatinating data with vertical dimension
df3 = pl.DataFrame(
    {
        "name": ["Ethan Edwards", "Fiona Foster", "Grace Gibson", "Henry Harris"],
        "birthdate": [
            dt.date(1977, 5, 10),
            dt.date(1975, 6, 23),
            dt.date(1973, 7, 22),
            dt.date(1971, 8, 3),
        ],
        "weight": [67.9, 72.5, 57.6, 93.1],  # (kg)
        "height": [1.76, 1.6, 1.66, 1.8],  # (m)
    }
)

print(f"concat: {pl.concat([df, df3], how='vertical')}")
