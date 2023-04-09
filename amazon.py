import requests
from bs4 import BeautifulSoup
import csv

def get_climate_pledge_friendly_products(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    products = []

    for product in soup.findall('div', class='s-result-item'):
        if product.find('span', class='a-badge-text'):
            if "Climate Pledge Friendly" in product.find('span', class='a-badge-text').text.strip():
                productname = product.find('span', class='a-size-medium a-color-base a-text-normal')
                if product_name:
                    products.append(product_name.text)

    return products


def main():
    base_url = 'https://www.amazon.com/s?k=climate+pledge+friendly&page='
    all_products = []

    for page_num in range(1, 11):  # Adjust the range to increase or decrease the number of pages to scrape
        url = base_url + str(page_num)
        print(f"Scraping page {page_num}...")
        products = get_climate_pledge_friendly_products(url)
        all_products.extend(products)

    with open('climate_pledge_friendly_products.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Product Name'])
        for product in all_products:
            writer.writerow([product])

    print("Scraping complete. Results saved to climate_pledge_friendly_products.csv")


if name == "main":
    main()