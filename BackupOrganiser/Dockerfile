FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 5000
ENV PYTHONUNBUFFERED=1

CMD ["python3", "app.py"]