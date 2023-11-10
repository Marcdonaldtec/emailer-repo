import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject, body, to_email):
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_email_password'
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    try:
        with smtplib.SMTP('smtp.your_email_provider.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, message.as_string())
        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")


if __name__ == "__main__":
    email_subject = "Test Subject"
    email_body = "This is a test email body."
    recipient_email = "recipient@example.com"

    send_email(email_subject, email_body, recipient_email)
