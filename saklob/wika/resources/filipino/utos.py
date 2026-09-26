MGA_UTOS = {
    "SAY": {
        "name": "sabihin",
        "description": "Magpakita ng mensahe.",
    },
    "VERSION": {
        "name": "bersiyon",
        "description": "Ipakita ang bersiyon ng Saklob.",
    },
    "HELP": {
        "name": "tulong",
        "description": "Ipakita ang mga available na utos.",
        "usage": "tulong [utos]",
    },
    "ENTER_CONTEXT": {
        "name": "pasok",
        "description": "Pumasok sa isang konteksto.",
        "usage": "pasok <konteksto>",
    },
    "EXIT_CONTEXT": {
        "name": "balik",
        "description": "Bumalik sa parent context.",
    },
    "EXIT": {
        "name": "labas",
        "description": "Lumabas sa Saklob.",
    },
}


def irehistro(bokabularyo):
    bokabularyo.idagdag("sabihin", "SAY")
    bokabularyo.idagdag("bersiyon", "VERSION")
    bokabularyo.idagdag("tulong", "HELP")
    bokabularyo.idagdag("pasok", "ENTER_CONTEXT")
    bokabularyo.idagdag("balik", "EXIT_CONTEXT")
    bokabularyo.idagdag("labas", "EXIT")


def kunin_utos(command_id):
    return MGA_UTOS.get(command_id)