# IMDB Web Scraper

Scrapy is a python framework for scraping data and crawling websites. I have created various crawlers to learn Scrapy and improve my Python skills

## Project

This repository contains various Scrapy demo spiders.
  - Quotes Scraper
  - IMDB movies scraper
  - Books Scraper

It also contains a simple http server to view the scraped data from the spiders.

The spiders save their data to an SQLite3 database. The website queries data from
the database.

# Setup
*I recommend using virtualenv to isolate your project dependencies*

- Install virtualenv
  - `sudo pip3 install --user virtualenv`
  - *May have to use `sudo -H` with newer versions*

- Create a new virtual environment with venv
  - `virtualenv env`
- Active the virtual environment
  - `source env/bin/activate`
- Install the package dependencies
  - `pip install -r requirements.txt`
  - Scrapy + Dependencies (Spiders)
  - Flask + Dependencies (Server)

## Running the Scrapy Spiders

- Run a spider using the name defined within the class
  - `scrapy crawl movies`
  - Current List of Available Spiders:
    - `movies`
      - Scrapes IMDB movie data and saves it to an SQLite3 database
    - `quotes`
    - `books`

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
    - List of all movies contained in database
    - Supports title search and pagination
    
## Simple Flask Site to View and Search Scraped Data
![homepage](https://github.com/evan-buss/imdb-web-scraper/blob/master/screenshot/Screen%20Shot%202019-10-07%20at%2020.57.41.png)
