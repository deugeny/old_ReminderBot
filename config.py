import os

# идентификатор бота
API_TOKEN = os.getenv('REMINDER_BOT_API_TOKEN', default='5957265855:AAGjxqDh-XqfUVFfIY6WdtjIt2OWhdFwQuA')

# путь к базе данных
DATABASE_PATH = os.getenv('REMINDER_BOT_DATABASE_PATH', default='sqlite:///jobs.db')

# Вид первого числа в формате даты. День или месяц.
DATE_FIRST_PART_KIND = os.getenv('REMINDER_BOT_DATE_FIRST_PART_KIND', default='day')

JOB_MAX_INSTANCES = 3

# trouble ticket number regular expression pattern
TROUBLE_TICKET_NUMBER_PATTERN = r'\d{8}'

