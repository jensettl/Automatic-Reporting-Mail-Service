# Functions for building and sending emails

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import config

SMTP_PORT = 587  # Standard port for email submission
SMTP_SERVER = "smtp.gmail.com"  # Google SMTP server
PWD = config.EMAIL_PWD  # Password for email account

def sendEmail(email_from, email_to, subject, body):
    msg = MIMEMultipart()  # Create a multipart message
    msg["From"] = email_from  # Add sender email to message
    msg["To"] = email_to  # Add receiver email to message
    msg["Subject"] = subject  # Add subject to message

    # Add body to email
    msg.attach(MIMEText(body, "plain"))

    text = msg.as_string()

    try:
        print("Connecting to server...")
        TIE_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        TIE_server.starttls()
        TIE_server.login(email_from, PWD)
        print("Connected to server")

        print()
        print(f"Sending email to - {email_to}")
        TIE_server.sendmail(email_from, email_to, text)
        print(f"Email successfully sent to {email_to}")
        print()

    except Exception as e:
        print(f"❌ An error occurred: {e}")

    finally:
        TIE_server.quit()
        print("Connection closed...")