class Tulong:
    def __init__(self, makina):
        self.makina = makina

    def ipakita(self, argumento=None):
        argumento = argumento or []

        konteksto = str(self.makina.sesyon.konteksto)

        if len(argumento) == 0:
            self._ipakita_lahat(konteksto)
            return

        if len(argumento) != 1:
            print(self.makina.mensahe("help_usage"))
            return

        self._ipakita_utos(argumento[0], konteksto)

    def iproseso(self, kahilingan):
        konteksto = str(self.makina.sesyon.konteksto)

        if kahilingan.uri == "general":
            self._ipakita_lahat(konteksto)
            return

        if kahilingan.uri == "command":
            self._ipakita_utos(
                kahilingan.utos,
                konteksto
            )
            return

        if kahilingan.uri == "argument":
            self._ipakita_argumento(
                kahilingan.utos,
                konteksto
            )
            return

        print(self.makina.mensahe("unknown_help_type"))

    def _ipakita_lahat(self, konteksto):
        print(
            self.makina.mensahe(
                "help_commands_in_context",
                konteksto=konteksto
            )
        )

        for utos in self.makina.rehistro.mga_magagamit(
            konteksto,
            self.makina.sesyon.mode,
            self.makina.sesyon.konteksto.magulang is not None
        ):
            metadata = self.makina.kunin_utos_metadata(
                utos.id
            )

            if metadata is None:
                continue

            print(
                f"  {metadata['name']:<16}"
                f" {metadata['description']}"
            )

    def _ipakita_utos(self, pangalan, konteksto):
        utos = self.makina.kunin_utos(pangalan)

        if utos is None:
            print(
                self.makina.mensahe(
                    "unknown_command",
                    pangalan=pangalan
                )
            )
            return

        if not utos.magagamit_sa(konteksto):
            print(
                self.makina.mensahe(
                    "command_unavailable",
                    pangalan=pangalan,
                    konteksto=konteksto
                )
            )
            return

        if not utos.magagamit_sa_mode(
            self.makina.sesyon.mode
        ):
            print(
                self.makina.mensahe(
                    "command_unavailable_mode",
                    pangalan=pangalan,
                    mode=self.makina.sesyon.mode
                )
            )
            return

        if (
            utos.kailangan_magulang
            and self.makina.sesyon.mode == "normal"
            and self.makina.sesyon.konteksto.magulang is None
        ):
            print(
                self.makina.mensahe(
                    "command_unavailable",
                    pangalan=pangalan,
                    konteksto=konteksto
                )
            )
            return

        metadata = self.makina.kunin_utos_metadata(
            utos.id
        )

        if metadata is None:
            return

        print(
            self.makina.mensahe("help_command")
            + f" {metadata['name']}"
        )

        print(
            self.makina.mensahe("help_description")
            + f" {metadata['description']}"
        )

        if metadata.get("usage"):
            print(
                self.makina.mensahe("help_usage_label")
                + f" {metadata['usage']}"
            )

    def _ipakita_argumento(self, pangalan, konteksto):
        utos = self.makina.kunin_utos(pangalan)

        if utos is None:
            print(
                self.makina.mensahe(
                    "unknown_command",
                    pangalan=pangalan
                )
            )
            return

        if not utos.magagamit_sa(konteksto):
            print(
                self.makina.mensahe(
                    "command_unavailable",
                    pangalan=pangalan,
                    konteksto=konteksto
                )
            )
            return

        if not utos.magagamit_sa_mode(
            self.makina.sesyon.mode
        ):
            print(
                self.makina.mensahe(
                    "command_unavailable_mode",
                    pangalan=pangalan,
                    mode=self.makina.sesyon.mode
                )
            )
            return

        if (
            utos.kailangan_magulang
            and self.makina.sesyon.mode == "normal"
            and self.makina.sesyon.konteksto.magulang is None
        ):
            print(
                self.makina.mensahe(
                    "command_unavailable",
                    pangalan=pangalan,
                    konteksto=konteksto
                )
            )
            return

        metadata = self.makina.kunin_utos_metadata(
            utos.id
        )

        if metadata is None:
            return

        if utos.provider_tulong:
            mga_linya = utos.provider_tulong(konteksto)

            for linya in mga_linya:
                print(linya)

            return

        if metadata.get("usage"):
            print(
                self.makina.mensahe("help_usage_label")
                + f" {metadata['usage']}"
            )
            return

        print(
            self.makina.mensahe(
                "no_argument_help",
                pangalan=metadata["name"]
            )
        )