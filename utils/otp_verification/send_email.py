import smtplib


class EmailAutomation:
    @staticmethod
    def send_email(subject, message, recipient_email):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(
            "chtsharsha@gmail.com",
            "eyai gdyd nkyb bzow",
        )
        email_body = f"To: {recipient_email}\nSubject: {subject}\n\n{message}"
        server.sendmail("chtsharsha@gmail.com", recipient_email, email_body)
