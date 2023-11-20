import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from validate_email_address import validate_email

class EmailSender:
    def __init__(self, server, port, sender_email, password):
        self.server = server
        self.port = port
        self.sender_email = sender_email
        self.password = password

    def setup_email_server(self):
        return {'server': self.server, 'port': self.port, 'sender_email': self.sender_email, 'password': self.password}

    @staticmethod
    def is_valid_email(email):
        try:
            result = validate_email(email, verify=False)
            return result and '@' in email
        except Exception as e:
            print(f"Error validating email: {e}")
        return False

    def send_email(self, recipient, subject, body):
        if not self.is_valid_email(recipient):
            raise ValueError("Imèl sa pa valide.")

        server_info = self.setup_email_server()

        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(self.server, self.port) as email_server:
            email_server.starttls()
            email_server.login(self.sender_email, self.password)
            email_server.sendmail(self.sender_email, recipient, msg.as_string())

recipient_email = input("Entrez l'adresse email du destinataire : ")
email_subject = input("Entrez le sujet de l'email : ")
email_body = input("Entrez le contenu de l'email : ")

emailer = EmailSender(server="smtp.gmail.com", port=587, sender_email="marcdonaldtech40@gmail.com", password="msbx kmxx omit uthm ")
emailer.send_email(recipient=recipient_email, subject=email_subject, body=email_body)
