from sec_api import XbrlApi
from sec_api import QueryApi


KEY = None

with open('backend/sec_api_key') as f:
    KEY = f.read()

xbrlApi = XbrlApi(KEY)

queryApi = QueryApi(KEY)

query = {
  "query": { "query_string": {
      "query": "ticker:TSLA AND formType:\"10-Q\""
    } },
  "from": "0",
  "size": "10",
  "sort": [{ "filedAt": { "order": "desc" } }]
}

filings = queryApi.get_filings(query)

filings = filings['filings']

accessionNo = filings[0]['accessionNo']



xbrl_json = xbrlApi.xbrl_to_json(
    accession_no=accessionNo
)

# access income statement, balance sheet and cash flow statement
print(xbrl_json["StatementsOfIncome"]['GrossProfit'][0])

# https://www.sec.gov/ix?doc=/Archives/edgar/data/320193/000032019322000108/aapl-20220924.htm
