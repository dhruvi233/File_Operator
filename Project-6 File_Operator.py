import os
from datetime import datetime

class JournalManager:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        try:
            entry = input("\nEnter your journal entry:")

            if entry.strip() =="":
                print("Journal entry cannot be empty.")
                return
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(f"[{timestamp}]\n")
                file.write(entry + "\n\n")

            print("\nEntry added successfully!")

        except PermissionError:
            print("Error: Permission denied while writing to the file.")
        except OSError as error:
            print("File error:", error)

    def view_entries(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                entries = file.read()

            if entries.strip() == "":
                print("\nYour journal is empty.")
                return
            else:
                print("\nYour Journal Entries:")
                print("----------------------------------------------")
                print(entries)

        except FileNotFoundError:
            print("\nNo journal entries found. Start by adding a new entry.")
        except PermissionError:
            print("Error: Permission denied while reading the file.")
        except OSError as error:
            print("File error:", error)

    def search_entry(self):
        try:
            keyword = input("\nEnter a keyword or date to search:").strip()

            if keyword == "":
                print("Search keyword cannot be empty.")
                return
            with open(self.filename, "r", encoding="utf-8") as file:
                entries = file.read()
            matching_entries = []
            current_entry = []

            for line in entries.splitlines():
                if line.startswith("[") and line.endswith("]"):
                    if current_entry:
                        matching_entries.append("\n".join(current_entry))
                    current_entry = [line]
                elif line.strip():
                    current_entry.append(line)
            if current_entry:
                matching_entries.append("\n".join(current_entry))
            found = False
            print("\nMatching Entries:")
            print("---------------------------------------------------")
            for entry in matching_entries:
                if keyword.lower() in entry.lower():
                    print(entry)
                    print()
                    found = True
            if not found:
                print("No entries were found for:", keyword)
    
        except FileNotFoundError:
            print("\nError: The journal file does not exist.")
            print("Please add a new entry first.")
        except PermissionError:
            print("Error: Permission denied while reading the file.")
        except OSError as error:
            print("File error:", error)
    def delete_entries(self):
        try:
            if not os.path.exists(self.filename):
                print("\nNo journal entries to delete.")
                return
            confirmation = input("\nAre you sure you want to delete all entries? (yes/no):").strip().lower()
            if confirmation == "yes":
                os.remove(self.filename)
                print("\nAll journal entries have been deleted.")
            elif confirmation == "no":
                print("\nDeletion cancelled.")
            else:
                print("\nInvalid response. Please enter yes or no.")
        except PermissionError:
            print("Error: Permission denied while deleting the file.")
        except OSError as error:
            print("File error:", error)

journal = JournalManager()

while True:
    print("\n=================================================================")
    print("                 PERSONAL JOURNAL MANAGER")
    print("===================================================================")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("\nPlease select an option:").strip()

    if choice == "1":
        journal.add_entry()
    elif choice == "2":
        journal.view_entries()
    elif choice == "3":
        journal.search_entry()
    elif choice == "4":
        journal.delete_entries()
    elif choice == "5":
        print("\nThank you for using Personal Journal Manager.")
        print("Goodbye!")
        break
    else:
        print("\nInvalid option. Please select a valid option.")
                

            
                
