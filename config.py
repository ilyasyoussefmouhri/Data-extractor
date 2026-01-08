import logging

logger = logging.getLogger(__name__)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
}

selectors = {
    'container' : 'div.BasePropertyCard_propertyCardWrap__gtWK6',
    'address' : 'div[data-testid="card-address"]',
    'price' : 'div[data-testid="card-price"]',
    'Bedrooms' : 'li[data-testid="property-meta-beds"]',
    'Bathrooms' : 'li[data-testid="property-meta-baths"]',
    'sq' : 'li[data-testid="property-meta-sqft"]',
    'type' : 'div.message',
    'link' : 'a.LinkComponent_anchor__JMkHs'
}

DELAY = 10

SITE_NAME = 'realtor.com'
URL = 'https://www.realtor.com/realestateandhomes-search/New-York_NY'
OUTPUT_FILE = 'data/data.csv'