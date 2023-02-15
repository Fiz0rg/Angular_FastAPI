FROM python:3.10.7

WORKDIR /store

COPY ./back/requirements.txt /store/back/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /store/back/requirements.txt

COPY ./back /store/back

CMD ["uvicorn", "back.server:app", "--reload", "--port", "8000"]