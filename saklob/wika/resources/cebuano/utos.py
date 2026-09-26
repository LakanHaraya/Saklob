MGA_UTOS = {
    "SAY": {
        "name": "ingon",
        "description": "Ipakita ang usa ka mensahe.",
    },
    "VERSION": {
        "name": "bersiyon",
        "description": "Ipakita ang bersiyon sa Saklob.",
    },
    "HELP": {
        "name": "tabang",
        "description": "Ipakita ang mga mausage nga sugo.",
        "usage": "tabang [sugo]",
    },
    "ENTER_CONTEXT": {
        "name": "sulod",
        "description": "Sulod sa usa ka konteksto.",
        "usage": "sulod <konteksto>",
    },
    "EXIT_CONTEXT": {
        "name": "balik",
        "description": "Balik sa parent context.",
    },
    "EXIT": {
        "name": "gawas",
        "description": "Gawas sa Saklob.",
    },
}


def irehistro(bokabularyo):
    bokabularyo.idagdag("ingon", "SAY")
    bokabularyo.idagdag("bersiyon", "VERSION")
    bokabularyo.idagdag("tabang", "HELP")
    bokabularyo.idagdag("sulod", "ENTER_CONTEXT")
    bokabularyo.idagdag("balik", "EXIT_CONTEXT")
    bokabularyo.idagdag("gawas", "EXIT")


def kunin_utos(command_id):
    return MGA_UTOS.get(command_id)