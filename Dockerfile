FROM mcr.microsoft.com/playwright/python:v1.44.0-focal

WORKDIR /if_task

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
CMD ["pytest", "tests/"]