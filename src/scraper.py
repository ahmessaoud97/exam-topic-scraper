import requests
import time
from bs4 import BeautifulSoup
from config.config import MAX_RETRIES, RETRY_BACKOFF
import logging

logging.basicConfig(level=logging.INFO)

class GoogleSearchAPI:
    def __init__(self, api_key: str, cse_id: str):
        self.api_key = api_key
        self.cse_id = cse_id
        self.base_url = "https://www.googleapis.com/customsearch/v1"

    def fetch_first_result(self, query: str) -> str:
        url = f"{self.base_url}?q={query}&key={self.api_key}&cx={self.cse_id}"
        retries = 0

        while retries < MAX_RETRIES:
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                data = response.json()

                items = data.get("items", [])
                if not items:
                    logging.warning(f"No results for query: '{query}'")
                    break

                for item in items:
                    link = item.get("link", "")
                    if "examtopics.com/discussions/" in link:
                        return link

                return items[0].get("link", "https://www.google.com/search?q=" + query.replace(" ", "+"))

            except requests.RequestException as e:
                logging.error(f"Search API error (attempt {retries + 1}): {e}")
                retries += 1
                time.sleep(RETRY_BACKOFF ** retries)

        logging.error(f"All retries failed for query: '{query}'")
        return "https://www.google.com/search?q=" + query.replace(" ", "+")


def scrape_page_content(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")

        content = "\n\n".join(
            p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)
        )

        if not content:
            logging.warning(f"No readable content found on: {url}")
            return f"No readable content found on: {url}"

        return content

    except requests.RequestException as e:
        logging.error(f"Request error while scraping {url}: {e}")
        return f"Failed to scrape {url}: {e}"

    except Exception as e:
        logging.exception(f"Unexpected error while scraping {url}")
        return f"Failed to scrape {url}: {e}"
