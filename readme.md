# yahoostock
 A package designed to scrape data from Yahoo Finance.

## Installation
```
pip install yahoostock
```
## Usage
Use the following code to see a list of useful methods.
```py
from yahoostock import yahoo
print(dir(yahoo))
```
Note that each method accepts a stock ticker as a single parameter and returns a float with the specified statistic.