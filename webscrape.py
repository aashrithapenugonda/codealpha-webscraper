import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import scrolledtext

def scrape_and_display():
    url = url_entry.get()
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        soup = BeautifulSoup(response.content, 'html.parser')
        titles = soup.find_all('h2')

        result_text.delete(1.0, tk.END)  # Clear previous content
        if titles:
            for title in titles:
                result_text.insert(tk.END, title.get_text() + "\n")
        else:
            result_text.insert(tk.END, "No h2 titles found on this page.\n")

    except requests.exceptions.RequestException as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {e}\n")
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"An unexpected error occurred: {e}\n")

# GUI setup
window = tk.Tk()
window.title("Web Scraper")

url_label = tk.Label(window, text="Enter URL:")
url_label.pack(pady=5)

url_entry = tk.Entry(window, width=50)
url_entry.pack(pady=5)

scrape_button = tk.Button(window, text="Scrape Titles", command=scrape_and_display)
scrape_button.pack(pady=10)

result_text = scrolledtext.ScrolledText(window, width=60, height=20)
result_text.pack(pady=10)

window.mainloop()