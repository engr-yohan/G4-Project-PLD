import sqlite3
import os

database_name = "app_database.db"

def get_connection():
    return sqlite3.connect(database_name)

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS contacts(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   first_name TEXT NOT NULL,
                   last_name TEXT NOT NULL,
                   address TEXT NOT NULL,
                   phone_number TEXT NOT NULL
                   )
                   ''')
    
    conn.commit()
    conn.close()

def add_contact(first_name, last_name, address, phone_number):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
                   INSERT INTO contacts (first_name, last_name, address, phone_number)
                   VALUES (?, ?, ?, ?)
                   ''', (first_name.title(), last_name.title(), address.title(), phone_number))
    
    conn.commit()
    conn.close()

def phone_exists(phone_number, exclude_id=None):
    conn = get_connection()
    cursor = conn.cursor()

    if exclude_id is None:
        cursor.execute('SELECT 1 FROM contacts WHERE phone_number = ? LIMIT 1', (phone_number,))
    else:
        cursor.execute('SELECT 1 FROM contacts WHERE phone_number = ? AND id != ? LIMIT 1', (phone_number, exclude_id))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists

def get_all_contacts():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT id, first_name, last_name, address, phone_number FROM contacts')
    rows = cursor.fetchall()
    conn.close()

    # Convert to list of dictionaries for compatibility
    contacts = []
    for row in rows:
        contacts.append({
            "id": row[0],
            "first": (row[1] or "").title(),
            "last": (row[2] or "").title(),
            "address": (row[3] or "").title(),
            "number": row[4]
        })
    return contacts

def update_contact(contact_id, first_name, last_name, address, phone_number):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
                   UPDATE contacts
                   SET first_name = ?, last_name = ?, address = ?, phone_number = ?
                   WHERE id = ?
                   ''', (first_name.title(), last_name.title(), address.title(), phone_number, contact_id))
    
    conn.commit()
    conn.close()

def delete_contact(contact_id):
    conn = get_connection()
    
    cursor = conn.cursor()
    cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))

    conn.commit()
    conn.close()
