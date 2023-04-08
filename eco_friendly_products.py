import sqlite3

def create_connection():
    conn = sqlite3.connect('eco_friendly_products.db')
    return conn

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
    
    # Add eco-friendly products (name, category, description, price)
    products = [('Bamboo Toothbrush', 'Personal Care', 'A biodegradable toothbrush made from bamboo', 3.99),
                ('Reusable Shopping Bag', 'Accessories', 'A reusable and washable shopping bag made from recycled materials', 8.99),
                ('Solar Charger', 'Electronics', 'A portable solar charger for your devices', 24.99),
                ('Stainless Steel Water Bottle', 'Drinkware', 'A reusable, insulated stainless steel water bottle', 19.99)]

    for product in products:
        insert_product(conn, product)

    conn.close()

if __name__ == '__main__':
    main()