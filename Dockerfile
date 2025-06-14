FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y wget unzip curl gnupg2 chromium chromium-driver && \
    pip install --no-cache-dir flask selenium webdriver-manager

WORKDIR /app
COPY . /app
CMD ["python", "server.py"]
