from saklob.wika.bokabularyo import Bokabularyo

from saklob.wika.resources.filipino import utos as filipino_utos
from saklob.wika.resources.filipino import mensahe as filipino_mensahe

from saklob.wika.resources.english import utos as english_utos
from saklob.wika.resources.english import mensahe as english_mensahe

from saklob.wika.resources.cebuano import utos as cebuano_utos
from saklob.wika.resources.cebuano import mensahe as cebuano_mensahe


class TagapamahalaWika:
    def __init__(self, locale):
        self.locale = locale

    def buuin_bokabularyo(self):
        bokabularyo = Bokabularyo()

        self._kunin_utos_module().irehistro(
            bokabularyo
        )

        return bokabularyo

    def kunin_utos(self, command_id):
        return self._kunin_utos_module().kunin_utos(
            command_id
        )

    def kunin_mensahe(self, susi):
        return self._kunin_mensahe_module().MGA_MENSAHE.get(
            susi
        )

    def _kunin_utos_module(self):
        if self.locale == "filipino":
            return filipino_utos

        if self.locale == "english":
            return english_utos

        if self.locale == "cebuano":
            return cebuano_utos

        raise ValueError(
            f"Hindi suportadong locale: {self.locale}"
        )

    def _kunin_mensahe_module(self):
        if self.locale == "filipino":
            return filipino_mensahe

        if self.locale == "english":
            return english_mensahe

        if self.locale == "cebuano":
            return cebuano_mensahe

        raise ValueError(
            f"Hindi suportadong locale: {self.locale}"
        )

    def suportado(self):
        return self.locale in {
            "filipino",
            "english",
            "cebuano",
        }