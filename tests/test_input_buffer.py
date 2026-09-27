import unittest

from saklob.ui.input_buffer import InputBuffer


class TestInputBuffer(unittest.TestCase):

    def test_input_within_limit(self):
        buffer = InputBuffer(
            maximum=128,
            haba=32
        )

        self.assertTrue(
            buffer.tanggapin("hello")
        )

    def test_input_at_limit(self):
        buffer = InputBuffer(
            maximum=128,
            haba=32
        )

        teksto = "a" * 32

        self.assertTrue(
            buffer.tanggapin(teksto)
        )

    def test_input_over_limit(self):
        buffer = InputBuffer(
            maximum=128,
            haba=32
        )

        teksto = "a" * 33

        self.assertFalse(
            buffer.tanggapin(teksto)
        )

    def test_minimum_length(self):
        buffer = InputBuffer(
            maximum=128,
            haba=8
        )

        self.assertTrue(
            buffer.tanggapin("12345678")
        )

        self.assertFalse(
            buffer.tanggapin("123456789")
        )

    def test_maximum_length(self):
        buffer = InputBuffer(
            maximum=128,
            haba=128
        )

        self.assertTrue(
            buffer.tanggapin("a" * 128)
        )

        self.assertFalse(
            buffer.tanggapin("a" * 129)
        )

    def test_length_cannot_exceed_maximum(self):
        with self.assertRaises(ValueError):
            InputBuffer(
                maximum=128,
                haba=129
            )

    def test_length_cannot_be_below_minimum(self):
        with self.assertRaises(ValueError):
            InputBuffer(
                minimum=8,
                maximum=128,
                haba=7
            )

if __name__ == "__main__":
    unittest.main()