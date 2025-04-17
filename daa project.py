import tkinter as tk
from tkinter import messagebox

def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    selected_activities = []
    last_end_time = 0
    for start, end in activities:
        if start >= last_end_time:
            selected_activities.append((start, end))
            last_end_time = end
    return selected_activities

class ActivitySelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Activity Selector")
        self.activities = []

        # Labels and entries
        tk.Label(root, text="Start Time:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(root, text="End Time:").grid(row=0, column=1, padx=5, pady=5)
        self.start_entry = tk.Entry(root, width=10)
        self.end_entry = tk.Entry(root, width=10)
        self.start_entry.grid(row=1, column=0)
        self.end_entry.grid(row=1, column=1)

        # Buttons
        tk.Button(root, text="Add Activity", command=self.add_activity).grid(row=1, column=2, padx=5)
        tk.Button(root, text="Select Activities", command=self.select_activities).grid(row=2, column=0, pady=10)
        tk.Button(root, text="Reset", command=self.reset).grid(row=2, column=1, pady=10)

        # Display areas
        self.activity_listbox = tk.Listbox(root, width=30, height=10)
        self.activity_listbox.grid(row=3, column=0, columnspan=3, padx=10, pady=5)
        self.result_listbox = tk.Listbox(root, width=30, height=10)
        self.result_listbox.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

    def add_activity(self):
        try:
            start = int(self.start_entry.get())
            end = int(self.end_entry.get())
            if start >= end:
                messagebox.showwarning("Invalid Input", "Start time must be less than end time.")
                return
            self.activities.append((start, end))
            self.activity_listbox.insert(tk.END, f"({start}, {end})")
            self.start_entry.delete(0, tk.END)
            self.end_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid integers.")

    def select_activities(self):
        if not self.activities:
            messagebox.showinfo("No Activities", "Add at least one activity first.")
            return
        selected = activity_selection(self.activities)
        self.result_listbox.delete(0, tk.END)
        self.result_listbox.insert(tk.END, "Selected Activities:")
        for start, end in selected:
            self.result_listbox.insert(tk.END, f"({start}, {end})")

    def reset(self):
        self.activities.clear()
        self.activity_listbox.delete(0, tk.END)
        self.result_listbox.delete(0, tk.END)
        self.start_entry.delete(0, tk.END)
        self.end_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ActivitySelectorApp(root)
    root.mainloop()
