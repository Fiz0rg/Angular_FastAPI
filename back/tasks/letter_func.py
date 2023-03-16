from email.message import EmailMessage

from config import SMTP_USER


def  gmail_registration_letter(registration_link: str):
    message = EmailMessage()

    message["Subject"] = f'Message from {SMTP_USER}'
    message["From"] = SMTP_USER
    message["To"] = SMTP_USER

    message.set_content(f"""/
    For registration follow this link {registration_link}
    """)

    return message