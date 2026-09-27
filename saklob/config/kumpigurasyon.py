import json
from pathlib import Path

from saklob.config.build import (
    FREE_FORM_INPUT_LENGTH,
    MIN_FREE_FORM_INPUT_LENGTH,
    MAX_FREE_FORM_INPUT_LENGTH,
)


class Kumpigurasyon:
    def __init__(self, path=None):
        if path is None:
            path = Path("saklob.json")

        self.path = Path(path)

        self.panimula_free_form_input_length = (
            FREE_FORM_INPUT_LENGTH
        )

        self.tumatakbo_free_form_input_length = (
            FREE_FORM_INPUT_LENGTH
        )

    def valid_free_form_input_length(self, haba):
        return (
            MIN_FREE_FORM_INPUT_LENGTH
            <= haba
            <= MAX_FREE_FORM_INPUT_LENGTH
        )

    def itakda_panimula_free_form_input_length(
        self,
        haba
    ):
        if not self.valid_free_form_input_length(haba):
            raise ValueError(
                "FREE_FORM_INPUT_LENGTH ay wala sa "
                "pinapahintulutang saklaw."
            )

        self.panimula_free_form_input_length = haba

    def simulan(self):
        self.tumatakbo_free_form_input_length = (
            self.panimula_free_form_input_length
        )

    def kunin_tumatakbo_free_form_input_length(self):
        return self.tumatakbo_free_form_input_length

    def kunin_panimula_free_form_input_length(self):
        return self.panimula_free_form_input_length

    def kunin_nakasulat_free_form_input_length(self):
        if not self.path.exists():
            return None

        data = json.loads(
            self.path.read_text(
                encoding="utf-8"
            )
        )

        return data.get(
            "free_form_input_length"
        )

    def ilagak(self):
        data = {
            "free_form_input_length":
                self.panimula_free_form_input_length
        }

        self.path.write_text(
            json.dumps(
                data,
                indent=4
            ),
            encoding="utf-8"
        )

    def ikarga(self):
        if not self.path.exists():
            return

        data = json.loads(
            self.path.read_text(
                encoding="utf-8"
            )
        )

        haba = data.get(
            "free_form_input_length"
        )

        if haba is None:
            return

        self.itakda_panimula_free_form_input_length(
            haba
        )