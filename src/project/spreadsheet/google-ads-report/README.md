# Google Ads Report

Using reports created in the Google ads web interface, create high level
reports.

## Usage

### Prepare data files

- In Google ads, select the default (canned / premade) reports for:
  - Campaigns
  - Locations
  - Ads
- Refer to [report.py](./report.py) for columns selected for these reports. In
  summary, they are:
  - Campaigns: status, campaign name, Clicks, Cost, Impressions, Interaction
    Rate, Conversion, Phone calls
  - Ads: First 3 headlines, Clicks, Final URL
  - Locations: Location, Campaign, Clicks, Conversions
- Edit the `report.py` and Google ads reports if you would like different
  columns
- Download Google ads reports for campaign, locations, and ads

### Report report

- Create virtual environment using `requirements.in`
- Run `report.py`
  - Example Usage with uv: `uv run report.py`

## See Also

- Combine the output for this report into this [Google Ads Digital Marketing Template](https://justunsix.github.io/garden/notes/650-business-comms-marketing-template-digital-report/)
