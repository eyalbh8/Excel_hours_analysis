import tkinter as tk
import smtplib

def Print_min(Medicine_name):
    window = tk.Tk()
    window.title("לשים לב")

    Result_label = tk.Label(window, text = "הגיע למינימום", font=("calibre",18, "bold"))
    Result_label.grid(row=0,column=1)

    label = tk.Label(window, text = Medicine_name, font=("calibre",18, "bold"))
    label.grid(row=2,column=0)

    window.mainloop()
    Medicine_allert = f"Reached the minimum: {Medicine_name}"
    Email_massage(Medicine_allert)

def Print_Expired(Medicine_name):
    window = tk.Tk()
    window.title("לשים לב")

    Result_label = tk.Label(window, text = "פג תוקף", font=("calibre",18, "bold"))
    Result_label.grid(row=0,column=1)

    label = tk.Label(window, text = Medicine_name, font=("calibre",18, "bold"))
    label.grid(row=2,column=0)

    window.mainloop()
    
    Medicine_allert = f"Medicine expired: {Medicine_name}"
    Email_massage(Medicine_allert)

def Print_Executed():
    window = tk.Tk()
    window.title("בוצע")

    Executed_label = tk.Label(window, text = "בוצע", font=("calibre",18, "bold"))
    Executed_label.grid(row=0,column=1)

    window.mainloop()


def Email_massage(Medicine_allert):
    EMAIL_ADRESS = "ttinbareyaltt@gmail.com"
    EMAIL_PASSWORD = "takornak"

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
    
        subject = "Medicine allert"
        body = Medicine_allert

        msg = f"Subject: {subject}\n\n{body}"
    
        smtp.sendmail(EMAIL_ADRESS, EMAIL_ADRESS, msg)
