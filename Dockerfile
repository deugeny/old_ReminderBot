FROM python:3.11-alpine

WORKDIR /usr/src/reminderbot

ENV REMINDER_BOT_API_TOKEN="5957265855:AAGjxqDh-XqfUVFfIY6WdtjIt2OWhdFwQuA"
ENV REMINDER_BOT_CONNECTION_STRING="sqlite:///jobs.db"
ENV REMINDER_BOT_DATE_FIRST_PART_KIND="day"
ENV REMINDER_BOT_JOB_MAX_INSTANCES=20
ENV REMINDER_BOT_THRED_POOL_EXECUTORS_COUNT=20
ENV REMINDER_BOT_PROCESS_POOL_EXECUTORS_COUNT=5

COPY pip_requirements.txt ./
RUN pip install --no-cache-dir -r pip_requirements.txt

RUN apk add --no-cache tzdata
ENV TZ=Europe/Moscow
RUN cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime

#UBUNTU
#RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apk update && apk upgrade
RUN apk add --no-cache sqlite

COPY *.py ./

ENTRYPOINT ["python", "main.py"]