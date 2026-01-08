# Data Extractor

A flexible web scraper that extracts data from websites and exports to CSV.

## Features

- Configurable selectors for different websites
- Logging system for debugging
- CSV export with pandas
- Error handling and data cleaning

## Project Structure
```
Data-extractor/
├── main.py           # Main entry point
├── scraper.py        # Fetching and extraction logic
├── tocsv.py          # CSV export
├── config.py         # Site configuration
├── requirements.txt
└── data/            # Output CSV files
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/Data-extractor.git
cd Data-extractor
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Configure your target site in `config.py`:
```python
URL = "https://example.com"
SELECTORS = {
    'container': 'div.item',
    'title': 'h2.title',
    # ... add your selectors
}
```

2. Run the scraper:
```bash
python main.py
```

3. Find your data in `data/` folder

## Configuration

Edit `config.py` to scrape different websites:

- `URL`: Target website
- `SELECTORS`: CSS selectors for data extraction
- `OUTPUT_FILE`: Where to save CSV
- `DELAY`: Seconds between requests
- `HEADERS`: Request headers

## Requirements

- Python 3.7+
- requests
- beautifulsoup4
- pandas
- lxml

## Notes

- Always check `robots.txt` before scraping
- Respect rate limits
- Add delays between requests
- Only scrape public data

## License

MIT License - see LICENSE file for details