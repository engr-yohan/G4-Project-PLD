# Address Book

This group project is an address book application built primarily in Python, designed to store up to 100 contact entries. It serves as a digital container for essential details like names, addresses, and phone numbers, allowing users to add, manage, and retrieve information. By providing structured access to both input data and output responses, the app offers a simple yet efficient way to organize personal or professional contacts.

## Installation

### Known Issues
- **edit()**: Only the first and last names are available for editing contacts.
- **search()**: In the revision, it does not operate correctly.
- **delete()**: The data is never shown, and you can only remove entries by knowing their designated number in the address book.
- **view()**: There is no "back" option, so you must exit to return to the home screen.

## Project Structure
```
G4-Project-PLD/
├─ main.py
├─ database.py
├─ app_database.db
├─ README.md
├─ picture_logo/
│  ├─ picture_1.jpg
│  ├─ picture_2.jpg
│  ├─ picture_3.jpg
│  ├─ picture_4.png
│  ├─ picture_5.png
│  └─ picture_6.png
└─ __pycache__/
```