# Web Scraping with Scrapy and Playwright

## Overview

This project contains two Scrapy spiders, one utilizing Playwright for web scraping and the other retrieving data by calling an API endpoint.

## Files

### [Playwright.py](https://github.com/Harry262000/Interview_Assignment/blob/main/CrowdA/CrowdA/spiders/playwrite.py)


This Python file contains a Scrapy spider named `CrowdAP` that utilizes Playwright for web scraping.

**Content:**
- **Scrapy Spider:**
  - **Name:** CrowdASpider
  - Utilizes Playwright for web scraping.
- **Custom Settings:**
  - Aborts certain requests based on resource type and HTTP method using should_abort_request.
- **Start Requests:**
  - Initiates web scraping by sending a request to a specified URL.
  - Configures Playwright with specific methods to execute, including waiting for a selector and scrolling the page.
- **Parsing:**
  - Parses the response asynchronously.
  - Closes the Playwright page after parsing.
- **Error Handling:**
  - Handles errors by closing the Playwright page if necessary.

**Major Differences:**
- **Web Scraping Method:**
  - Utilizes Playwright, a browser automation tool, to scrape data directly from web pages.
  - Capable of handling dynamic content and executing JavaScript on web pages.
- **Page Interaction:**
  - Interacts with the web page by waiting for specific elements to appear (wait_for_selector) and scrolling the page.
- **Data Extraction:**
  - Extracts data directly from the rendered web page using Playwright's methods.

### [CrowdA.py](https://github.com/Harry262000/Interview_Assignment/blob/main/CrowdA/CrowdA/spiders/CrowdA.py)

This Python file contains a Scrapy spider named `CrowdA` that retrieves data by calling an API endpoint.

**Content:**
- **Scrapy Spider:**
  - **Name:** CrowdA
  - Retrieves data by calling an API endpoint.
- **Start Requests:**
  - Initiates data retrieval by sending a request to a specified API URL.
  - Parses the JSON response and yields extracted data.
- **Parsing API Response:**
  - Parses the JSON response asynchronously.
  - Extracts specific data fields from the API response.

**Major Differences:**
- **Data Source:**
  - Retrieves structured data (JSON) from a predefined API endpoint.
  - Does not involve web scraping; data is obtained directly from the API.
- **API Interaction:**
  - Makes HTTP requests to the API endpoint and handles the JSON response.
- **Data Extraction:**
  - Extracts data from the JSON response received from the API.

## Credits

- Created by [Harshal Honde](https://github.com/Harry262000)
