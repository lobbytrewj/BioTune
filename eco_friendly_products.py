import pymongo
import requests
from bs4 import BeautifulSoup

def scrape_ecoroots_products(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    product_list = []

    for product_div in soup.find_all('div', class_='grid__item small--one-half medium-up--one-quarter'):
        product_name = product_div.find('div', class_='product-card__title').text.strip()
        product_category = 'Not specified'  # Modify this based on your needs.
        product_description = ''  # Product descriptions are not available on the category page.
        product_price = float(product_div.find('span', class_='price-item price-item--regular').text.strip().replace('$', ''))

        product_list.append((product_name, product_category, product_description, product_price))

    return product_list

def scrape_earth_hero_products(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    product_list = []

    for product_div in soup.find_all('div', class_='product-item'):
        product_name = product_div.find('h2', class_='woocommerce-loop-product__title').text.strip()
        product_category = 'Not specified'  # Modify this based on your needs.
        product_description = ''  # Product descriptions are not available on the category page.
        product_price = float(product_div.find('span', class_='woocommerce-Price-amount').text.strip().replace('$', ''))

        product_list.append((product_name, product_category, product_description, product_price))

    return product_list

def main():
    # Connect to the MongoDB server
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Create a new database (or connect to an existing one)
    db = client["eco_friendly_products"]

    # Create a new collection (or connect to an existing one)
    products = db["products"]   

    ecoroots_url = 'https://ecoroots.us/collections/zero-waste-products'
    ecoroots_products = scrape_ecoroots_products(ecoroots_url)

    for product in ecoroots_products:
        product_document = {
            "name": product[0],
            "category": product[1],
            "description": product[2],
            "price": product[3],
        }
        products.insert_one(product_document)

    earth_hero_url = 'https://earthhero.com/product-category/zero-waste-lifestyle/'
    earth_hero_products = scrape_earth_hero_products(earth_hero_url)

    for product in earth_hero_products:
        product_document = {
            "name": product[0],
            "category": product[1],
            "description": product[2],
            "price": product[3],
        }
        products.insert_one(product_document)
        
if __name__ == '__main__':
    main()