import tkinter as tk

from tkinter import messagebox

import time



class DangerousWritingApp:

    def __init__(self, root):

        self.root = root

        self.root.title("The Most Dangerous Writing App")

        self.root.geometry("600x400")



        # Text area

        self.text = tk.Text(root, wrap="word", font=("Arial", 14))

        self.text.pack(expand=True, fill="both", padx=10, pady=10)



        # Timer label

        self.timer_label = tk.Label(root, text="Keep typing...", font=("Arial", 12), fg="red")

        self.timer_label.pack()



        # Variables

        self.last_key_time = time.time()

        self.time_limit = 5  # seconds



        # Bind keypress

        self.text.bind("<Key>", self.reset_timer)



        # Start checking

        self.check_idle_time()



    def reset_timer(self, event=None):

        """Reset the timer whenever user types."""

        self.last_key_time = time.time()

        self.timer_label.config(text="Keep typing...")



    def check_idle_time(self):

        """Check if user has been idle too long."""

        idle_time = time.time() - self.last_key_time

        if idle_time > self.time_limit:

            self.text.delete("1.0", tk.END)

            self.timer_label.config(text="⏰ You stopped! All text deleted!")

            messagebox.showwarning("Time's Up!", "You stopped typing. Everything has been deleted!")

            self.last_key_time = time.time()  # reset so it doesn't loop-delete



        # Schedule check every 1 second

        self.root.after(1000, self.check_idle_time)





if __name__ == "__main__":

    root = tk.Tk()

    app = DangerousWritingApp(root)

    root.mainloop()

