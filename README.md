# E-Result-Analysis

A system to retrieve PDF files from university websites and analysing results.

* scrape_pdfs.py - web scraping the PDFs from a website (needs website specific modifications)
* PDF_to_Excel.py - converts compatible PDFs to xlsx files, uses pdftables api
* analyse.py - analyses the content of the converted sheets and displays them to registered user (after simple authentication)
