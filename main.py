import sqlite3

# Create a database and a table to store medications
conn = sqlite3.connect('medicines.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS medicines
             (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, dosage TEXT, frequency TEXT)''')
conn.commit()
1 
# Function to add a new medication
def add_medicine(name, dosage, frequency):
    c.execute("INSERT INTO medicines (name, dosage, frequency) VALUES (?, ?, ?)", (name, dosage, frequency))
    conn.commit()
    print("Medication added successfully.")

# Function to display all medications
def show_medicines():
    c.execute("SELECT * FROM medicines")
    medicines = c.fetchall()
    if len(medicines) > 0:
        print("Medication List:")
        for medicine in medicines:
            print("ID:", medicine[0])
            print("Name:", medicine[1])
            print("Dosage:", medicine[2])
            print("Frequency:", medicine[3])
            print("----------------------")
    else:
        print("No medications registered currently.")

# Function to delete a medication
def delete_medicine(medicine_id):
    c.execute("DELETE FROM medicines WHERE id=?", (medicine_id,))
    conn.commit()
    print("Medication deleted successfully.")

# Function to update frequency of a medication
def update_frequency(medicine_id, new_frequency):
    c.execute("UPDATE medicines SET frequency=? WHERE id=?", (new_frequency, medicine_id))
    conn.commit()
    print("Frequency updated successfully.")

# Menu options
def print_menu():
    print("1. Add a new medication")
    print("2. Show medications")
    print("3. Delete a medication")
    print("4. Update frequency")
    print("5. Exit")

# Main program
while True:
    print_menu()
    choice = input("Please enter the option number: ")
    if choice == '1':
        name = input("Name: ")
        dosage = input("Dosage: ")
        frequency = input("Frequency: ")
        add_medicine(name, dosage, frequency)
    elif choice == '2':
        show_medicines()
    elif choice == '3':
        medicine_id = input("Enter the ID of the medication to delete: ")
        delete_medicine(medicine_id)
    elif choice == '4':
        medicine_id = input("Enter the ID of the medication to update frequency: ")
        new_frequency = input("New frequency: ")
        update_frequency(medicine_id, new_frequency)
    elif choice == '5':
        break
    else:
        print("Invalid option. Please try again.")

# Close the database when the program finishes
conn.close()