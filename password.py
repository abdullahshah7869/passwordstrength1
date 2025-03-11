import tkinter as tk
from tkinter import ttk
import re

# Function to check password strength
def check_password_strength(event=None):
    password = password_entry.get()

    # Password strength criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[@$!%*?&]', password))

    # Calculate strength
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    # Update the progress bar and strength label based on criteria met
    if criteria_met == 5:
        strength_label.config(text="Strong", fg="green")
        strength_bar["value"] = 100
        strength_bar.config(style="strong.Horizontal.TProgressbar")
    elif criteria_met == 4:
        strength_label.config(text="Medium", fg="orange")
        strength_bar["value"] = 75
        strength_bar.config(style="medium.Horizontal.TProgressbar")
    elif criteria_met == 3:
        strength_label.config(text="Weak", fg="red")
        strength_bar["value"] = 50
        strength_bar.config(style="weak.Horizontal.TProgressbar")
    else:
        strength_label.config(text="Very Weak", fg="red")
        strength_bar["value"] = 25
        strength_bar.config(style="very_weak.Horizontal.TProgressbar")
    
    # Update the guidelines visibility
    if len(password) < 8:
        length_label.config(fg="red")
    else:
        length_label.config(fg="green")
    
    if not uppercase_criteria:
        uppercase_label.config(fg="red")
    else:
        uppercase_label.config(fg="green")
    
    if not lowercase_criteria:
        lowercase_label.config(fg="red")
    else:
        lowercase_label.config(fg="green")
    
    if not number_criteria:
        number_label.config(fg="red")
    else:
        number_label.config(fg="green")
    
    if not special_char_criteria:
        special_char_label.config(fg="red")
    else:
        special_char_label.config(fg="green")

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("450x400")
root.config(bg="#f5f5f5")

# Create a style for the progress bar
style = ttk.Style(root)
style.configure("strong.Horizontal.TProgressbar", thickness=30, background="green")
style.configure("medium.Horizontal.TProgressbar", thickness=30, background="orange")
style.configure("weak.Horizontal.TProgressbar", thickness=30, background="red")
style.configure("very_weak.Horizontal.TProgressbar", thickness=30, background="lightgray")

# Title label
title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333")
title_label.pack(pady=20)

# Password input field
password_label = tk.Label(root, text="Enter your password:", font=("Arial", 12), bg="#f5f5f5", fg="#333")
password_label.pack(pady=5)

password_entry = tk.Entry(root, font=("Arial", 14), width=35, show="*", relief="solid", bd=2)
password_entry.pack(pady=10)

# Bind the event to the password input for real-time feedback
password_entry.bind("<KeyRelease>", check_password_strength)

# Strength label
strength_label = tk.Label(root, text="Enter a password to check strength", font=("Arial", 12), bg="#f5f5f5", fg="#333")
strength_label.pack(pady=5)

# Progress bar for strength visualization
strength_bar = ttk.Progressbar(root, length=300, mode="determinate", maximum=100, value=0)
strength_bar.pack(pady=15)

# Password guidelines (helpful for users)
guidelines_frame = tk.Frame(root, bg="#f5f5f5")
guidelines_frame.pack(pady=10)

length_label = tk.Label(guidelines_frame, text="• At least 8 characters", font=("Arial", 10), bg="#f5f5f5", fg="gray")
length_label.grid(row=0, column=0, sticky="w")

uppercase_label = tk.Label(guidelines_frame, text="• At least one uppercase letter", font=("Arial", 10), bg="#f5f5f5", fg="gray")
uppercase_label.grid(row=1, column=0, sticky="w")

lowercase_label = tk.Label(guidelines_frame, text="• At least one lowercase letter", font=("Arial", 10), bg="#f5f5f5", fg="gray")
lowercase_label.grid(row=2, column=0, sticky="w")

number_label = tk.Label(guidelines_frame, text="• At least one number", font=("Arial", 10), bg="#f5f5f5", fg="gray")
number_label.grid(row=3, column=0, sticky="w")

special_char_label = tk.Label(guidelines_frame, text="• At least one special character (@$!%*?&)", font=("Arial", 10), bg="#f5f5f5", fg="gray")
special_char_label.grid(row=4, column=0, sticky="w")

# Reset button to clear all inputs
def reset():
    password_entry.delete(0, tk.END)
    strength_label.config(text="Enter a password to check strength", fg="#333")
    strength_bar["value"] = 0
    strength_bar.config(style="very_weak.Horizontal.TProgressbar")
    length_label.config(fg="gray")
    uppercase_label.config(fg="gray")
    lowercase_label.config(fg="gray")
    number_label.config(fg="gray")
    special_char_label.config(fg="gray")

reset_button = tk.Button(root, text="Reset", font=("Arial", 12), command=reset, bg="lightblue", relief="solid", bd=1)
reset_button.pack(pady=10)

# Run the app
root.mainloop()
