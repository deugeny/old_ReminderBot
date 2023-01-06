import unittest
import message_parser
from datetime import datetime


class MessageParserTestCase(unittest.TestCase):
    def test_parse_remind_message_empty_message_successfully(self):
        message = ""
        expected_result = None, "", None
        actual_result = message_parser.parse_remind_message(message)
        self.assertEqual(expected_result, actual_result)  # add assertion here

    def test_parse_remind_message_without_parameters_successfully(self):
        message = "/remind"
        expected_result = None, "", None
        actual_result = message_parser.parse_remind_message(message)
        self.assertEqual(expected_result, actual_result)  # add assertion here

    def test_parse_remind_message_without_time_successfully(self):
        today = datetime.today()
        today_str = today.strftime("%d.%m.%Y")
        command_text = f"please run task at {today_str}"
        command = "/remind "
        message = command + command_text
        expected_result = today, command_text, None
        actual_result = message_parser.parse_remind_message(message)
        self.assertEqual(expected_result, actual_result)  # add assertion here

    def test_parse_remind_message_without_date_successfully(self):
        now = datetime.now()
        not_time_str = str(now.time())
        command_text = f"please run task at {not_time_str}"
        command = "/remind "
        message = command + command_text
        expected_result = now, command_text, None
        actual_result = message_parser.parse_remind_message(message)
        self.assertEqual(expected_result, actual_result)  # add assertion here

    def test_parse_remind_message_with_datetime_successfully(self):
        now = datetime.now()
        dt = now.date().strftime("%d.%m.%Y")
        time = str(now.time())
        command_text = f"please run task {dt} at {time}"
        command = "/remind "
        message = command + command_text
        expected_result = now, command_text, None
        actual_result = message_parser.parse_remind_message(message)
        self.assertEqual(expected_result, actual_result)  # add assertion here

    def test_parse_remind_message_with_datetime_and_trouble_ticket_number_successfully(self):
        trouble_ticket_number = '12345678'
        now = datetime.now()
        dt = now.date().strftime("%d.%m.%Y")
        time = str(now.time())
        command_text = f"please run task {dt} at {time}. trouble ticket number {trouble_ticket_number}."
        command = "/remind "
        message = command + command_text
        expected_result = now, command_text, trouble_ticket_number
        actual_result = message_parser.parse_remind_message(message)
        self.assertEqual(expected_result, actual_result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
