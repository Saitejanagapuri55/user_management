import smtplib
from email.mime.text import MIMEText
import os

def send_email(to_email, subject, body):
    smtp_server = os.getenv("smtp_server")
    smtp_port = int(os.getenv("smtp_port"))
    smtp_username = os.getenv("smtp_username")
    smtp_password = os.getenv("smtp_password")

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = smtp_username
    msg["To"] = to_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
