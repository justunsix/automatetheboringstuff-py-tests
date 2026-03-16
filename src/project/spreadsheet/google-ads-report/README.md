# Google Ads Report

Using reports created in the Google ads web interface, create high level
reports.

## Usage

### Prepare data files

In Google ads, select the default (canned / premade) reports for the 
following and download them:

- `Ad group report.csv` - Ad groups (Campaigns > Ad groups)
- `Ad report.csv` - Ads (Campaigns > Ads > Main Screen)
- `Asset groups report.csv` - Asset groups (Campaigns > Asset groups)
- `Campaign report.csv` - Campaigns (Campaigns > Main Screen)
- `Location report.csv` - Locations (Audiences, keywords, and content > Locations)
- `Searches-Word.csv` - Word Searches (Overview > Top searches and words 
  within searches where people saw your ads)
  
Refer to [report.py](./report.py) for columns selected for these reports. In
summary, they are:

- Campaigns: status, campaign name, Clicks, Cost, Impressions, Interaction
  Rate, Conversion, Phone calls
- Ads: First 3 headlines, Clicks, Final URL
- Locations: Location, Campaign, Clicks, Conversions
- Ad groups: ad group, campaign, clicks, cost, impressions, interaction rate, 
  conversions, phone calls
- Asset groups: Asset group, Clicks, Impressions, interaction rate, Conversions
- Word Searches: standardized by the report card

### Prepare report configuration

- Edit the `report.py` and Google ads reports if you would like different
  columns
- Make sure files are using UTF-8 encoding

### Run report

Create virtual environment using `requirements.in` and run `report.py`

``` shell

# Using Virtual environment and pip
python -m venv ./venv
./venv/Scripts/Activate
pip install -r .\requirements.in
python report.py

# or using uv to setup environment and install requirements
uv run report.py
```

## See Also

- Combine the output for this report into this 
  [Google Ads Digital Marketing Template](https://justunsix.github.io/garden/notes/650-business-comms-marketing-template-digital-report/)
