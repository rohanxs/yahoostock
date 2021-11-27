from requests import get

def get_price(stock_name : str):
    stock_name = stock_name.upper()

    try:
        url = f"https://finance.yahoo.com/quote/{stock_name}?p={stock_name}&.tsrc=fin-srch"
        scraped_text = get(url).text

        scraped_text = scraped_text[
            scraped_text.index("\"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)\""):
        ]

        price = scraped_text[scraped_text.index("47")+4:scraped_text.index("</span")]
        price = float(price.replace(',', ''))

        return price
        
    except:
        print(f"Stock {stock_name} not found.")
        return False