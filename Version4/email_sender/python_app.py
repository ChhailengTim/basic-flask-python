from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = 'dmoza2018@gmail.com'
email_password = password

email_receivers = ['chhailengtim2018@gmail.com', 'vexeteh811@cdeter.com']

subject = 'Email Sender Version2'
body = """
Let's try and test with my coding.
"""

for email_receiver in email_receivers:
    em = EmailMessage()
    em['From'] = 'Test 2'
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)


    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
