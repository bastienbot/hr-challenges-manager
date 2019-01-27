import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailSender:

    EMAIL_HOST = 'email-smtp.eu-west-1.amazonaws.com'
    EMAIL_HOST_USER = os.getenv("SES_USERNAME")
    EMAIL_HOST_PASSWORD = os.getenv("SES_PASSWORD")
    EMAIL_PORT = 587

    """
    @desc Sends an email with an html body to a candidate through SES

    @params profile: dict
    @params content: str
    @returns
    """
    def send(profile, content):
        # Recipients list is declared
        rcpt = [profile.get("email")]
        message = MIMEMultipart('alternative')
        message['Subject'] = "Clevy challenge"
        message['From'] = "bastien@clevy.io"
        message['To'] = profile.get("email")
        if os.getenv("BCC_EMAIL") is not None and len(os.getenv("BCC_EMAIL")) > 5:
            # We add BCC to recipients list if needed
            message['Bcc'] = os.getenv("BCC_EMAIL")
            rcpt.append(message['Bcc'])

        html = content
        mime_text = MIMEText(html, 'html')
        message.attach(mime_text)

        s = smtplib.SMTP(EmailSender.EMAIL_HOST, EmailSender.EMAIL_PORT)
        s.starttls()
        # We add the recipients list as param
        s.login(EmailSender.EMAIL_HOST_USER, EmailSender.EMAIL_HOST_PASSWORD)
        s.sendmail(message["From"], rcpt, message.as_string())
        s.quit()
