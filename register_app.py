import sqlite3
import hashlib


db = sqlite3.connect('registerapp.db')
sql = db.cursor()


sql.execute('''CREATE TABLE IF NOT EXISTS registerapp (
             id INTEGER PRIMARY KEY,
             username TEXT NOT NULL UNIQUE,
             first_name VARCHAR(55),
             last_name VARCHAR(55),
             email TEXT NOT NULL UNIQUE,
             password TEXT NOT NULL
             )''')


def register_user():
    while True:
        username = input("Username: ")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        password = input("Password: ")
        confirm_password = input("Confirm Password: ")

        if password != confirm_password:
            print("Passwords do not match. Please try again.")
            continue

       
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        
        sql.execute("SELECT * FROM registerapp WHERE email=?", (email,))
        existing_user = sql.fetchone()
        if existing_user:
            print("This email is already registered. Please use a different email.")
            continue

        
        sql.execute("INSERT INTO registerapp (username, first_name, last_name, email, password) VALUES (?, ?, ?, ?, ?)",
                  (username, first_name, last_name, email, hashed_password))
        db.commit()
        print("Registration successful!")
        break


register_user()


db.close()
