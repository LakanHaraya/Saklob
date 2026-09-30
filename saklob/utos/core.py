from saklob.utos.utos import Utos

def lumikha_core_utos(makina):
    def sabihin(argumento):
        if not argumento:
            print(makina.mensahe("say"))
            return

        teksto = " ".join(argumento)

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

        mga_linya = [
            makina.mensahe(
                "available_child_contexts"
            )
        ]

        for pangalan in mga_papasukan:
            buong_konteksto = (
                f"{konteksto}:{pangalan}"
            )

            deskripsiyon = (
                makina.konteksto_rehistro
                .kunin_deskripsiyon(buong_konteksto)
            )

            if deskripsiyon is None:
                mga_linya.append(
                    f"  {pangalan}"
                )
                continue

            mga_linya.append(
                f"  {pangalan:<16} {deskripsiyon}"
            )

        return mga_linya

    def kumpigurahin(argumento):
        if argumento:
            print(
                makina.mensahe(
                    "configure_usage"
                )
            )
            return

        makina.sesyon.mode = "kumpigurasyon"

    def haba(argumento):
        if not argumento:
            print(
                f"FREE_FORM_INPUT_LENGTH: "
                f"{makina.config.kunin_panimula_free_form_input_length()}"
            )
            return

        if len(argumento) != 1:
            print(
                "Gamit: haba <halaga>"
            )
            return

        try:
            halaga = int(argumento[0])
        except ValueError:
            print(
                "Ang haba ay dapat isang buong bilang."
            )
            return

        try:
            makina.config.itakda_panimula_free_form_input_length(
                halaga
            )
        except ValueError:
            print(
                "FREE_FORM_INPUT_LENGTH ay wala sa "
                "pinapahintulutang saklaw."
            )
            return

        print(
            f"FREE_FORM_INPUT_LENGTH: "
            f"{makina.config.kunin_panimula_free_form_input_length()}"
        )
    
    def isulat(argumento):
        if argumento:
            print(
                "Gamit: isulat"
            )
            return

        makina.config.ilagak()

        print(
            "Naisulat ang panimulang kumpigurasyon."
        )

    def ipakita(argumento):
        if len(argumento) != 2:
            print(
                "Gamit: ipakita kumpigurasyon "
                "<tumatakbo|panimula|nakasulat|lahat>"
            )
            return

        if argumento[0] != "kumpigurasyon":
            print(
                f"Walang impormasyon para sa "
                f"'{argumento[0]}'."
            )
            return

        estado = argumento[1]

        if estado == "tumatakbo":
            print("Kumpigurasyon:")
            print(
                f"  FREE_FORM_INPUT_LENGTH: "
                f"{makina.config.kunin_tumatakbo_free_form_input_length()}"
            )
            return

        if estado == "panimula":
            print("Kumpigurasyon:")
            print(
                f"  FREE_FORM_INPUT_LENGTH: "
                f"{makina.config.kunin_panimula_free_form_input_length()}"
            )
            return

        if estado == "nakasulat":
            print("Kumpigurasyon:")
            print(
                f"  FREE_FORM_INPUT_LENGTH: "
                f"{makina.config.kunin_nakasulat_free_form_input_length()}"
            )
            return

        if estado == "lahat":
            print("Kumpigurasyon:")

            print("  Tumatakbo:")
            print(
                f"    FREE_FORM_INPUT_LENGTH: "
                f"{makina.config.kunin_tumatakbo_free_form_input_length()}"
            )

            print("  Panimula:")
            print(
                f"    FREE_FORM_INPUT_LENGTH: "
                f"{makina.config.kunin_panimula_free_form_input_length()}"
            )

            print("  Nakasulat:")
            print(
                f"    FREE_FORM_INPUT_LENGTH: "
                f"{makina.config.kunin_nakasulat_free_form_input_length()}"
            )
            return

        print(
            f"Walang impormasyon para sa "
            f"'{estado}'."
        )

    return [
        Utos(
            "SAY",
            sabihin,
            malayang_input=True
        ),
        Utos("VERSION", bersiyon),
        Utos("HELP", tulong),
        Utos(
            "ENTER_CONTEXT",
            pasok,
            mga_mode=["normal"],
            provider_tulong=tulong_pasok
        ),
        Utos(
            "EXIT_CONTEXT",
            balik,
            kailangan_magulang=True
        ),
        Utos("EXIT", labas),
        Utos(
            "CONFIGURE",
            kumpigurahin,
            mga_mode=["normal"]
        ),
        Utos(
            "INPUT_LENGTH",
            haba,
            mga_mode=["kumpigurasyon"]
        ),
        Utos(
            "WRITE_CONFIG",
            isulat,
            mga_mode=["kumpigurasyon"]
        ),
        Utos(
            "SHOW",
            ipakita,
            mga_mode=["kumpigurasyon"]
        ),
    ]