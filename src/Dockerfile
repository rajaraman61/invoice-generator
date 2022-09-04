
FROM python:3.8-slim

WORKDIR /src
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000