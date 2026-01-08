import logging
from config import URL, SITE_NAME
from scraper import fetch_page, extract_data
from tocsv import save_csv


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s >>>> %(filename)s | %(levelname)s : %(message)s',
        handlers=[
            logging.FileHandler('app.log'),
            logging.StreamHandler()
        ]
    )

    logger = logging.getLogger(__name__)

    logger.info(f"Starting scrape: {SITE_NAME}")
    logger.info(f"Target URL: {URL}")

    html = fetch_page(URL)
    if not html:
        return

    data = extract_data(html)
    if not data:
        return

    df = save_csv(data)
    if df is not None:
        logger.info("Scraping completed successfully!")
        print("\nPreview:")
        print(df.head())


if __name__ == "__main__":
    main()