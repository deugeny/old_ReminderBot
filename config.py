import os

# идентификатор бота
API_TOKEN = os.getenv('REMINDER_BOT_API_TOKEN', default='5957265855:AAGjxqDh-XqfUVFfIY6WdtjIt2OWhdFwQuA')

# путь к базе данных
DATABASE_CONNECTION_STRING = os.getenv('REMINDER_BOT_CONNECTION_STRING', default='sqlite:///jobs.db')

# Вид первого числа в формате даты. День или месяц.
DATE_FIRST_PART_KIND = os.getenv('REMINDER_BOT_DATE_FIRST_PART_KIND', default='day')

JOB_MAX_INSTANCES = os.getenv('REMINDER_BOT_JOB_MAX_INSTANCES', default=3)

THREAD_POOL_EXECUTORS_COUNT = os.getenv('REMINDER_BOT_THREAD_POOL_EXECUTORS_COUNT', default=20)

PROCESS_POOL_EXECUTORS_COUNT = os.getenv('REMINDER_BOT_PROCESS_POOL_EXECUTORS_COUNT', default=5)

# trouble ticket number regular expression pattern
TROUBLE_TICKET_NUMBER_PATTERN = r'\d{8}'

