import tkinter as tk
from time import strftime

# Create window
root = tk.Tk()
root.title("Digital Clock with Date")
root.geometry("600x300")
root.resizable(False, False)

# Function to update clock
def update_clock():
    # Get current time
    current_time = strftime("%I:%M:%S %p")

    # Get current date
    current_date = strftime("%A, %d %B %Y")

    # Update labels
    time_label.config(text=current_time)
    date_label.config(text=current_date)

    # Update every 1 second
    root.after(1000, update_clock)


# Time label
time_label = tk.Label(
    root,
    font=("Arial", 50, "bold"),
    bg="black",
    fg="white"
)
time_label.pack(fill="both", expand=True)


# Date label
date_label = tk.Label(
    root,
    font=("Arial", 25),
    bg="black",
    fg="white"
)
date_label.pack(fill="both", expand=True)


# Start clock
update_clock()

# Run window
root.mainloop()