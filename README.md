# Webscraping and Downloading PDF Files from bitsavers.org

This project demonstrates how to scrape and download PDF files from bitsavers.org using Scrapy, a powerful web crawling and scraping framework in Python.

## Overview

Bitsavers.org is a valuable resource for vintage computer documentation, including manuals, schematics, and technical documents in PDF format. This project aims to automate the process of scraping and downloading these PDF files for archival or research purposes.

## Requirements

To run this project, you'll need:

- Python 3.x
- Scrapy
- CSV module (included in Python standard library)

## Getting Started

1. Clone this repository to your local machine:

```bash
git clone https://github.com/FaeyO/webscrape-and-download-pdf-file-from-bitsavers.org.git
```

2. Navigate to the project directory:

```bash
cd download
```

3. Install the required dependencies:

```bash
pip install scrapy
```

## Usage

1. Run the Scrapy spider to scrape the PDF files from bitsavers.org:

```bash
scrapy crawl pdf
```

2. The spider will collect data such as file names, links to PDF files, and other relevant information.

3. After scraping is complete, the data will be saved into a CSV file named `pdf_loader.csv` in the project directory.

4. PDF files will be downloaded to the `pdf_files` directory in the project directory.

## Understanding the Process

- The Scrapy spider (`pdf.py`) is responsible for crawling the bitsavers.org website and extracting PDF file links and metadata.

- Each PDF file link is downloaded using Scrapy's built-in file download capabilities.

- The extracted data, including file names and links, is stored in a CSV file (`pdf_loader.csv`) for further analysis or reference.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.


## Disclaimer

Please be mindful of the website's terms of use and copyright restrictions when scraping and downloading files from bitsavers.org. Respect the website's bandwidth and usage policies to avoid overloading their servers.

## Acknowledgements

Special thanks to bitsavers.org for providing a valuable resource for vintage computer documentation, and to the Scrapy community for creating and maintaining a powerful web scraping framework.

### website view

![image](https://github.com/FaeyO/webscrape-and-download-pdf-file-from-bitsavers.org/assets/118575325/c65c70c4-5664-4707-99e4-04c8e63131fe)
