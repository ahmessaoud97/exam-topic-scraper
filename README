# Exam Topic Scraper

**Exam Topic Scraper** scrapes exam topics for various certifications (e.g., AWS, Azure) from the web and compiles them into a well-structured PDF document for study purposes.

## 📦 Features
- Scrapes the top Google result for each exam topic page.
- Supports multiple certification types, including AWS, Azure, and more.
- Generates a formatted PDF with all scraped content.
- Configurable output file format and page numbers.

## 🚀 Usage

### Installation
Make sure you have Poetry installed, or follow the installation steps from [Poetry's official documentation](https://python-poetry.org/docs/#installation).

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/exam-topic-scraper.git
    cd exam-topic-scraper
    ```

2. Install dependencies:
    ```bash
    poetry install
    ```

3. Configure your Google Custom Search API (API Key and CSE ID) in `config/config.py`.

4. Run the scraper to fetch exam topics and generate a PDF:
    ```bash
    poetry run python src/main.py --cert "AWS Certified Developer" --pages 3 --output aws.pdf
    ```

    Parameters:
    - `--cert`: Name of the certification (e.g., "AWS Certified Developer", "Azure Fundamentals").
    - `--pages`: Number of pages to scrape from Google.
    - `--output`: Path to save the generated PDF (default: `output.pdf`).

## 🧪 Dev Tools
- **black**: Code formatter.
- **flake8**: Linter.
- **mypy**: Type checker.
- **isort**: Import sorter.

### Running Dev Tools
Before pushing your changes, run the following to ensure the code adheres to project standards:

```bash
poetry run black .
poetry run flake8 .
poetry run isort .
poetry run mypy .
