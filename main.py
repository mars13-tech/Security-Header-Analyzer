import requests
import tkinter as tk
from tkinter import ttk, messagebox

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy",
    "X-XSS-Protection"
]

def analyze_headers():
    url = entry.get().strip()
    
    if not url.startswith("http"):
        url = "https://" + url
    
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        result_text.delete("1.0", tk.END)

        result_text.insert(tk.END, f"Scanning: {url}\n\n")

        for header in SECURITY_HEADERS:
            if header in headers:
                result_text.insert(tk.END, f"{header}: ✅ Present\n", "present")
            else:
                result_text.insert(tk.END, f"{header}: ❌ Missing\n", "missing")

    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Unable to connect. Check the URL or internet.")

# GUI Setup
root = tk.Tk()
root.title("Security Header Analyzer")
root.geometry("600x450")
root.resizable(False, False)

title = tk.Label(root, text="Security Header Analyzer", font=("Arial", 16, "bold"))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

label = tk.Label(frame, text="Enter Website URL:")
label.grid(row=0, column=0, padx=5)

entry = tk.Entry(frame, width=40)
entry.grid(row=0, column=1, padx=5)

scan_button = tk.Button(root, text="Scan", command=analyze_headers, font=("Arial", 12), bg="#4CAF50", fg="white")
scan_button.pack(pady=10)

result_text = tk.Text(root, width=60, height=15, font=("Consolas", 11))
result_text.pack(pady=5)

result_text.tag_config("present", foreground="green")
result_text.tag_config("missing", foreground="red")

root.mainloop()
