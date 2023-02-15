import time
import numpy as np
import mysql.connector

samples = 1000
list_sample = np.arange(samples)
sin_value = np.sin(6*np.pi*(list_sample / samples))

# Connect to the MySQL database

max_retries = 50
retry_interval_seconds = 10

conn = None
for i in range(max_retries):
    try:
        conn = mysql.connector.connect(user='root', password='root', host='mysql', port=3306, database='grafana')
        break  # Connection successful, exit loop
    except Exception as e:
        print(f"Failed to connect. Retrying in {retry_interval_seconds} seconds.")
        time.sleep(retry_interval_seconds)

if conn:
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sine (
        id INT AUTO_INCREMENT PRIMARY KEY,
        x BIGINT,
        y FLOAT
    )
    """)

    # Insert the data into the table
    for i in range(len(list_sample)):
        cursor.execute("INSERT INTO sine (x, y) VALUES (%s, %s)", (float(list_sample[i]), float(sin_value[i])))

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()
    print(f"Successfully inserted data to MySQL.")
else:
    print(f"Failed to connect in 20 tries.")
