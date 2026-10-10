# File_Operator
PROJECT 6: PERSONAL JOURNAL MANAGER

1. Overview
Personal Journal Manager is a menu-driven Python application that allows users to add, view, search, and delete journal entries. Each new entry is saved with the current date and time. The program uses a text file to store entries so they remain available after the program closes.
2. Video Demonstration
▶️ Click here to watch the project video: https://drive.google.com/file/d/11MXQ1_a89OjtDgeFlzVzucjLXqeAwylR/view?usp=sharing

4. Objectives
●	Understand file handling in Python.
●	Store and retrieve journal entries using a text file.
●	Add timestamps to journal entries.
●	Search for entries using a keyword or date.
●	Handle common file-related errors using exception handling.
●	Apply object-oriented programming through a JournalManager class.

6. Features
●	Add a New Entry: Saves journal text with a timestamp.
●	View All Entries: Displays all saved journal entries.
●	Search for an Entry: Finds entries containing a specified keyword or date.
●	Delete All Entries: Requests confirmation before deleting the journal file.
●	Timestamp Support: Records when each entry is added.
●	Input Validation: Prevents empty entries and empty search keywords.
●	Exception Handling: Handles missing files, permission issues, and other file errors.
●	Menu-Driven Interface: Offers numbered options for each operation.

7. Python Concepts Used
●	Classes and Objects — JournalManager organizes the journal operations.
●	Methods — separate methods add, view, search, and delete entries.
●	File Handling — open(), read(), write(), and file modes "a" and "r".
●	Context Manager — with open(...) manages file access safely.
●	Exception Handling — handles FileNotFoundError, PermissionError, and OSError.
●	Loops and Conditional Statements — control the menu and user choices.
●	String Methods — strip(), lower(), splitlines(), and startswith() help validate and search text.
●	Date and Time — datetime.now() and strftime() create timestamps.
●	OS Module — os.path.exists() checks for the file and os.remove() deletes it.

8. Program Menu
1.	1. Add a New Entry
2.	2. View All Entries
3.	3. Search for an Entry
4.	4. Delete All Entries
5.	5. Exit

Main Menu:
=================================================================\n                 PERSONAL JOURNAL MANAGER\n=================================================================\n1. Add a New Entry\n2. View All Entries\n3. Search for an Entry\n4. Delete All Entries\n5. Exit\nPlease select an option: 1
Adding an Entry:
Enter your journal entry: Today I learned Python file handling.\nEntry added successfully!
Example of a Saved Entry:
[2026-10-10 18:30:00]\nToday I learned Python file handling.
Note: The timestamp is an example; the program generates the actual date and time.
8. Input Validation and Error Handling
●	Empty journal entries are not saved.
●	Empty search keywords are rejected.
●	A helpful message appears if the journal file does not exist.
●	PermissionError and other file-system errors are handled.
●	Deletion requires a yes/no confirmation.
●	Invalid menu choices display an error message.
9. How to Run the Program
6.	Install Python if it is not already installed.
7.	Open Python IDLE or another Python editor.
8.	Create a new Python file and paste the project code.
9.	Save the file as personal_journal_manager.py.
10.	Press F5 in IDLE to run the program.
11.	Choose an option from the menu and follow the instructions.
10. Program Structure
●	JournalManager class — contains all journal operations.
●	add_entry() — saves a new entry with a timestamp.
●	view_entries() — reads and displays saved entries.
●	search_entry() — searches entries by keyword or date.
●	delete_entries() — confirms and deletes all journal entries.
●	Main menu loop — displays options until Exit is selected.
●	journal.txt — stores entries and is created when the first entry is added.
11. Assumptions and Limitations
●	Entries are stored locally in a plain-text file named journal.txt.
●	The current delete option removes all entries, not one selected entry.
●	The program does not include password protection or encryption.
●	Search uses a simple case-insensitive match against entry text and timestamps.

13. Author
Dhruvi Manoj Das
14. License
This project was created for educational and learning purposes. It may be used and modified for personal learning with appropriate credit to the author.
