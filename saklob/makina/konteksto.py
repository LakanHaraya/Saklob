class Konteksto:
    def __init__(self, pangalan, magulang=None):
        self.pangalan = pangalan
        self.magulang = magulang

    def __str__(self):
        if self.magulang is None:
            return self.pangalan

        return f"{self.magulang}:{self.pangalan}"