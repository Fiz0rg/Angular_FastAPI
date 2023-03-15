from .settings import tasker


@tasker.task
def auth_gmail_letter(confirmation_link: str) -> None:
    
    pass