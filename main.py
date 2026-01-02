import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(
        level=logging.INFO,
        filename='app.log',
        format="%(asctime)s >>>> %(filename)s:%(lineno)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d : %H:%M:%S",
)

