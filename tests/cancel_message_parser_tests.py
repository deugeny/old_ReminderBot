import unittest

from handlers import cancel_command_handler


class CancelMessageParsingTestCase(unittest.TestCase):
    def test_parse_cancel_command_empty_message(self):
        command = ''
        expected = None
        actual = cancel_command_handler.parse_cancel_command(command)
        self.assertEqual(expected, actual)  # add assertion here

    def test_parse_cancel_command_message_without_parameters(self):
        command = '/cancel'
        expected = None
        actual = cancel_command_handler.parse_cancel_command(command)
        self.assertEqual(expected, actual)  # add assertion here

    def test_parse_cancel_command_message_with_all_argument(self):
        command = '/cancel all'
        expected = 'all'
        actual = cancel_command_handler.parse_cancel_command(command)
        self.assertEqual(expected, actual)  # add assertion here

    def test_parse_cancel_command_message_with_id_argument(self):
        command = '/cancel 123456'
        expected = '123456'
        actual = cancel_command_handler.parse_cancel_command(command)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
