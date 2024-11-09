import tkinter as tk
from tkinter import messagebox
import psycopg2

config = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='qwerty',
    client_encoding='UTF8'
)

def check_login():
    username = entry_username.get()
    password = entry_password.get()
    
    with config.cursor() as cursor:
        sql = 'SELECT * FROM users WHERE username = %s;'
        cursor.execute(sql, (username,))
        user = cursor.fetchone()

    if user and user[2] == password:
        messagebox.showinfo("Welcome", f"Welcome, {username}!")
    elif user:
        messagebox.showerror("Error", "Incorrect password!")
    else:
        messagebox.showerror("Error", "Username not found!")

def add_user():
    new_username = entry_new_username.get()
    new_password = entry_new_password.get()

    with config.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE username = %s;", (new_username,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Username already exists!")
            return
        
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s);", 
                       (new_username, new_password))
        config.commit()
        messagebox.showinfo("Success", "User added successfully!")

def change_password():
    username = entry_username.get()
    new_password = entry_password.get()

    with config.cursor() as cursor:
        cursor.execute("UPDATE users SET password = %s WHERE username = %s;", 
                       (new_password, username))
        config.commit()
        messagebox.showinfo("Success", "Password changed successfully!")

def delete_user():
    username = entry_username.get()

    with config.cursor() as cursor:
        cursor.execute("DELETE FROM users WHERE username = %s;", (username,))
        config.commit()
        messagebox.showinfo("Success", "User deleted successfully!")

root = tk.Tk()
root.title("User Management System")

label_login = tk.Label(root, text="Login", font=("Arial", 14))
label_login.pack(pady=10)

label_username = tk.Label(root, text="Username:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

login_button = tk.Button(root, text="Login", command=check_login)
login_button.pack(pady=5)

label_new_user = tk.Label(root, text="Add New User", font=("Arial", 14))
label_new_user.pack(pady=10)

label_new_username = tk.Label(root, text="New Username:")
label_new_username.pack()
entry_new_username = tk.Entry(root)
entry_new_username.pack()

label_new_password = tk.Label(root, text="New Password:")
label_new_password.pack()
entry_new_password = tk.Entry(root, show="*")
entry_new_password.pack()

add_user_button = tk.Button(root, text="Add User", command=add_user)
add_user_button.pack(pady=5)

change_password_button = tk.Button(root, text="Change Password", command=change_password)
change_password_button.pack(pady=5)

delete_user_button = tk.Button(root, text="Delete User", command=delete_user)
delete_user_button.pack(pady=5)

root.mainloop()

config.close()