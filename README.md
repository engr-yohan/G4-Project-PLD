# Address Book 4

## Overview

This is a comprehensive address book application built with Python and SQLite, designed to manage up to 100 contact entries. The application provides a user-friendly graphical interface (GUI) built with Tkinter, allowing users to efficiently store, organize, and retrieve contact information including names, addresses, and phone numbers. The application combines a clean, intuitive interface with robust backend database management.

**Course**: CMPE 102 (Programming Logic and Design)
**Project Type**: Group Project (Group 4)
**Academic Institution**: PUP (Polytechnic University of the Philippines)

---

## Features

## Core Functionality
- **Add Contact**: Create new contact entries with validation
- **View Contacts**: Display all stored contacts in a formatted list
- **Edit Contact**: Update existing contact information
- **Delete Contact**: Remove contacts from the database
- **Search Contacts**: Find contacts by name, address, or phone number

### Data Validation
- **Name Validation**: Accepts only letters and spaces, prevents empty entries
- **Phone Number Validation**:
    - Digits only (0-9)
    - Maximum 11 digits
    - Duplicate phone numbers are not allowed
    - Phone numbers must be unique across all contacts
- **Address Validation**: Ensures non-empty address fields
- **Capacity Management**: Maximum of 100 contact entries

### User Interface
- **Maroon-themed GUI**: Branded color scheme with maroon background (#800000) and gold accents (#FFD700)
- **Logo Support**: Displays a custom logo (picture_7.png) with automatic scaling
- **Responsive Design**: Button-based navigation for intuitive menu navigation
- **Dialog Boxes**: Input dialogs for adding/editing contacts and confirmation dialogs for actions

## Project Structure
```
G4-Project-PLD/
├─ main.py
├─ database.py
├─ app_database.db (auto-created)
├─ README.md 
├─ picture_logo/
│  ├─ picture_1.jpg
│  ├─ picture_2.jpg
│  ├─ picture_3.jpg
│  ├─ picture_4.png
│  ├─ picture_5.png
│  ├─ picture_6.png
│  ├─ picture_7.png (current logo)
│  └─ picture_8.png
├─ __pycache__/
└─ .gitignore 
```

---

## Technical Stack

- **Language**: Python 3.13.7
- **GUI Framework**: Tkinter (buitl-in with Python)
- **Database**: SQLite3
- **Database Format**: `.db` file
- **Operating System**: Cross-platforms (Windows, macOS, Linux)

---

## Installation & Setup

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually included with Python)

### Running the Application

1. **Navigate to the project directory**:
    ```bash
    cd "c:\Users\DENVER\Downloads\PUP\08_CMPE 102 (PLD)\G4-Project-PLD"
    ```

2. **Run the application**:
    ```bash
    python main.py
    ```

3. The application window will open with the home menu displaying available options.

---

##  Database Schema

The SQLite database contains a single `contacts` table with the following structure:

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY, AUTOINCREMENT | Unique contact identifier |
| first_name | TEXT | NOT NULL | Contact's first name |
| last_name | TEXT | NOT NULL | Contact's last name |
| address | TEXT | NOT NULL | Contact's physical address |
| phone_number | TEXT | NOT NULL, UNIQUE | Contact's phone number (must be unique) |

---

## File Descriptions

### `main.py`
Contains the `AddressBook` class implementing the Tkinter GUI:
- **Window Setup**: Creates the main application window with custom styling (600x400 pixels, maroon background)
- **Logo Handling**: Loads and scales the logo image (picture_7.png) from the picture_logo directory with dynamic scaling
- **Menu Navigation**: Provides navigation between different screens (Home, Add, Edit, Delete, View, Search)
- **Input Validation**: VAlidates user inputs for:
    - Names: Letters and spaces only
    - Phone numbers: 11-digit maximun, digits only, no duplicates
    - Addresses: Non-empty fields
- **CRUD Operations**: Implements add, view, edit, delete, and search functionality
- **UI Components**: Button-based interface with frames, labels, and styled buttons

### `database.py`
Handles all database operations using SQLite:
- `initialize_database()`: Creates the contacts table if it doesn't exist
- `add_contact(first_name, last_name, address, phone_number)`: Inserts a new contact into the database
- `get_all_contacts()`: Retrieves all contacts from the database and returns them as a list of dictionaries
- `update_contact(contact_id, first_name, last_name, address, phone_number)`: Updates an existing contact's information
- `delete_contact(contact_id)`: Removes a contact from the database by ID
- `phone_exists(phone_number, exclude_id=None)`: Checks if a phone number already exists (for validation); optional exclude_id parameter to ignore a specific contact during updates
- `get_connection()`: Establishes and returns a SQLite connection to app_database.db

---

## Known Issues & Limitations

### Current Issues
1. **Delete Functionality**:
    - Contact data is not displayed before deletion
    - Users must know the contact's designated ID number to remove entries
    - No preview of what will be deleted
    - **Recommendation**: Display list of contacts before deletion step

2. **Special Character Handling**: 
    - The application cannot handle special characters in names or addresses
    - Limited to alphabetic characters and spaces in names
    - May cause issues with internationl names or addresses with special punctuation
    - **Impact**: Users with non-ASCII names cannot be properly registered.

3. **Display Enhancement Needed**:
    - Better visual feedback when performing delete operations
    - No confimation preview showing which contact is being deleted

### Limitations
- **Maximum Contacts**: Fixed at 100 entries
- **Name Format**: Only support letters and spaces (no hyphens, apostrophes, diacritics)
- **Phone Number Format**: Limited to 11-digit maximum
- **No Email Field**: Contact table doesn't include email address storage
- **No categories**: All contacts are in a flat structure withoit grouping options
- **No Export/Import**: Cannot backup or import contacts from external files

---

## Future Improvements

1. **Enhanced Delete operation**:
    - Display contact list for selection before deletion
    - Show contact preview before confirming deletion
    - Undo functionality for recent deletions

2. **Special Character Support**:
    - Update validation regex to support international character sets
    - Allow hyphens, apostrophes, and Unicode characters in names
    - Support for accented characters

3. **Advanced Search**:
    - Filter by multiple criteria (name, phone, address)
    - Sort contacts by name, date added, or phone number
    - Case-insensitive searching

4. **Data Management**:
    - Export contacts to CSV or Excel format
    - Import contacts from extermal files
    - Backup database functionality
    - Data encryption for sensitive information

5. **Contact Organization**:
    - Categorize contacts (Work, Personal, Family, Friends, etc.)
    - Tags and labels for better organization
    - Favorites or starred contacts.

6. **Extended Contact fields**:
    - Email address field
    - Multiple phone numbers per contact
    - Date of birth for birthday reminders
    - Notes or additional comments

7. **User Experience Improvements**:
    - Dark mode theme option
    - Customizable color schemes
    - Keyboard shortcuts for common operations
    - Contact duplication detection

---

## Usage Guide

### Adding a Contact
1. Click **"Add Contact"** from home menu
2. Enter the following information:
    - **First Name**: Letters and spaces only (e.g., "John")
    - **Last Name**: Letters and spaces only (e.g., "Smith")
    - **Address**: Any text (e.g., "123 Main Street, Apartment 4B, New York, NY 10001")
    - **Phone NUmber**: Digits only, maximum 11 digits (e.g., "09876543210")
3. Phone number validation will ensure no duplicate numbers exist
4. Click **OK** to save the contact; **Cancel** to discard


### Viewing All Contacts
1. Click **"View Contacts"** to see a list of all saved contacts
2. Contacts are displayed in a scrollable window with:
    - Contact ID number
    - Full name (First + Last)
    - Address
    - Phone number
3. Click **Close** to return to the home menu

### Searching for Contacts
1. Clock **"Search Contacts"** form the home menu
2. Enter a name or phone number to search
3. Results will be displayed if matches are found
4. Returns all contacts with matching first name, last name, or phone number

### Editing a Contact
1. Click **"Edit Contact"** from the home menu
2. A dialog will prompt you to enter the contact ID to modify (you can view all contacts first to find the ID)
3. Modify any of the contact fields:
    - First name
    - Last name
    - Address
    - Phone number
4. Changes are saved immediately to the database upon confirmation

### Deleting a Contact
1. Click **"Delete Contact"** from the home menu
2. A dialog will prompt you to enter the contactID to remove
3. Note: You may need to view all contacts first to find the correct ID
4. Confirm the deletion when prompted
5. The contact will be permanently rmeoved from the database.

---

## Troubleshooting

### Application Won't Start
- Ensure Python 3.6+ is installed: `python -- version`
- Verify Tkinter is installed: `python -m tkinter` (should open a test window)
- Check that all files are in the correct directory

### Database Error
- Delete `app_database.db` to reset the database (all contacts will be lost)
- The database will not be automatically recreated on next run

### Logo Not Displaying
- Ensure `picture_logo/picture_&.png` exists in the correct directory
- If missing, copy and PNG file to that location and rename it to picture_7.png
- Application will still work without the logo, displaying text instead

### Validation Errors
- **Name validation failed**: Remove special characters, use only letters and spaces
- **Phone validation failed**: use only digits (0-9), maximum 11 digits
- **Duplicate phone**: The phone number already exists; check with "View Contacts"
---

## Project Participants

### Collaborators

- **Project Manager**: Sayasaya, Denver
- **Lead Engineer**: Orquez, Bernard Anthony
- **Senior Developer**: Cayabyab, Jonie
- **Junior Developer**: Domasig, Verdhenz Apple
- **Quality and Test Engineer**: Murillo, Marian Andrea

---

## Contact Information & Support

For questions or issues regarding this project, please contact the project participants listed above or refer to the project documentation.

---

## License

This poject is created for educational purposes as part of CMPE 102 at PUP (Polytechnic University of the Philippines).

---

**Last Updated**: January 10, 2026
**Version**: 1.0
**Status**: Finished
