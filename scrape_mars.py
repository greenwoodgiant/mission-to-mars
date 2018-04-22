from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd


def init_browser():
    executable_path = {'executable_path': 'C:\\Users\\itsch\\Desktop\\boot_camp\\homework\\mission_to_mars\\chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()
    mars_data = {}

    #
    # FEATURED HEADLINE
    #

    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)

    news_soup = BeautifulSoup(browser.html, 'html.parser')
    news_result = news_soup.find('li', class_='slide')

    headline = news_result.find('div', class_='content_title').text
    blurb = news_result.find('div', class_='article_teaser_body').text

    mars_data["news_headline"] = headline
    mars_data["news_tag"] = blurb

    #
    # FEATURED IMAGE
    #

    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)

    image_soup = BeautifulSoup(browser.html, 'html.parser')
    image_result = image_soup.find('article', class_='carousel_item')

    featured_image = image_result.find('a')['data-fancybox-href']
    featured_image = "https://www.jpl.nasa.gov" + featured_image
    featured_title = image_result.find('h1', class_="media_feature_title").text.strip()

    mars_data["image_url"] = featured_image
    mars_data["image_title"] = featured_title

    #
    # FEATURED WEATHER
    #

    tweet_url = "https://twitter.com/marswxreport"
    browser.visit(tweet_url)

    tweet_soup = BeautifulSoup(browser.html, 'html.parser')
    tweet_result = tweet_soup.find('div', class_='js-tweet-text-container')

    mars_weather = tweet_result.find('p').text

    mars_data["weather"] = mars_weather

    #
    # FACT TABLE
    #

    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)

    fact_soup = BeautifulSoup(browser.html, 'html.parser')
    fact_result = fact_soup.find('table', class_='tablepress-id-mars')

    fact_table = pd.read_html(str(fact_result))[0]
    fact_table.columns = ["Stats","Values"]
    fact_table.set_index("Stats",drop=True,inplace=True)
    html_table = fact_table.to_html()

    mars_data["fact_table"] = html_table

    #
    # HEMISPHERES
    #

    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
        {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
        ]
    mars_data["hemispheres"] = hemisphere_image_urls

    return mars_data

#print(scrape())