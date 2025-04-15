from src.scraper import GoogleSearchAPI, scrape_page_content
from src.pdf_generator import generate_pdf
from config.config import GOOGLE_API_KEY, CSE_ID, PDF_OUTPUT_PATH, CERTIFICATION_NAME, TOTAL_PAGES


def main() -> None:
    api = GoogleSearchAPI(GOOGLE_API_KEY, CSE_ID)
    all_pages = []

    for page in range(1, TOTAL_PAGES + 1):
        query = f"exam topic {CERTIFICATION_NAME} {page}"
        print(f"🔍 Searching: {query}")
        url = api.fetch_first_result(query)

        if url:
            print(f"🌐 Scraping: {url}")
            content = scrape_page_content(url)
            all_pages.append((f"{query} - {url}", content))
        else:
            all_pages.append((query, "No result found."))

    generate_pdf(all_pages, PDF_OUTPUT_PATH)


if __name__ == "__main__":
    main()
