import tkinter as tk
import calendar
from tkinter import ttk

def show_calendar():
    year = int(year_entry.get())
    month = int(month_combobox.get())
    
    cal_text = calendar.month(year, month)
    calendar_output.delete('1.0', tk.END)
    calendar_output.insert(tk.END, cal_text)

# Create main window
root = tk.Tk()
root.title("Calendar Viewer")
root.geometry("400x400")

# Title Label
title_label = tk.Label(root, text="Calendar Viewer", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Year Entry
year_label = tk.Label(root, text="Enter Year:")
year_label.pack()
year_entry = tk.Entry(root)
year_entry.pack(pady=5)

# Month Selection
month_label = tk.Label(root, text="Select Month:")
month_label.pack()
month_combobox = ttk.Combobox(root, values=list(range(1, 13)))
month_combobox.pack(pady=5)

# Show Button
show_button = tk.Button(root, text="Show Calendar", command=show_calendar)
show_button.pack(pady=10)

# Calendar Output
calendar_output = tk.Text(root, width=40, height=10, font=("Courier", 10))
calendar_output.pack()

# Run the application
root.mainloop()