import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import argparse
import sys
import time
import pyfiglet

def create_pyfiglet_banner(name):
    banner = pyfiglet.figlet_format(name, font="isometric1")
    print(banner)
def send_email(sender_email, receiver_email, subject, message, smtp_server, smtp_port):
    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the message to the MIME
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS encryption
        
        # Progress animation
        animation = "|/-\\"
        for i in range(20):
            sys.stdout.write("\r" + f"\033[32m[+] Sending Email {animation[i % len(animation)]}\033[0m ")
            sys.stdout.flush()
            time.sleep(0.1)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        # Close the connection
        server.quit()
        print("\n\033[32m[+] Email sent successfully!\033[0m")
    except Exception as e:
        print(f"\n\033[31m[-] Failed to send email. Error: {e}\033[0m")

if __name__ == "__main__":
    create_pyfiglet_banner("Mailox")
    parser = argparse.ArgumentParser(description='Send an email via SMTP')
    parser.add_argument('--sender-email', required=True, help='Sender email address')
    parser.add_argument('--receiver-email', required=True, help='Recipient email address')
    parser.add_argument('--subject', required=True, help='Email subject')
    parser.add_argument('--message', required=True, help='Email message')
    parser.add_argument('--smtp-server', required=True, help='SMTP server address')
    parser.add_argument('--smtp-port', required=True, type=int, help='SMTP server port')
    args = parser.parse_args()

    send_email(args.sender_email, args.receiver_email, args.subject, args.message, args.smtp_server, args.smtp_port)
