import smtplib
from email.mime.text import MIMEText

class EmailService:
    def send_email(self, email_message):
        msg = MIMEText(email_message.body)

        msg['Subject'] = email_message.subject
        msg['From'] = email_message.from_address
        msg['To'] = email_message.to_address

        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()