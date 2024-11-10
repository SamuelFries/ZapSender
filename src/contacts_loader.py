import csv

def load_contacts(file_path):
    contacts = []
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                contacts.append(row[0])
        print(f"Loaded {len(contacts)} contacts.")
    except Exception as e:
        print(f"Failed to load contacts. Error: {str(e)}")
    return contacts