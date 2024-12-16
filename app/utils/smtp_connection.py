import smtplib
from email.mime.text import MIMEText

def send_email(to_email: str, subject: str, body: str):
    smtp_server = "sandbox.smtp.mailtrap.io"
    smtp_port = 2525
    smtp_username = "your_username"
    smtp_password = "your_password"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "no-reply@example.com"
    msg["To"] = to_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
