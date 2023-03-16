from smtplib import SMTP_SSL

from config import SMTP_PASSWORD, SMTP_USER, SMTP_HOST, SMTP_PORT

from .settings import tasker
from .letter_func import gmail_registration_letter


@tasker.task
def auth_gmail_letter(confirmation_link: str) -> None:

    message = gmail_registration_letter(confirmation_link)
    with SMTP_SSL(host=SMTP_HOST, port=SMTP_PORT) as postman:
        postman.login(SMTP_USER, SMTP_PASSWORD)
        postman.send_message(message)
    