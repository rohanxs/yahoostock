from requests import get

def get_price(stock_name : str) -> float:

    '''Returns the current price of some stock.'''

    url = f"https://finance.yahoo.com/quote/{stock_name}?p={stock_name}&.tsrc=fin-srch"
    scraped_text = get(url).text

    _ = scraped_text.index("Fw(b) Fz(36px) Mb(-4px) D(ib)\"")
    scraped_text = scraped_text[_:_+200]

    return float(
        scraped_text[
            scraped_text.index("value=")+7:
            scraped_text.index("\" active")
        ].replace(',', '')
    )

def get_percent_change(stock_name : str) -> float:

    '''Returns the percent change in price of some stock in the past day.'''

    url = f"https://finance.yahoo.com/quote/{stock_name}?p={stock_name}"
    scraped_text = get(url).text

    scraped_text = scraped_text[scraped_text.index("Fw(500) Pstart(8px) Fz(24px)")+30:]
    _ = scraped_text.index("Fw(500) Pstart(8px) Fz(24px)")
    scraped_text = scraped_text[_+50:_+300]

    return float(
        scraped_text[
            scraped_text.index("value=")+7:
            scraped_text.index("\" active=")
        ].replace(',','')
    )

def get_change(stock_name : str) -> float:

    '''Returns the total change in price of a stock in the past day.'''

    url = f"https://finance.yahoo.com/quote/{stock_name}?p={stock_name}"
    scraped_text = get(url).text

    _ = scraped_text.index("Fw(500) Pstart(8px) Fz(24px)")
    scraped_text = scraped_text[_+50:_+200]

    return float(
        scraped_text[
            scraped_text.index("value=")+7:
            scraped_text.index("\" active")
        ].replace(',','')
    )

def get_open(stock_name : str) -> float:

    '''Returns the most recent opening price of some stock.'''

    url = f"https://finance.yahoo.com/quote/{stock_name}?p={stock_name}&.tsrc=fin-srch"
    scraped_text = get(url).text

    _ = scraped_text.index("OPEN-value")
    scraped_text = scraped_text[_:_+170]

    return float(
        scraped_text[
            scraped_text.index("\">")+2:
            scraped_text.index("</")
        ].replace(',','')
    )

def get_previous_close(stock_name : str) -> float:

    '''Returns the most recent closing price of some stock.'''

    url = f"https://finance.yahoo.com/quote/{stock_name}?p={stock_name}&.tsrc=fin-srch"

    scraped_text = get(url).text

    _ = scraped_text.index("PREV_CLOSE-value")
    scraped_text = scraped_text[_:_+170]

    return float(
        scraped_text[
            scraped_text.index("\">")+2:
            scraped_text.index("</")
        ].replace(',','')
    )

def get_all(stock_name : str) -> dict:
    
    (
        '''Returns all relevant information about a stock's statistics. '''
        '''NOTE: Although convenient, this method is still heavily unoptimized '''
        '''and makes unnecessary requests along with redundant string searching. '''
        '''Try to avoid use unless absolutely unnecessary.'''
    )

    info = {
        'name' : stock_name,
        'price' : get_price(stock_name),
        'percent_change' : get_percent_change(stock_name),
        'change' : get_change(stock_name),
        'open' : get_open(stock_name),
        'previous_close' : get_previous_close(stock_name)
    }

    return info