import unittest

from saklob.ui.terminal import Terminal


class TestTerminal(unittest.TestCase):

    def test_terminal_creates_input_buffer(self):
        terminal = Terminal()

        self.assertEqual(
            terminal.input_buffer.haba,
            32
        )

        self.assertEqual(
            terminal.input_buffer.maximum,
            128
        )


if __name__ == "__main__":
    unittest.main()