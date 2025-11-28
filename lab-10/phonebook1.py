import psycopg2
import csv

def connect_db():
    try:
        connection = psycopg2.connect(
            dbname="phonebookdb",
            user="postgres",
            password="12345",
            host="localhost",
            port="5432"
        )
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table():
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                surname VARCHAR(100),
                name VARCHAR(100),
                phone VARCHAR(20)
            )
        """)
        connection.commit()
        cursor.close()
        connection.close()

def insert_data_from_csv(csv_file):
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                surname, name, phone = row
                cursor.execute(
                    "INSERT INTO phonebook (surname, name, phone) VALUES (%s, %s, %s)",
                    (surname, name, phone)
                )
        connection.commit()
        cursor.close()
        connection.close()
        print("Data successfully inserted from CSV.")

def insert_data_from_console():
    surname = input("Enter surname: ")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO phonebook (surname, name, phone) VALUES (%s, %s, %s)",
            (surname, name, phone)
        )
        connection.commit()
        cursor.close()
        connection.close()
        print("Data successfully added.")

def update_data():
    record_id = input("Enter ID of the record to update: ")
    column = input("What do you want to update (surname/name/phone)? ").strip().lower()
    if column not in ["surname", "name", "phone"]:
        print("Invalid column. Only 'surname', 'name', or 'phone' are allowed.")
        return

    new_value = input(f"Enter new value for {column}: ")
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute(f"UPDATE phonebook SET {column} = %s WHERE id = %s", (new_value, record_id))
        connection.commit()
        cursor.close()
        connection.close()
        print("Record successfully updated.")

def query_data():
    connection = connect_db()
    if not connection:
        return
    cursor = connection.cursor()

    filter_type = input("Enter filter (surname/name/phone or press Enter to show all): ").strip().lower()
    filter_value = input("Enter value to search: ").strip() if filter_type else None

    try:
        if not filter_type:
            cursor.execute("SELECT * FROM phonebook ORDER BY id")
        elif filter_type in ["surname", "name", "phone"]:
            cursor.execute(f"SELECT * FROM phonebook WHERE {filter_type} ILIKE %s ORDER BY id", ('%' + filter_value + '%',))
        else:
            print("Invalid filter type.")
            return

        rows = cursor.fetchall()
        if rows:
            print("\n--- Phonebook Entries ---")
            for row in rows:
                print(f"ID: {row[0]}, Surname: {row[1]}, Name: {row[2]}, Phone: {row[3]}")
        else:
            print("No entries found.")
    except Exception as e:
        print("Error querying data:", e)
    finally:
        cursor.close()
        connection.close()

def delete_data():
    column = input("Delete by what? (surname/name/phone): ").strip().lower()
    if column not in ["surname", "name", "phone"]:
        print("Invalid column.")
        return

    value = input(f"Enter exact value of {column} to delete: ").strip()
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM phonebook WHERE {column} ILIKE %s", (value,))
        rows = cursor.fetchall()
        if not rows:
            print("No entries found for deletion.")
        else:
            print("Found the following entries:")
            for row in rows:
                print(f"ID: {row[0]}, Surname: {row[1]}, Name: {row[2]}, Phone: {row[3]}")
            confirm = input("Delete all these entries? (yes/no): ").strip().lower()
            if confirm == "yes":
                cursor.execute(f"DELETE FROM phonebook WHERE {column} ILIKE %s", (value,))
                connection.commit()
                print("Entries deleted.")
        cursor.close()
        connection.close()

def delete_by_id():
    id_to_delete = input("Enter ID of the record to delete: ")
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM phonebook WHERE id = %s", (id_to_delete,))
        row = cursor.fetchone()
        if row:
            print(f"Found record: ID: {row[0]}, Surname: {row[1]}, Name: {row[2]}, Phone: {row[3]}")
            confirm = input("Delete this record? (yes/no): ").strip().lower()
            if confirm == "yes":
                cursor.execute("DELETE FROM phonebook WHERE id = %s", (id_to_delete,))
                connection.commit()
                print("Record deleted.")
        else:
            print("No record found with this ID.")
        cursor.close()
        connection.close()

if __name__ == "__main__":
    create_table()
    while True:
        print("\nOptions:")
        print("1. Insert data from CSV")
        print("2. Insert data manually")
        print("3. Update data")
        print("4. Show entries")
        print("5. Delete by surname, name, or phone")
        print("6. Delete by ID")
        print("7. Exit")
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            insert_data_from_csv('data.csv')
        elif choice == "2":
            insert_data_from_console()
        elif choice == "3":
            update_data()
        elif choice == "4":
            query_data()
        elif choice == "5":
            delete_data()
        elif choice == "6":
            delete_by_id()
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")
