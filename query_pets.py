import sqlite3

def query_pets():
    connection = sqlite3.connect('pets.db')
    cursor = connection.cursor()

    while True:
        person_id = input("Enter a person's ID (-1 to exit): ")
        if person_id == '-1':
            print("Exiting the program.")
            break

        # Check if the person exists
        cursor.execute("SELECT first_name, last_name, age FROM person WHERE id = ?;", (person_id,))
        person = cursor.fetchone()

        if not person:
            print(f"No person found with ID {person_id}.")
        else:
            first_name, last_name, age = person
            print(f"{first_name} {last_name}, {age} years old")

            # Fetch the person's pets
            cursor.execute("""
                SELECT pet.name, pet.breed, pet.age, pet.dead
                FROM pet
                INNER JOIN person_pet ON pet.id = person_pet.pet_id
                WHERE person_pet.person_id = ?;
            """, (person_id,))

            pets = cursor.fetchall()
            if pets:
                for pet in pets:
                    pet_name, breed, pet_age, is_dead = pet
                    status = "that is deceased" if is_dead else "that is alive"
                    print(f"{first_name} owned {pet_name}, a {breed}, that was {pet_age} years old {status}.")
            else:
                print(f"{first_name} {last_name} does not own any pets.")

    connection.close()

if __name__ == "__main__":
    query_pets()
