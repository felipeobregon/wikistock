from sec_api import XbrlApi


KEY = None

with open('backend/sec_api_key') as f:
    KEY = f.read()

xbrlApi = XbrlApi(KEY)

xbrl_json = xbrlApi.xbrl_to_json(
    htm_url="https://www.sec.gov/ix?doc=/Archives/edgar/data/320193/000032019322000108/aapl-20220924.htm"
)

# access income statement, balance sheet and cash flow statement
print(xbrl_json["StatementsOfIncome"]['GrossProfit'])

# https://www.sec.gov/ix?doc=/Archives/edgar/data/320193/000032019322000108/aapl-20220924.htm