import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailSender:

    EMAIL_HOST = 'email-smtp.eu-west-1.amazonaws.com'
    EMAIL_HOST_USER = os.getenv("SES_USERNAME")
    EMAIL_HOST_PASSWORD = os.getenv("SES_PASSWORD")
    EMAIL_PORT = 587

    def send(candidate, template):
        message = MIMEMultipart('alternative')
        message['Subject'] = "Clevy technical test"
        message['From'] = "bastien@clevy.io"
        message['To'] = candidate.email

        html = template.get_template()
        mime_text = MIMEText(html, 'html')
        message.attach(mime_text)

        s = smtplib.SMTP(EmailSender.EMAIL_HOST, EmailSender.EMAIL_PORT)
        s.starttls()
        s.login(EmailSender.EMAIL_HOST_USER, EmailSender.EMAIL_HOST_PASSWORD)
        s.sendmail(message["From"], message["To"], message.as_string())
        s.quit()
