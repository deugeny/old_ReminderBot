from datetime import datetime
from typing import Final
from telebot import formatting

# strings
START_MESSAGE: Final = formatting.format_text("Привет 🖐\r\nЯ, Бот <b>Управляющий напоминаниями</b>\r\n"
                                                "Выберите раздел с которым хотите взаимодействовать:\r\n"
                                                "--------------------------------------------------------------\r\n"
                                                "⏰ <b>создать</b> - Создание нового напоминания\r\n\r\n"
                                                "🔍 <b>просмотр</b> - Просмотр ранее созданных напоминаний\r\n\r\n"
                                                "❌ <b>отменить</b> - Просмотр ранее созданных напоминаний\r\n")

REMIND_MESSAGE = f'Используйте команду /remind для установки напоминания. Дата и время ' \
                 f'будут извлечены из сообщения. Если дата не указана, то будет использована текущая.' \
                 f'\r\nПример: /remind Запустить установку ОС {datetime.now().strftime("%d.%m.%Y в %H:%M")} '

CONFIRMATION_MESSAGE = 'Вы установили напоминание на дату/время {0}. Для отмены используйте команду /cancel {1}'

HELP_MESSAGE = 'Применение:/help command - отображает справку по применению команды command.'

CANCEL_MESSAGE = "/cancel [id|all] используйте для отмены напоминания с идентификатором id или всех напоминаний 'all'"

START_COMMAND_DESCRIPTION = "Начало работы с ботом."
HELP_COMMAND_DESCRIPTION = "Получение справки по работе с ботом."
REMIND_COMMAND_DESCRIPTION = "Установка напоминаний"
CANCEL_COMMAND_DESCRIPTION = "Отмена напоминаний"
INVALID_ARGUMENT = "Ошибочный аргумент. "
UNKNOWN_JOB_FORMAT = 'Не найдено напоминание с id={0}'
ALL_JOBS_CANCELED = "Произведена отмена всех напоминаний"

ERROR_DATETIME = "Ошибочные дата или время. Дата и время запуска напоминания должны быть больше текущего времени."

ERROR_MESSAGE = "Произошла ошибка"

REQUEST_CANCELLATION_TARGET_MESSAGE = 'Укажите номер отменяемого задания или all для отмены всех заданий?'
