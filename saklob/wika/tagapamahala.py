from saklob.wika.bokabularyo import Bokabularyo

from saklob.wika.resources.filipino import utos as filipino_utos
from saklob.wika.resources.filipino import mensahe as filipino_mensahe

from saklob.wika.resources.english import utos as english_utos
from saklob.wika.resources.english import mensahe as english_mensahe

from saklob.wika.resources.cebuano import utos as cebuano_utos
from saklob.wika.resources.cebuano import mensahe as cebuano_mensahe


MGA_RESOURCE = {
    "filipino": {
        "utos": filipino_utos,
        "mensahe": filipino_mensahe,
    },
    "english": {
        "utos": english_utos,
        "mensahe": english_mensahe,
    },
    "cebuano": {
        "utos": cebuano_utos,
        "mensahe": cebuano_mensahe,
    },
}


class TagapamahalaWika:
    def __init__(self, locale):
        if locale not in MGA_RESOURCE:
            raise ValueError(
                f"Unsupported locale: {locale}"
            )

        self.locale = locale
        self.resource = MGA_RESOURCE[locale]

        self.fallback = MGA_RESOURCE["filipino"]

    def buuin_bokabularyo(self):
        bokabularyo = Bokabularyo()

        mga_utos = self.fallback["utos"].MGA_UTOS.copy()
        mga_utos.update(
            self.resource["utos"].MGA_UTOS
        )

        for command_id, metadata in mga_utos.items():
            bokabularyo.idagdag(
                metadata["name"],
                command_id
            )

        return bokabularyo

    def kunin_utos(self, command_id):
        metadata = self.resource["utos"].MGA_UTOS.get(
            command_id
        )

        if metadata is not None:
            return metadata

        return self.fallback["utos"].MGA_UTOS.get(
            command_id
        )

    def kunin_mensahe(self, susi):
        mensahe = self.resource["mensahe"].MGA_MENSAHE.get(
            susi
        )

        if mensahe is not None:
            return mensahe

        return self.fallback["mensahe"].MGA_MENSAHE.get(
            susi
        )

    def suportado(self):
        return self.locale in MGA_RESOURCE