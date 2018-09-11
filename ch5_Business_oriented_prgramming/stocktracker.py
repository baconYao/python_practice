 #!/usr/bin/python
 # -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup           # Use the latest version of beautifulsuop
import os, csv, time

field_order = ['date', 'last_trade']
fields = {
    'date': 'Date',
    'last_trade': 'Last Trade',
    'ah_price': 'After Hours price',
}

def get_stock_html(ticker_name):
    # Create opener object
    opener = urllib2.build_opener(
        urllib2.HTTPRedirectHandler(),
        urllib2.HTTPHandler()
    )
    # Add header to request
    """
        some websites like to block automated agents like this, so to be on the safe side you’re being sneaky here and setting the user agent you send to the server so you appear to be a completely different web browser . In this case, you’re pretending to be Internet Explorer 7 running on Windows XP. You can find other user agent strings by doing a web search for “user agent strings.
    """
    opener.addheaders = [
        ('User-agent', 
         "Mozilla/4.0 (compatible; MSIE 7.0; "
         "Windows NT 5.1; .NET CLR 2.0.50727; "
         ".NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)")
    ]
    # Read web page with opener
    url = "http://finance.yahoo.com/q?s=" + ticker_name
    response = opener.open(url)
    return ''.join(response.readlines())

def find_quote_section(html):
    # Create parse obj
    soup = BeautifulSoup(html, 'html.parser')
    # Find yfi_quote_summary element
    quote = soup.find('div', attrs={'id': 'app'})
    # quote = soup.find('body')
    return quote

"""
    Target website may changes its content, you must to check it by yourself
"""
def parse_stock_html(html, ticker_name):
    quote = find_quote_section(html)
    result = {}
    tick = ticker_name.lower()

    # <h1>Google Inc.</h2>
    result['stock_name'] = quote.find('h1', attrs={'data-reactid': '7'}).string

    ### Current values
    result['last_trade'] = quote.find('span', attrs={'data-reactid': '38'}).string

    print result

    return result

def write_row(ticker_name, stock_values):
    # Look for existing CSV file
    file_name = "stocktracker-" + ticker_name + ".csv"
    if os.access(file_name, os.F_OK):
        # File exists
        file_mode = 'ab'
    else:
        # File doesn't exists
        file_mode = 'wb'

    # Create csv.DictWritter obj
    csv_writer = csv.DictWriter(
        open(file_name, file_mode),
        fieldnames = field_order,
        extrasaction = 'ignore'
    )
    # Write rows
    if file_mode == 'wb':
        csv_writer.writerow(fields)
    csv_writer.writerow(stock_values)


if __name__ == '__main__':
    # Call function
    html = get_stock_html('GOOG')
    stock = parse_stock_html(html, 'GOOG')
    stock['date'] = time.strftime("%Y-%m-%d %H:%M")
    write_row('GOOG', stock)
    print stock