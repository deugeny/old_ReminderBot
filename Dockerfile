FROM python:3.11-alpine

WORKDIR /usr/src/reminderbot

ENV REMINDER_BOT_API_TOKEN="5957265855:AAGjxqDh-XqfUVFfIY6WdtjIt2OWhdFwQuA"
ENV REMINDER_BOT_CONNECTION_STRING="sqlite:///jobs.db"
ENV REMINDER_BOT_DATE_FIRST_PART_KIND="day"
ENV REMINDER_BOT_JOB_MAX_INSTANCES=3
ENV REMINDER_BOT_THRED_POOL_EXECUTORS_COUNT=20
ENV REMINDER_BOT_PROCESS_POOL_EXECUTORS_COUNT=5

COPY pip_requirements.txt ./
RUN pip install --no-cache-dir -r pip_requirements.txt

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#RUN pip install -U pip aiogram pytz && apt-get update && apt-get install sqlite3
RUN apt-get update && apt-get install sqlite3
COPY *.py ./

ENTRYPOINT ["python", "main.py"]