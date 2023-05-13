import sqlite3

def create_connection():
    conn = sqlite3.connect('listings.db')
    return conn

def create_table(item_name):
    conn = create_connection()
    c = conn.cursor()

    item_name = item_name.replace(" ", "_")

    c.execute(f'''CREATE TABLE IF NOT EXISTS {item_name} (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 user TEXT,
                 platinum INTEGER,
                 order_type TEXT,
                 platform TEXT)''')

    conn.commit()
    conn.close()

def add_orders(item_name, orders):
    conn = create_connection()
    c = conn.cursor()

    item_name = item_name.replace(" ", "_")

    for order in orders:
        user = order["user"]["ingame_name"]
        platinum = order["platinum"]
        order_type = order["order_type"]
        platform = order["platform"]

        c.execute(f"INSERT INTO {item_name} (user, platinum, order_type, platform) VALUES (?, ?, ?, ?)",
                  (user, platinum, order_type, platform))

    conn.commit()
    conn.close()

def get_orders(item_name, order_type):
    conn = create_connection()
    c = conn.cursor()
    
    if order_type == 'buy':
        c.execute(f"SELECT * FROM {item_name} WHERE order_type = 'buy' ORDER BY platinum ASC LIMIT 10")
    elif order_type == 'sell':
        c.execute(f"SELECT * FROM {item_name} WHERE order_type = 'sell' ORDER BY platinum DESC LIMIT 10")
    else:
        print('Invalid order type')
        return []

    rows = c.fetchall()
    conn.close()
    
    return rows
