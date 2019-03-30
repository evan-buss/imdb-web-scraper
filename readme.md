# CSC459 Big Data - Scrapy Reasearch

Scrapy is a python framework for scraping data and crawling websites.

## Project

This repository contains various Scrapy demo spiders.
  - Quotes scraper
  - IMDB movies scraper

It also contains a simple http server to view the scraped data from the spiders.

The spiders save their data to an SQLite3 database. The website queries data from
the database.

# Setup
*I recommend using venv to isolate your project dependencies*

- Create a new virtual environment with venv
  - `python3 -m venv environment`
- Install the package dependencies
  - `pip install -r requirements.txt`
  - Flask + Dependencies (Server)
  - Scrapy + Dependencies

## Running the Scrapy Spiders

- Run a spider using the name defined within the class
  - `scrapy crawl movies`
  - Current List of Available Spiders:
    - `movies`
    - `quotes`

- Run scrapy interactively to test html selectors
  - `scrapy shell [url]`
  - You can then execute selections
    - Ex) `response.css('div.summary::text').get()`

## Running the Flask Server

- Set the shell environment variables
  - `set FLASK_APP=server`
  - `set FLASK_ENV=development`
- Start the server
  - `flask run`
- Site Pages
  - /movies
    - List of all database movies
    - Supports title search and pagination
