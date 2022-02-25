from requests import get

def get_eval(stock_name : str) -> float:
    (
        '''Returns a prediction on whether a certain stock will rise or fall '''
        '''based on CNN's stock forecast. A negative number indicates a predicted '''
        '''decrease in stock value and a high number indicates a predicted increase.'''
    )
    
    scraped_text = get(
        f'https://money.cnn.com/quote/forecast/forecast.html?symb={stock_name}'
    ).text
    
    _ = scraped_text.index('The median estimate represents a ')

    evaluation = round(
        float(scraped_text[
            _+28 : _+128
        ].split('">')[1].split('%')[0]
    )/100, 4)

    return evaluation

print(get_eval.__doc__)