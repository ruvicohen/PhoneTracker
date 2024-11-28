FROM python:3.8-slim

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY .env .env

EXPOSE 5000

ENV PYTHONPATH=/app

CMD ["python", "app/main.py"]