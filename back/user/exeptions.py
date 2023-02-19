from fastapi import status, HTTPException

def exceptions(headers: dict) -> HTTPException:
        return HTTPException(
                             status_code=status.HTTP_401_UNAUTHORIZED,
                             detail="Could not validate credentials",
                             headers=headers)

