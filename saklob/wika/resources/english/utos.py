MGA_UTOS = {
    "SAY": {
        "name": "say",
        "description": "Display a message.",
    },
    "VERSION": {
        "name": "version",
        "description": "Display the Saklob version.",
    },
    "HELP": {
        "name": "help",
        "description": "Display available commands.",
        "usage": "help [command]",
    },
    "ENTER_CONTEXT": {
        "name": "enter",
        "description": "Enter a context.",
        "usage": "enter <context>",
    },
    "EXIT_CONTEXT": {
        "name": "back",
        "description": "Return to the parent context.",
    },
    "EXIT": {
        "name": "exit",
        "description": "Exit Saklob.",
    },
}


def irehistro(bokabularyo):
    bokabularyo.idagdag("say", "SAY")
    bokabularyo.idagdag("version", "VERSION")
    bokabularyo.idagdag("help", "HELP")
    bokabularyo.idagdag("enter", "ENTER_CONTEXT")
    bokabularyo.idagdag("back", "EXIT_CONTEXT")
    bokabularyo.idagdag("exit", "EXIT")


def kunin_utos(command_id):
    return MGA_UTOS.get(command_id)