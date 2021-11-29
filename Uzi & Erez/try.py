import smtplib


EMAIL_ADRESS = "Eyalbh8@gmail.com"
EMAIL_PASSWORD = "hanchibanchi"

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
    
    subject = "Medicine allert"
    body = "Expired medicine"

    msg = f"Subject: {subject}\n\n{body}"
    
    smtp.sendmail(EMAIL_ADRESS, EMAIL_ADRESS, msg)