import os
import json
import requests
import boto3
from datetime import datetime
from typing import Dict, Any

# Configuration from environment variables
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
STOCK_SYMBOL = os.getenv("STOCK_SYMBOL", "AAPL")

def fetch_stock_data(symbol: str) -> Dict[str, Any]:
    """Fetch daily stock data from Alpha Vantage."""
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    if "Error Message" in data:
        raise ValueError(f"API Error: {data['Error Message']}")
    
    return data

def upload_to_s3(data: Dict[str, Any], bucket: str, symbol: str):
    """Upload JSON data to S3 bucket."""
    s3 = boto3.client("s3")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"raw/market_data/{symbol}_{timestamp}.json"
    
    s3.put_object(
        Bucket=bucket,
        Key=file_name,
        Body=json.dumps(data),
        ContentType="application/json"
    )
    print(f"Successfully uploaded {file_name} to bucket {bucket}")

def main():
    if not ALPHA_VANTAGE_API_KEY or not S3_BUCKET_NAME:
        print("Error: ALPHA_VANTAGE_API_KEY and S3_BUCKET_NAME environment variables must be set.")
        return

    try:
        print(f"Fetching data for {STOCK_SYMBOL}...")
        stock_data = fetch_stock_data(STOCK_SYMBOL)
        
        print(f"Uploading data to S3...")
        upload_to_s3(stock_data, S3_BUCKET_NAME, STOCK_SYMBOL)
        
    except Exception as e:
        print(f"Pipeline failed: {e}")

if __name__ == "__main__":
    main()
