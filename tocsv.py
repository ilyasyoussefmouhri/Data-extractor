import os
import pandas as pd
from config import OUTPUT_FILE
import logging

logger = logging.getLogger(__name__)

def save_csv(data):
    df = pd.DataFrame(data)
    df = df.dropna(subset=['Price', 'Address'])
    df = df.fillna('')

    try:
        os.makedirs('data', exist_ok=True)  # Create folder if needed
        df.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')
        logger.info(f"Successfully saved {len(df)} records to {OUTPUT_FILE}")
    except Exception as e:
        logger.error(f"Failed to save data: {e}")
        return None

    return df