
import requests
import pandas as pd
from pathlib import Path

def fetch_api_data():

    # REST API URL
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        # Send HTTP GET request
        response = requests.get(url, timeout=15)

        # Check response
        response.raise_for_status()

        # Convert JSON into Python data
        data = response.json()

        # Convert JSON data into DataFrame
        df = pd.DataFrame(data)

        print("\nAPI DATA")
        print(df.head())

        # Save API data
        base_dir = Path(__file__).resolve().parent.parent
        report_dir = base_dir / "reports"
        report_dir.mkdir(exist_ok=True)

        df.to_csv(
            report_dir / "api_data.csv",
            index=False
        )

        print("\nAPI data fetched successfully!")

    except requests.exceptions.RequestException as error:
        print("API Error:", error)
