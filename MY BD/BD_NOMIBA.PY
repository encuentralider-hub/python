import sqlite3

# 1. Connect to the database (creates the file if it doesn't exist)
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# 2. Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS DR1_CAT_NOM_002 (
        002_codigo TEXT PRIMARY KEY,
        002_nombre TEXT,
        002_apellido TEXT,
        002_sueldo INTEGER
    )
''')

# 3. Insert some data
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")

# 4. Save (commit) the changes and close the connection
conn.commit()
conn.close()

print("Data saved successfully!")