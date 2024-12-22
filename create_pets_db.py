import sqlite3

def create_db():
    connection = sqlite3.connect('pets.db')
    cursor = connection.cursor()

    # Drop tables if they already exist
    cursor.execute("DROP TABLE IF EXISTS person;")
    cursor.execute("DROP TABLE IF EXISTS pet;")
    cursor.execute("DROP TABLE IF EXISTS person_pet;")

    # Create tables
    cursor.execute("""
        CREATE TABLE person (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            age INTEGER
        );
    """)

    cursor.execute("""
        CREATE TABLE pet (
            id INTEGER PRIMARY KEY,
            name TEXT,
            breed TEXT,
            age INTEGER,
            dead INTEGER
        );
    """)

    cursor.execute("""
        CREATE TABLE person_pet (
            person_id INTEGER,
            pet_id INTEGER
        );
    """)

    connection.commit()
    connection.close()
    print("Database schema created in pets.db!")

if __name__ == "__main__":
    create_db()
