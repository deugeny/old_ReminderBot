FROM python:3.11-alpine

WORKDIR /usr/src/reminderbot

ENV TELEGRAM_API_TOKEN="5957265855:AAGjxqDh-XqfUVFfIY6WdtjIt2OWhdFwQuA"
COPY pip_requirements.txt ./
RUN pip install --no-cache-dir -r pip_requirements.txt

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#RUN pip install -U pip aiogram pytz && apt-get update && apt-get install sqlite3
RUN apt-get update && apt-get install sqlite3
COPY *.py ./

ENTRYPOINT ["python", "main.py"]