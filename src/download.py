"""
download.py

Downloads HDB resale datasets from Data.gov.sg automatically.
"""

from pathlib import Path
import requests

from src.config import CONFIG, RAW_PATH


BASE_URL = (
    "https://api-open.data.gov.sg/v1/public/api/datasets"
)


class DownloadManager:

    def __init__(self):

        self.datasets = CONFIG["datasets"]

        RAW_PATH.mkdir(parents=True, exist_ok=True)

    def get_download_url(self, dataset_id: str) -> str:
        """
        Get temporary download URL from Data.gov.sg
        """

        url = f"{BASE_URL}/{dataset_id}/initiate-download"

        response = requests.get(url)

        response.raise_for_status()

        payload = response.json()

        if payload["code"] != 0:
            raise Exception(payload["errorMsg"])

        return payload["data"]["url"]

    def download_csv(self, download_url: str, destination: Path):
        """
        Download CSV in streaming mode.
        """

        if destination.exists():

            print(f"✓ {destination.name} already exists")

            return

        print(f"Downloading {destination.name}")

        response = requests.get(download_url, stream=True)

        response.raise_for_status()

        with open(destination, "wb") as file:

            for chunk in response.iter_content(chunk_size=8192):

                if chunk:

                    file.write(chunk)

        print(f"✓ Saved to {destination}")

    def download_all(self):
        """
        Download all configured datasets.
        """

        print("\nDownloading datasets...\n")

        for dataset in self.datasets:

            print("-" * 60)

            print(f"Dataset : {dataset['name']}")

            download_url = self.get_download_url(
                dataset["dataset_id"]
            )

            destination = (
                RAW_PATH /
                f"{dataset['name']}.csv"
            )

            self.download_csv(
                download_url,
                destination
            )

        print("\nAll downloads completed.")