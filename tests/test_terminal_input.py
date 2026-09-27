import unittest

from saklob.ui.input_buffer import InputBuffer


class TestTerminalInput(unittest.TestCase):

    def test_input_at_operational_limit_is_accepted(self):
        buffer = InputBuffer(
            maximum=128,
            minimum=8,
            haba=32
        )

        self.assertTrue(
            buffer.tanggapin("a" * 32)
        )

    def test_input_above_operational_limit_is_rejected(self):
        buffer = InputBuffer(
            maximum=128,
            minimum=8,
            haba=32
        )

        self.assertFalse(
            buffer.tanggapin("a" * 33)
        )


if __name__ == "__main__":
    unittest.main()