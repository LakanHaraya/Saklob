from saklob.utos.utos import Utos


class Rehistro:
    def __init__(self):
        self._ayon_sa_id = {}

    def idagdag(self, utos):
        self._ayon_sa_id[utos.id] = utos

    def kunin_id(self, id):
        return self._ayon_sa_id.get(id)

    def mga_id(self):
        return list(self._ayon_sa_id.keys())

    def mga_magagamit(self, konteksto, mode=None):
        return [
            utos
            for utos in self._ayon_sa_id.values()
            if (
                utos.magagamit_sa(konteksto)
                and utos.magagamit_sa_mode(mode)
            )
        ]