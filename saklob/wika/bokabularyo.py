class Bokabularyo:
    def __init__(self):
        self._mga_salita = {}

    def idagdag(self, salita, command_id):
        self._mga_salita[salita] = command_id

    def kunin_id(self, salita):
        return self._mga_salita.get(salita)

    def mga_salita(self):
        return list(self._mga_salita.keys())