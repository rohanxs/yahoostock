from requests import get

def get_price(stock_name : str):
    '''Returns the current price of some stock.'''
    url = f"https://finance.yahoo.com/quote/{stock_name}?p={stock_name}&.tsrc=fin-srch"
    scraped_text = get(url).text

    _ = scraped_text.index("Fw(b) Fz(36px) Mb(-4px) D(ib)\"")
    scraped_text = scraped_text[_:_+1000]

    return float(
        scraped_text[
            scraped_text.index("47")+4:scraped_text.index("</")
        ].replace(',', '')
    )

def get_percent_change(stock_name : str):
    '''Returns the percent change in price of some stock in the past day.'''
    url = f"https://finance.yahoo.com/quote/{stock_name}?p={stock_name}"
    scraped_text = get(url).text

    scraped_text = scraped_text[scraped_text.index("Fw(500) Pstart(8px) Fz(24px)")+30:]
    _ = scraped_text.index("Fw(500) Pstart(8px) Fz(24px)")
    scraped_text = scraped_text[_+50:_+300][scraped_text.index("48")+4:]

    return float(
        scraped_text[
            scraped_text.index("(")+1:scraped_text.index("%")
        ].replace(',','')
    )

def get_change(stock_name : str):
    '''Returns the total change in price of a stock in the past day.'''
    url = f"https://finance.yahoo.com/quote/{stock_name}?p={stock_name}"
    scraped_text = get(url).text

    _ = scraped_text.index("Fw(500) Pstart(8px) Fz(24px)")
    scraped_text = scraped_text[_+50:_+200]

    return float(
        scraped_text[
            scraped_text.index("value=")+7:scraped_text.index("\" active")
        ].replace(',','')
    )

def get_open(stock_name : str):
    '''Returns the most recent opening price of some stock.'''
    url = f"https://finance.yahoo.com/quote/{stock_name}?p={stock_name}&.tsrc=fin-srch"
    scraped_text = get(url).text

    _ = scraped_text.index("OPEN-value")
    scraped_text = scraped_text[_:_+170]

    return float(
        scraped_text[
            scraped_text.index("\">")+2:scraped_text.index("</")
        ].replace(',','')
    )

def get_previous_close(stock_name : str):
    '''Returns thei most recent closing price of some stock.'''
    url = f"https://finance.yahoo.com/quote/{stock_name}?p={stock_name}&.tsrc=fin-srch"
    scraped_text = get(url).text

    _ = scraped_text.index("PREV_CLOSE-value")
    scraped_text = scraped_text[_:_+170]

    return float(
        scraped_text[
            scraped_text.index("\">")+2:scraped_text.index("</")
        ].replace(',','')
    )