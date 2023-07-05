

import tkinter as tk
import webbrowser

def open_faq_page():
    chosen_site = site_var.get()
    chosen_source= source_var.get()

    with open("chosen_options.txt", "a") as file:
        file.write("Chosen site is: " + chosen_site + "\n" +"Discovery Source: " + chosen_source +  "\n\n")
    

    site_faq_urls = {
        "Udemy": "https://www.udemy.com/faq/",
        "Duolingo": "https://www.duolingo.com/help",
        "Coursera": "https://learner.coursera.help/hc/en-us"
    }

 
    if chosen_site in site_faq_urls:
        webbrowser.open(site_faq_urls[chosen_site])
    else:
        print("Choose options from both fields.")


window = tk.Tk()


site_var = tk.StringVar(value="Udemy")
source_var=tk.StringVar(value="Google Ads")

site_label = tk.Label(window, text="Choose a site:")
site_label.pack()

site_option_1 = tk.Radiobutton(window, text="Udemy", variable=site_var, value="Udemy")
site_option_1.pack()

site_option_2 = tk.Radiobutton(window, text="Duolingo", variable=site_var, value="Duolingo")
site_option_2.pack()

site_option_3 = tk.Radiobutton(window, text="Coursera", variable=site_var, value="Coursera")
site_option_3.pack()


source_label = tk.Label(window, text="Where did you discover this site?")
source_label.pack()

source_option_1 = tk.Radiobutton(window, text="Google Ads", variable=source_var, value=" Google Ads")
source_option_1.pack()

source_option_2 = tk.Radiobutton(window, text="Instagram Ads", variable=source_var, value="Instagram Ads")
source_option_2.pack()

source_option_3 = tk.Radiobutton(window, text="Youtube Ads", variable=source_var, value="Youtube Ads")
source_option_3.pack()


submit_button = tk.Button(window, text="Submit", command=open_faq_page)
submit_button.pack()


window.mainloop()







