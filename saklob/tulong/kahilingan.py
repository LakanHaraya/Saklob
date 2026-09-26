class HelpRequest:
    GENERAL = "general"
    COMMAND = "command"
    ARGUMENT = "argument"

    def __init__(self, uri, utos=None):
        self.uri = uri
        self.utos = utos