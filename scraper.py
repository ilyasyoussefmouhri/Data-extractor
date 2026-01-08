import requests
from bs4 import BeautifulSoup
import logging
from config import HEADERS
from config import selectors
from config import DELAY
import time
logger = logging.getLogger(__name__)


session = requests.Session()

def fetch_page(url):
    try:
        time.sleep(DELAY)
        response = session.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        logger.info("Page fetched successfully")
        return response.text
    except Exception as e:
        logger.error(f"Failed to fetch: {e}")
        return None

def extract_data(html):
    soup = BeautifulSoup(html, 'lxml')
    data = []

    containers = soup.select(selectors['container'])
    logger.info(f"Found {len(containers)} properties")

    for container in containers:
        try:
            # Extract with fallback for missing elements
            address = container.select_one(selectors['address'])
            price = container.select_one(selectors['price'])
            bedrooms = container.select_one(selectors['bedrooms'])
            bathrooms = container.select_one(selectors['bathrooms'])
            area = container.select_one(selectors['sq'])
            prop_type = container.select_one(selectors['type'])
            link_elem = container.select_one(selectors['link'])

            data.append({
                'Title': prop_type.text.strip() if prop_type else '',
                'Address': address.text.strip() if address else '',
                'Price': price.text.strip() if price else '',
                'Bedrooms': bedrooms.text.strip() if bedrooms else '',
                'Bathrooms': bathrooms.text.strip() if bathrooms else '',
                'Area': area.text.strip() if area else '',
                'Link': link_elem.get('href') if link_elem else ''
            })
        except Exception as e:
            logger.warning(f"Failed to extract property: {e}")
            continue

    logger.info(f"Successfully extracted {len(data)} properties")
    return data