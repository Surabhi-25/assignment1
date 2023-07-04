import tkinter as tk
import webbrowser as wb

root = tk.Tk()

# Entry widget
entry = tk.Entry(root, font=("Times New Roman", 30), width=30)
entry.grid(row=0, column=0)

l1 = tk.Label(root, font=("Times New Roman", 20))
l1.grid(row=1, column=0)
def display():
    search = entry.get()
    print(search)
    if search:
        l1.config(text="Navigating to PINTEREST")
        
        wb.open(f"https://in.pinterest.com/search/pins/?q={search}")
    else:
        print("Please enter something")


search_button = tk.Button(root, text="Search", font=("Times New Roman", 20),bg="#b4faeb", activebackground="#90fca7", command=display)
search_button.grid(row=3, column=0)

close_button = tk.Button(root, text="Close", font=("Times New Roman", 20),bg="#fcba03", activebackground="#cc8d7e", command=root.destroy)
close_button.grid(row=4, column=0)

root.mainloop()

