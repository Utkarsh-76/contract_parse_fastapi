from datetime import datetime
from parsing_code.scrapping import extract_links

from datetime import timedelta
from collections import Counter


today_date = datetime.now().date()
today_date_str = str(today_date).replace('-', '_')


def get_sample_counts(codes, sol_type):
    """
    Download solicitation and extract information from it and send it via mail
    @param codes: search codes
    @param sol_type: S type
    """

    days_to_scrap = 7
    start_date = today_date - timedelta(days=days_to_scrap)

    contracts = extract_links(codes, sol_type)
    values = [contract[4] for contract in contracts
              if datetime.strptime(contracts[1], '%m-%d-%Y').date() >= start_date]
    value_counts = dict(Counter(values))

    return value_counts
