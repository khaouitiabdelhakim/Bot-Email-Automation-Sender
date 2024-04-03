import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender and receiver email addresses
sender = ["myemail@gmail.com", "aaaa bbbb cccc dddd"]
receiver_email = "receiver_email"

# Function to send email
def sendEmail(to, sender_email, password):
    # Create a multipart message
    message = MIMEMultipart("alternative")
    message["Subject"] = "Write Your Subject Here"
    message["From"] = "Name of the sender"
    message["To"] = to
    message["Importance"] = "high"  # Set the importance level

    # HTML content of the email
    html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Email Sample</title>
        </head>
        <body>
            <div>
                <h1>Hello</h1>
                <h3>how are you?</h3>
            </div>
        </body>
        </html>"""
        
    # Create a MIMEText object with the HTML content
    part2 = MIMEText(html, "html")
    message.attach(part2)

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Connect to the SMTP server and send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        try:
            # Login to the server using the sender's email and password
            server.login(sender_email, password)
            
            # Send the email
            server.sendmail(sender_email, to, message.as_string())
            
            # Print a success message
            print(f"Email sent successfully to {to}")
        except smtplib.SMTPAuthenticationError as e:
            # Handle authentication errors
            print(f"SMTP Authentication Error: {e}")
            print("Check username, password, and 'Less Secure Apps' access.")
        except Exception as e:
            # Handle other exceptions
            print(f"An error occurred: {e}")

# Call the sendEmail function with the receiver email, sender's email, and password
sendEmail(receiver_email, sender[0], sender[1])

# Copyright information
"""
Author: KHAOUITI ABDELHAKIM
GitHub: @khaouitiabdelhakim
""" 
