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
        cursor.execute("SELECT * FROM users WHERE username = %s;", (username,))
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
root.configure(bg="#2A3663")

bg_color = "#2A3663"
text_color = "#B59F78"
button_color = "#4A5B7A"
font_main = ("Arial", 12)
font_title = ("Arial", 14, "bold")

title_label = tk.Label(root, text="User Management System", font=font_title, bg=bg_color, fg=text_color)
title_label.pack(pady=10)

login_frame = tk.Frame(root, bg=bg_color)
login_frame.pack(pady=10, padx=20, fill="x")

label_login = tk.Label(login_frame, text="Login", font=font_main, bg=bg_color, fg=text_color)
label_login.pack(pady=5)

label_username = tk.Label(login_frame, text="Username:", bg=bg_color, fg=text_color)
label_username.pack(anchor="w")
entry_username = tk.Entry(login_frame, width=30)
entry_username.pack()

label_password = tk.Label(login_frame, text="Password:", bg=bg_color, fg=text_color)
label_password.pack(anchor="w")
entry_password = tk.Entry(login_frame, show="*", width=30)
entry_password.pack()

login_button = tk.Button(login_frame, text="Login", command=check_login, bg=button_color, fg=text_color)
login_button.pack(pady=10)

add_user_frame = tk.Frame(root, bg=bg_color)
add_user_frame.pack(pady=10, padx=20, fill="x")

label_new_user = tk.Label(add_user_frame, text="Add New User", font=font_main, bg=bg_color, fg=text_color)
label_new_user.pack(pady=5)

label_new_username = tk.Label(add_user_frame, text="New Username:", bg=bg_color, fg=text_color)
label_new_username.pack(anchor="w")
entry_new_username = tk.Entry(add_user_frame, width=30)
entry_new_username.pack()

label_new_password = tk.Label(add_user_frame, text="New Password:", bg=bg_color, fg=text_color)
label_new_password.pack(anchor="w")
entry_new_password = tk.Entry(add_user_frame, show="*", width=30)
entry_new_password.pack()

add_user_button = tk.Button(add_user_frame, text="Add User", command=add_user, bg=button_color, fg=text_color)
add_user_button.pack(pady=10)

change_password_button = tk.Button(root, text="Change Password", command=change_password, bg=button_color, fg=text_color)
change_password_button.pack(pady=10)

delete_user_button = tk.Button(root, text="Delete User", command=delete_user, bg=button_color, fg=text_color)
delete_user_button.pack(pady=10)

root.mainloop()

config.close()