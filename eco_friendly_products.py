import pymongo

# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a new database (or connect to an existing one)
db = client["eco_friendly_products"]

# Create a new collection (or connect to an existing one)
products = db["products"]

# Insert a document into the "products" collection
product = {
    "name": "Bamboo Toothbrush",
    "category": "Personal Care",
    "description": "A biodegradable toothbrush made from bamboo",
    "price": 3.99
}

insert_result = products.insert_one(product)
print(f"Inserted product with ID: {insert_result.inserted_id}")