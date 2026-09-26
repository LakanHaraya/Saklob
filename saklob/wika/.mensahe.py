MGA_MENSAHE = {
    "filipino": {
        "banner": "Saklob v0.1.0",
        "exit_hint": "Itipa ang 'labas' upang umalis.",
        "goodbye": "Paalam.",

        "unknown_command": (
            "Utos ay hindi kilala: {pangalan}"
        ),

        "command_unavailable": (
            "Utos '{pangalan}' ay hindi magagamit "
            "sa konteksto '{konteksto}'."
        ),

        "help_usage": "Gamit: tulong [utos]",

        "help_commands_in_context": (
            "Mga utos sa konteksto '{konteksto}':"
        ),

        "help_command": "Utos:",

        "help_description": "Paglalarawan:",

        "help_usage_label": "Gamit:",

        "unknown_help_type": (
            "Hindi kilalang uri ng help request."
        ),

        "no_argument_help": (
            "Walang karagdagang impormasyon "
            "sa argumento para sa '{pangalan}'."
        ),

        "enter_context_usage": (
            "Gamit: pasok <konteksto>"
        ),

        "context_unavailable": (
            "Konteksto '{konteksto}' ay hindi maaaring "
            "pasukan mula sa '{kasalukuyan}'."
        ),

        "no_child_context": (
            "Walang available na child context."
        ),

        "say": "Kumusta mula sa Saklob!",
        "version": "Saklob v0.1.0",
    },

    "english": {
        "banner": "Saklob v0.1.0",
        "exit_hint": "Type 'exit' to leave.",
        "goodbye": "Goodbye.",

        "unknown_command": (
            "Unknown command: {pangalan}"
        ),

        "command_unavailable": (
            "Command '{pangalan}' is not available "
            "in context '{konteksto}'."
        ),

        "help_usage": "Usage: help [command]",

        "help_commands_in_context": (
            "Commands in context '{konteksto}':"
        ),

        "help_command": "Command:",

        "help_description": "Description:",

        "help_usage_label": "Usage:",

        "unknown_help_type": (
            "Unknown help request type."
        ),

        "no_argument_help": (
            "No additional argument information "
            "is available for '{pangalan}'."
        ),

        "enter_context_usage": (
            "Usage: enter <context>"
        ),

        "context_unavailable": (
            "Context '{konteksto}' cannot be entered "
            "from '{kasalukuyan}'."
        ),

        "no_child_context": (
            "No available child contexts."
        ),

        "say": "Hello from Saklob!",
        "version": "Saklob v0.1.0",
    },

    "cebuano": {
        "banner": "Saklob v0.1.0",
        "exit_hint": "I-type ang 'gawas' aron mogawas.",
        "goodbye": "Paalam.",

        "unknown_command": (
            "Wala mailhi nga sugo: {pangalan}"
        ),

        "command_unavailable": (
            "Ang sugo nga '{pangalan}' dili magamit "
            "sa konteksto nga '{konteksto}'."
        ),

        "help_usage": "Paggamit: tabang [sugo]",

        "help_commands_in_context": (
            "Mga sugo sa konteksto nga '{konteksto}':"
        ),

        "help_command": "Sugo:",

        "help_description": "Paghulagway:",

        "help_usage_label": "Paggamit:",

        "unknown_help_type": (
            "Wala mailhi nga matang sa help request."
        ),

        "no_argument_help": (
            "Walay dugang nga impormasyon "
            "alang sa argumento sa '{pangalan}'."
        ),

        "enter_context_usage": (
            "Paggamit: sulod <konteksto>"
        ),

        "context_unavailable": (
            "Dili masudlan ang konteksto nga '{konteksto}' "
            "gikan sa '{kasalukuyan}'."
        ),

        "no_child_context": (
            "Walay magamit nga child context."
        ),

        "say": "Kumusta gikan sa Saklob!",
        "version": "Saklob v0.1.0",
    },
}


def mensahe(locale, susi, **halaga):
    teksto = MGA_MENSAHE[locale][susi]

    if halaga:
        return teksto.format(**halaga)

    return teksto