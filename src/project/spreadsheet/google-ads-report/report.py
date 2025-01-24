import polars as pl

CAMPAIGN_DATA = "campaigns.csv"
AD_DATA = "ads.csv"
LOCATION_DATA = "locations.csv"

# Polars output configuration
## Set polars table output as markdown
pl.Config.set_tbl_formatting("ASCII_MARKDOWN")
pl.Config.set_tbl_cell_numeric_alignment("RIGHT")
pl.Config.set_tbl_cols(20)
## Allow up 50 rows of output, strings up to 100 chars
pl.Config(tbl_rows=50, set_fmt_str_lengths=100)
## Hide column data types
pl.Config.set_tbl_hide_column_data_types(True)


def clean_and_convert(s):
    """For string s that is a number, remove the comma in the string"""
    return int(s.replace(",", ""))


def get_dates_from_data():
    """Read to/from dates in campaign report.
    Assume other reports use the same dates"""
    output(
        pl.read_csv(CAMPAIGN_DATA, n_rows=1, truncate_ragged_lines=True).select(
            pl.col("Campaign report").alias("Reporting period")
        )
    )


def campaign_report():
    """Read data and create summary of campaign results"""

    # Example of SQL option
    # campaigns = pl.read_csv(CAMPAIGN_DATA, skip_lines=2)
    #
    # with pl.SQLContext(register_globals=True, eager=True) as ctx:
    #     query = """
    #     SELECT
    #         "Campaign status",
    #         Campaign,
    #         Clicks,
    #         Cost,
    #         "Impr.",
    #         Interactions,
    #         Conversions,
    #         "Phone calls"
    #     FROM
    #        campaigns
    #     WHERE
    #         "Campaign status"='Total: Campaigns'
    #
    #     """
    #     return ctx.execute(query)

    campaigns = pl.read_csv(CAMPAIGN_DATA, skip_lines=2)

    return campaigns.select(
        pl.col("Campaign status"),
        pl.col("Campaign"),
        pl.col("Clicks")
        .cast(pl.Utf8)
        .map_elements(clean_and_convert, return_dtype=pl.Int16),
        pl.col("Cost").alias("Cost ($)"),
        pl.col("Impr.").alias("Impressions"),
        pl.col("Interactions"),
        pl.col("Interaction rate"),
        pl.col("Conversions"),
        pl.col("Phone calls"),
    ).filter((pl.col("Campaign status").eq("Total: Campaigns")))


def ads_report():
    """Read data and create summary of ads results"""

    ads = pl.read_csv(
        AD_DATA,
        skip_lines=2,
        ignore_errors=True,
    )

    return (
        ads.select(
            pl.col("Headline 1"),
            pl.col("Headline 2"),
            pl.col("Headline 3"),
            pl.col("Clicks")
            .cast(pl.Utf8)
            .map_elements(clean_and_convert, return_dtype=pl.Int16),
            pl.col("Final URL"),
        )
        .filter(pl.col("Clicks").is_not_null(), pl.col("Final URL").is_not_null())
        .sort("Clicks", descending=True)
        .limit(10)
    )


def locations_report():
    """Read data and create summary of locations results"""

    locations = pl.read_csv(LOCATION_DATA, skip_lines=2, ignore_errors=True)

    return (
        locations.select(
            pl.col("Location"),
            pl.col("Campaign"),
            pl.col("Clicks").map_elements(clean_and_convert, return_dtype=pl.Int16),
            pl.col("Conversions"),
        )
        .sort(pl.col("Clicks"), descending=True)
        .filter(pl.col("Location").is_not_null())
        .limit(10)
    )


def output(result):
    """Format analyzed data for reporting"""
    print(result)


def main():
    """Read and analyze data and output for report"""
    get_dates_from_data()
    output(campaign_report())
    output(ads_report())
    output(locations_report())


if __name__ == "__main__":
    main()
