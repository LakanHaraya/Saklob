from saklob.config.build import MAX_CLI_INPUT_LENGTH

class InputBuffer:
    def __init__(
        self,
        maximum=MAX_CLI_INPUT_LENGTH
    ):
        self.maximum = maximum

    def tanggapin(self, teksto):
        return len(teksto) <= self.maximum