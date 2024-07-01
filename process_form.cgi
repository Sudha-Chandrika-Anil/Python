#!C:\Users\admin\AppData\Local\Programs\Python\Python310\python.exe
import cgi
import mysql.connector

# Function to establish database connection
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='Python',  # Replace with your database name
            user='root',        # Replace with your database username
            password=''         # Replace with your database password
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Database connection error: {e}")
        return None

# Print HTTP header
print("Content-Type: text/html")
print()

# Retrieve form data
form = cgi.FieldStorage()
action = form.getvalue('action')

# Database connection
conn = connect_to_database()

# Handle different CRUD operations
if action == 'insert':
    # Insert Operation
    name = form.getvalue('name')
    if conn:
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO student (name) VALUES (%s)"
            cursor.execute(sql, (name,))
            conn.commit()
            cursor.close()
            print("<h1>Data inserted successfully!</h1>")
        except mysql.connector.Error as e:
            print(f"Error inserting data: {e}")

elif action == 'update':
    # Update Operation
    update_id = form.getvalue('update_id')
    new_name = form.getvalue('new_name')
    if conn:
        try:
            cursor = conn.cursor()
            sql = "UPDATE student SET name = %s WHERE id = %s"
            cursor.execute(sql, (new_name, update_id))
            conn.commit()
            cursor.close()
            print(f"<h1>Record ID '{update_id}' updated successfully!</h1>")
        except mysql.connector.Error as e:
            print(f"Error updating record: {e}")

elif action == 'delete':
    # Delete Operation
    delete_id = form.getvalue('delete_id')
    if conn:
        try:
            cursor = conn.cursor()
            sql = "DELETE FROM student WHERE id = %s"
            cursor.execute(sql, (delete_id,))
            conn.commit()
            cursor.close()
            print(f"<h1>Record ID '{delete_id}' deleted successfully!</h1>")
        except mysql.connector.Error as e:
            print(f"Error deleting record: {e}")

elif action == 'view':
    # View Operation (Read all records)
    if conn:
        try:
            cursor = conn.cursor()
            sql = "SELECT id, name FROM student"
            cursor.execute(sql)
            rows = cursor.fetchall()
            cursor.close()

            # Print HTML response
            print("<h1>Student Records</h1>")
            if rows:
                print("<table border='1'>")
                print("<tr><th>ID</th><th>Name</th></tr>")
                for row in rows:
                    print(f"<tr><td>{row[0]}</td><td>{row[1]}</td></tr>")
                print("</table>")
            else:
                print("<p>No records found</p>")
        except mysql.connector.Error as e:
            print(f"Error retrieving records: {e}")

# Close database connection
if conn:
    conn.close()




