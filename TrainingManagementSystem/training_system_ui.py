import tkinter as tk
from tkinter import ttk, messagebox

def create_login(parent):
    frame = tk.Toplevel(parent)
    frame.title("1. Login Screen")
    frame.geometry("350x300")
    frame.configure(bg="#f0f4f8")

    tk.Label(frame, text="Training Management System", font=("Arial", 14, "bold"), bg="#f0f4f8").pack(pady=15)
    tk.Label(frame, text="Sign in to your account", bg="#f0f4f8").pack()

    tk.Label(frame, text="Username", bg="#f0f4f8").pack(pady=(15,0))
    tk.Entry(frame, width=25).pack()

    tk.Label(frame, text="Password", bg="#f0f4f8").pack(pady=(10,0))
    tk.Entry(frame, width=25, show="*").pack()

    tk.Button(frame, text="Login", bg="#2563EB", fg="white", width=15).pack(pady=20)


def create_learner_dashboard(parent):
    frame = tk.Toplevel(parent)
    frame.title("2. Learner Dashboard")
    frame.geometry("350x320")
    frame.configure(bg="#f0f4f8")

    tk.Label(frame, text="Learner Dashboard", font=("Arial", 14, "bold"), bg="#f0f4f8").pack(pady=10)
    tk.Label(frame, text="Welcome, John Doe!", bg="#f0f4f8").pack()

    tk.Button(frame, text="Home", width=20).pack(pady=5)
    tk.Button(frame, text="Register Course", width=20).pack(pady=5)
    tk.Button(frame, text="My Courses", width=20).pack(pady=5)
    tk.Button(frame, text="Support Ticket", width=20).pack(pady=5)
    tk.Button(frame, text="Logout", width=20).pack(pady=5)


def create_course_registration(parent):
    frame = tk.Toplevel(parent)
    frame.title("3. Course Registration")
    frame.geometry("350x300")
    frame.configure(bg="#f0f4f8")

    tk.Label(frame, text="Register for Course", font=("Arial", 14, "bold"), bg="#f0f4f8").pack(pady=15)
    tk.Label(frame, text="Course Code: AI101", bg="#f0f4f8").pack()
    tk.Label(frame, text="Course Name: Artificial Intelligence", bg="#f0f4f8").pack()
    tk.Label(frame, text="Available Spaces: 8", bg="#f0f4f8").pack(pady=10)

    tk.Button(frame, text="Register", bg="#22C55E", fg="white", width=12).pack(pady=5)
    tk.Button(frame, text="Cancel", width=12).pack(pady=5)


def create_support_ticket(parent):
    frame = tk.Toplevel(parent)
    frame.title("5. Support Ticket")
    frame.geometry("350x320")
    frame.configure(bg="#f0f4f8")

    tk.Label(frame, text="Create Support Ticket", font=("Arial", 14, "bold"), bg="#f0f4f8").pack(pady=10)
    tk.Label(frame, text="Problem:", bg="#f0f4f8").pack()
    tk.Text(frame, width=30, height=4).pack(pady=5)
    tk.Button(frame, text="Submit Ticket", bg="#2563EB", fg="white", width=15).pack(pady=10)
    tk.Label(frame, text="Status: Open", bg="#f0f4f8").pack()


def create_course_management(parent):
    frame = tk.Toplevel(parent)
    frame.title("4. Course Management (Admin)")
    frame.geometry("450x300")
    frame.configure(bg="#f0f4f8")

    tk.Label(frame, text="Manage Courses", font=("Arial", 14, "bold"), bg="#f0f4f8").pack(pady=10)

    columns = ("Code", "Name", "Capacity")
    tree = ttk.Treeview(frame, columns=columns, show="headings", height=5)
    tree.heading("Code", text="Course Code")
    tree.heading("Name", text="Course Name")
    tree.heading("Capacity", text="Capacity")

    tree.column("Code", width=100)
    tree.column("Name", width=150)
    tree.column("Capacity", width=80)

    tree.insert("", "end", values=("PY101", "Python Programming", 20))
    tree.insert("", "end", values=("DB101", "Database Systems", 30))
    tree.insert("", "end", values=("AI101", "Artificial Intelligence", 20))
    tree.pack(pady=10)

    tk.Button(frame, text="Add", width=10).pack(side="left", padx=15)
    tk.Button(frame, text="Edit", width=10).pack(side="left", padx=5)
    tk.Button(frame, text="Delete", width=10).pack(side="left", padx=5)


def create_reports(parent):
    frame = tk.Toplevel(parent)
    frame.title("6. Reports (Admin)")
    frame.geometry("350x300")
    frame.configure(bg="#f0f4f8")

    tk.Label(frame, text="Reports Overview", font=("Arial", 14, "bold"), bg="#f0f4f8").pack(pady=15)
    tk.Label(frame, text="Total Learners: 500", bg="#f0f4f8").pack(pady=3)
    tk.Label(frame, text="Total Courses: 20", bg="#f0f4f8").pack(pady=3)
    tk.Label(frame, text="Total Registrations: 450", bg="#f0f4f8").pack(pady=3)
    tk.Label(frame, text="Successful: 400", bg="#f0f4f8").pack(pady=3)
    tk.Label(frame, text="Unsuccessful: 50", bg="#f0f4f8").pack(pady=3)

    tk.Button(frame, text="View Report", bg="#2563EB", fg="white", width=15).pack(pady=15)


# ========== MAIN WINDOW ==========
root = tk.Tk()
root.title("Training Management System - All Screens")
root.geometry("300x200")
root.configure(bg="#e0e7ff")

tk.Label(root, text="All Screens Launcher", font=("Arial", 14, "bold"), bg="#e0e7ff").pack(pady=20)
tk.Label(root, text="All windows will open now", bg="#e0e7ff").pack()

# Open all screens
create_login(root)
create_learner_dashboard(root)
create_course_registration(root)
create_support_ticket(root)
create_course_management(root)
create_reports(root)

root.mainloop()