import sqlite3

def load_data():
    connection = sqlite3.connect('pets.db')
    cursor = connection.cursor()

    # Insert data into the person table
    cursor.executemany(
        "INSERT INTO person (id, first_name, last_name, age) VALUES (?, ?, ?, ?);",
        [
            (1, 'James', 'Smith', 41),
            (2, 'Diana', 'Greene', 23),
            (3, 'Sara', 'White', 27),
            (4, 'William', 'Gibson', 23)
        ]
    )

    # Insert data into the pet table
    cursor.executemany(
        "INSERT INTO pet (id, name, breed, age, dead) VALUES (?, ?, ?, ?, ?);",
        [
            (1, 'Rusty', 'Dalmatian', 4, 1),
            (2, 'Bella', 'Alaskan Malamute', 3, 0),
            (3, 'Max', 'Cocker Spaniel', 1, 0),
            (4, 'Rocky', 'Beagle', 7, 0),
            (5, 'Rufus', 'Cocker Spaniel', 1, 0),
            (6, 'Spot', 'Bloodhound', 2, 1)
        ]
    )

    # Insert data into the person_pet table
    cursor.executemany(
        "INSERT INTO person_pet (person_id, pet_id) VALUES (?, ?);",
        [
            (1, 1), (1, 2),
            (2, 3), (2, 4),
            (3, 5), (4, 6)
        ]
    )

    connection.commit()
    connection.close()

if __name__ == "__main__":
    load_data()
    print("Data loaded into pets.db successfully!")
