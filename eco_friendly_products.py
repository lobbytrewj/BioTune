import pymongo

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
    insert_result = products.insert_one(product)
    print(f"Inserted product with ID: {insert_result.inserted_id}")