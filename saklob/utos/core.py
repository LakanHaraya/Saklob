from saklob.utos.utos import Utos

MAX_SAY_ARGUMENT_LENGTH = 32

def lumikha_core_utos(makina):
    def sabihin(argumento):
        if not argumento:
            print(makina.mensahe("say"))
            return

        teksto = " ".join(argumento)

        if len(teksto) > MAX_SAY_ARGUMENT_LENGTH:
            print(
                makina.mensahe(
                    "say_argument_too_long",
                    maximum=MAX_SAY_ARGUMENT_LENGTH
                )
            )
            return

        print(
            makina.mensahe(
                "say_with_argument",
                argumento=teksto
            )
        )

    def bersiyon(argumento):
        print(makina.mensahe("version"))

    def tulong(argumento):
        makina.tulong.ipakita(argumento)

    def labas(argumento):
        makina.tumatakbo = False
        print(makina.mensahe("goodbye"))

    def pasok(argumento):
        if len(argumento) != 1:
            print(
                makina.mensahe(
                    "enter_context_usage"
                )
            )
            return

        kasalukuyan = str(makina.sesyon.konteksto)

        mga_papasukan = makina.konteksto_rehistro.mga_papasukan(
            kasalukuyan
        )

        if argumento[0] not in mga_papasukan:
            print(
                makina.mensahe(
                    "context_unavailable",
                    konteksto=argumento[0],
                    kasalukuyan=kasalukuyan
                )
            )
            return

        makina.sesyon.pasok(argumento[0])

    def balik(argumento):
        if makina.sesyon.mode == "kumpigurasyon":
            makina.sesyon.mode = "normal"
            return

        makina.sesyon.balik()

    def tulong_pasok(konteksto):
        mga_papasukan = makina.konteksto_rehistro.mga_papasukan(
            konteksto
        )

        if not mga_papasukan:
            return [
                makina.mensahe(
                    "no_child_context"
                )
            ]

        return [
            f"  {pangalan}"
            for pangalan in mga_papasukan
        ]

    def kumpigurahin(argumento):
        if argumento:
            print(
                makina.mensahe(
                    "configure_usage"
                )
            )
            return

        makina.sesyon.mode = "kumpigurasyon"

    return [
        Utos("SAY", sabihin),
        Utos("VERSION", bersiyon),
        Utos("HELP", tulong),
        Utos(
            "ENTER_CONTEXT",
            pasok,
            provider_tulong=tulong_pasok
        ),
        Utos("EXIT_CONTEXT", balik),
        Utos("EXIT", labas),
        Utos(
            "CONFIGURE",
            kumpigurahin,
            mga_mode=["normal"]
        ),
    ]