from email.message import EmailMessage
import ssl
import smtplib

email_sender = ''       # your email
email_password = ''     # your email's app password

email_receiver = ''     # email of the person reciving the message

subject = 'This is a Test'
body = """
Hey, this message is a test to sent an email using python.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())