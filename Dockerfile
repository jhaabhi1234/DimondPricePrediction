FROM python:3.11-slim-buster
WORKDIR /service
COPY requirements.txt .
RUN pip install -r requirement.txt
COPY . ./
ENTRYPOINT [ "python3", "app.py" ]