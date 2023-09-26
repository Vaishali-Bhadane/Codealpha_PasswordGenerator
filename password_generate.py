




import random
import string
import tkinter as tk

def generate_password():
    all_characters = lower + upper + numbers + symbols
    length = length_entry.get()
    try:
        length = int(length)
        if length < 8:
            error_message.config(text="Password length must be at least 8 characters.", fg="red")
        else:
            error_message.config(text="")
            password_list = random.sample(all_characters, length)
            # Ensure at least one number in the password
            if not any(char.isdigit() for char in password_list):
                random_index = random.randint(0, length - 1)
                password_list[random_index] = random.choice(numbers)
            
            password = ''.join(password_list)
            password_label.config(text="Your password is: " + password, fg="black")
            password_label.config(font=("Helvetica", 14))  
    except ValueError:
        error_message.config(text="Invalid input. Please enter a valid number for the password length.", fg="red")

# main window
root = tk.Tk()
root.title("Password Generator")

# window dimensions 
root.geometry("300x250") 
root.configure(bg="#e0ffe0")  

# Character sets
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()."

# Label for instructions
instruction_label = tk.Label(root, text="Enter the length of the password (at least 8 characters):", bg="#e0ffe0")
instruction_label.pack(pady=10)

# Entry for password length
length_entry = tk.Entry(root)
length_entry.pack()

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Label to display the generated password
password_label = tk.Label(root, text="", fg="black", bg="#e0ffe0")
password_label.pack()

# Label to display error messages
error_message = tk.Label(root, text="", fg="red", bg="#e0ffe0")
error_message.pack()

# Run the GUI
root.mainloop()
