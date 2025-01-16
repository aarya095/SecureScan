import mysql.connector

# Establish MySQL Connection
try:
    connection = mysql.connector.connect(
        host="localhost",  # Change to your MySQL host
        user="root",  # Change to your MySQL username
        password="employee123",  # Change to your MySQL password
        database="secure_scan"  # Change to your database name
    )

    if connection.is_connected():
        print("✅ Successfully connected to MySQL database")

        # Get MySQL Server info
        db_info = connection.get_server_info()
        print("MySQL Server Version:", db_info)

        # Close Connection
        connection.close()
        print("✅ MySQL connection closed")

except mysql.connector.Error as e:
    print("❌ Error connecting to MySQL:", e)
