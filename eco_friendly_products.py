import sqlite3
import requests
from bs4 import BeautifulSoup
import os

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


def create_connection():
    database_path = os.path.join('/Users/EricJeong/Desktop/EcoSub', 'eco_friendly_products.db')
    print(f"Connecting to database at: {database_path}")
    conn = sqlite3.connect(database_path)
    print("Connection successful!")
    return conn

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


def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        category TEXT NOT NULL,
                        description TEXT,
                        price REAL);''')
    conn.commit()

def insert_product(conn, product):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, category, description, price) VALUES (?, ?, ?, ?)", product)
    conn.commit()

def main():
    conn = create_connection()
    create_table(conn)

    products = [('Bamboo Toothbrush', 'Personal Care', 'A biodegradable toothbrush made from bamboo', 3.99),
                # ... (unchanged)
                ('Stainless Steel Water Bottle', 'Drinkware', 'A reusable, insulated stainless steel water bottle', 19.99)]

    for product in products:
        insert_product(conn, product)

    ecoroots_url = 'https://ecoroots.us/collections/zero-waste-products'
    products2 = scrape_ecoroots_products(ecoroots_url)
    for product in products2:
        insert_product(conn, product)

    earth_hero_url = 'https://earthhero.com/product-category/zero-waste-lifestyle/'
    products3 = scrape_earth_hero_products(earth_hero_url)
    for product in products3:
        insert_product(conn, product)

    conn.close()

if __name__ == '__main__':
    main()




