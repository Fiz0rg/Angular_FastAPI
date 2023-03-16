from email.message import EmailMessage

from config import SMTP_USER


def  gmail_registration_letter(registration_link: str, user_gmail: str) -> EmailMessage:
    message = EmailMessage()

    message["Subject"] = f'Message from {SMTP_USER}'
    message["From"] = SMTP_USER
    message["To"] = user_gmail

    message.set_content(f"""/
    For registration follow this link {registration_link}
    """)

    return message