import os 

from dotenv import load_dotenv

load_dotenv()


SMTP_SECRET_KEY = os.environ.get("SMTP_SECRET_KEY")
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
SMTP_HOST = os.environ.get("SMTP_HOST")
SMTP_PORT = os.environ.get("SMTP_PORT")