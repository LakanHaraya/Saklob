class KontekstoRehistro:
    def __init__(self):
        self._mga_konteksto = {
            "saklob": []
        }

        self._mga_deskripsiyon = {}

    def mga_papasukan(self, konteksto):
        return self._mga_konteksto.get(konteksto, [])

    def idagdag(self, konteksto, mga_anak):
        self._mga_konteksto[konteksto] = list(mga_anak)

    def idagdag_anak(self, konteksto, anak):
        if konteksto not in self._mga_konteksto:
            self._mga_konteksto[konteksto] = []

        if anak not in self._mga_konteksto[konteksto]:
            self._mga_konteksto[konteksto].append(anak)

    def itakda_deskripsiyon(self, konteksto, deskripsiyon):
        self._mga_deskripsiyon[konteksto] = deskripsiyon

    def kunin_deskripsiyon(self, konteksto):
        return self._mga_deskripsiyon.get(konteksto)