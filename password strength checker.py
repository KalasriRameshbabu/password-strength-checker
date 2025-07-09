import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar, Style
import re

# Check password strength function
def check_strength(password):
    suggestions = []
    length = len(password)
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    digit = re.search(r"\d", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = 0
    if length >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if upper:
        score += 1
    else:
        suggestions.append("Add uppercase letters (A-Z).")

    if lower:
        score += 1
    else:
        suggestions.append("Add lowercase letters (a-z).")

    if digit:
        score += 1
    else:
        suggestions.append("Include numbers (0-9).")

    if special:
        score += 1
    else:
        suggestions.append("Use special characters (!@#...).")

    if score <= 2:
        return "❌ Weak", "red", suggestions, 20
    elif score == 3 or score == 4:
        return "⚠️ Moderate", "orange", suggestions, 60
    else:
        return "✅ Strong", "green", suggestions, 100

# Analyze password and update UI
def analyze_password():
    pwd = password_entry.get()
    if not pwd:
        messagebox.showerror("Input Error", "Please enter a password.")
        return

    result, color, tips, progress_value = check_strength(pwd)
    result_label.config(text=f"Strength: {result}", bg=color, fg="white")
    progress['value'] = progress_value

    suggestion_text.config(state='normal')
    suggestion_text.delete(1.0, tk.END)
    if tips:
        suggestion_text.insert(tk.END, "\n".join(tips))
    else:
        suggestion_text.insert(tk.END, "✅ Your password looks great!")
    suggestion_text.config(state='disabled')

# Toggle password visibility
def toggle_password():
    password_entry.config(show="" if show_var.get() else "*")

# Copy password to clipboard
def copy_password():
    pwd = password_entry.get()
    if pwd:
        window.clipboard_clear()
        window.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Animate the heading title text color
def animate_title():
    colors = ["#2c3e50", "#1abc9c", "#e74c3c", "#9b59b6"]
    title_label.config(fg=colors[animate_title.counter % len(colors)])
    animate_title.counter += 1
    window.after(500, animate_title)

animate_title.counter = 0

# Create main window
window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("650x550")
window.config(bg="#d1f2eb")  # Mint green background

# Style for progressbar
style = Style()
style.configure("TProgressbar", thickness=20)

# Animated title
title_label = tk.Label(window, text="🔐 Password Strength Checker",
                       font=("Courier", 22, "bold"), bg="#d1f2eb")
title_label.pack(pady=20)
animate_title()

# Password entry
tk.Label(window, text="Enter your password:", font=("Segoe UI", 14), bg="#d1f2eb").pack()
password_entry = tk.Entry(window, width=30, font=("Segoe UI", 14), show="*")
password_entry.pack(pady=10)

# Show password checkbox
show_var = tk.BooleanVar()
tk.Checkbutton(window, text="Show Password", variable=show_var, command=toggle_password,
               font=("Segoe UI", 11), bg="#d1f2eb").pack()

# Button to check strength
tk.Button(window, text="Check Strength", command=analyze_password,
          font=("Segoe UI", 12, "bold"), bg="#007bff", fg="white", width=20).pack(pady=10)

# Result display
result_label = tk.Label(window, text="", font=("Segoe UI", 16, "bold"), bg="#d1f2eb", width=30)
result_label.pack(pady=10)

# Progress bar
progress = Progressbar(window, orient='horizontal', length=400, mode='determinate')
progress.pack(pady=5)

# Suggestion heading
tk.Label(window, text="Suggestions to Improve:", font=("Segoe UI", 13), bg="#d1f2eb", fg="#333").pack(pady=(10, 5))

# Suggestion text area
suggestion_text = tk.Text(window, height=6, width=60, font=("Segoe UI", 11), wrap="word",
                          state='disabled', bg="#f0f5f5", relief="sunken", bd=2)
suggestion_text.pack(pady=10)

# Copy password button
tk.Button(window, text="Copy Password", command=copy_password,
          font=("Segoe UI", 11), bg="#20b2aa", fg="white").pack(pady=5)

# Footer
tk.Label(window, text="🔧 Developed by Kalasri", font=("Segoe UI", 10, "italic"),
         bg="#d1f2eb", fg="#555").pack(pady=10)

# Run the GUI
window.mainloop()
