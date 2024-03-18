import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import messagebox

def send_email():
    sender_email = sender_email_entry.get()
    receiver_email = receiver_email_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", "end")
    smtp_server = smtp_server_entry.get()
    smtp_port = int(smtp_port_entry.get())

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
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email. Error: {e}")

# Create the GUI
root = tk.Tk()
root.title("Email Sending Tool")

sender_email_label = tk.Label(root, text="Sender Email:")
sender_email_label.grid(row=0, column=0)
sender_email_entry = tk.Entry(root)
sender_email_entry.grid(row=0, column=1)

receiver_email_label = tk.Label(root, text="Receiver Email:")
receiver_email_label.grid(row=1, column=0)
receiver_email_entry = tk.Entry(root)
receiver_email_entry.grid(row=1, column=1)

subject_label = tk.Label(root, text="Subject:")
subject_label.grid(row=2, column=0)
subject_entry = tk.Entry(root)
subject_entry.grid(row=2, column=1)

message_label = tk.Label(root, text="Message:")
message_label.grid(row=3, column=0)
message_text = tk.Text(root, height=5, width=30)
message_text.grid(row=3, column=1)

smtp_server_label = tk.Label(root, text="SMTP Server:")
smtp_server_label.grid(row=4, column=0)
smtp_server_entry = tk.Entry(root)
smtp_server_entry.grid(row=4, column=1)

smtp_port_label = tk.Label(root, text="SMTP Port:")
smtp_port_label.grid(row=5, column=0)
smtp_port_entry = tk.Entry(root)
smtp_port_entry.grid(row=5, column=1)

send_button = tk.Button(root, text="Send Email", command=send_email)
send_button.grid(row=6, columnspan=2)

root.mainloop()
