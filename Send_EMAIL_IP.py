import smtplib
import socket
from email.mime.text import MIMEText

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"  # Change based on your email provider
SMTP_PORT = 587
EMAIL_SENDER = "night981gogonereal@gmail.com"
EMAIL_PASSWORD = "682040googleverificationcode"
EMAIL_RECEIVER = "viveklpclko@gmail.com"

def get_ip_address():
    """Returns the current system's IP address"""
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        return f"Error retrieving IP: {e}"

def send_email(ip_address):
    """Sends an email containing the IP address"""
    subject = "Machine IP Address"
    body = f"The current machine's IP address is: {ip_address}"

    msg = MIMEText(body)
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = subject

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    ip = get_ip_address()
    send_email(ip)
