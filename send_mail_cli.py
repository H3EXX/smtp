import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import argparse

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
        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        # Close the connection
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

def print_banner():
    banner = """
    _____ _ _     _       _     _             
  / ____(_) |   | |     | |   | |            
 | |  __ _| |__ | |_ ___| |__ | |_ ___  _ __ 
 | | |_ | | '_ \| __/ _ \ '_ \| __/ _ \| '__|
 | |__| | | | | | ||  __/ |_) | || (_) | |   
  \_____|_|_| |_|\__\___|_.__/ \__\___/|_|   
                                             
    """
    print(banner)

if __name__ == "__main__":
    print_banner()
    
    parser = argparse.ArgumentParser(description='Send an email via SMTP')
    parser.add_argument('--sender-email', required=True, help='Sender email address')
    parser.add_argument('--receiver-email', required=True, help='Recipient email address')
    parser.add_argument('--subject', required=True, help='Email subject')
    parser.add_argument('--message', required=True, help='Email message')
    parser.add_argument('--smtp-server', required=True, help='SMTP server address')
    parser.add_argument('--smtp-port', required=True, type=int, help='SMTP server port')
    args = parser.parse_args()

    send_email(args.sender_email, args.receiver_email, args.subject, args.message, args.smtp_server, args.smtp_port)
