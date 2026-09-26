class Utos:
    def __init__(
        self,
        id,
        handler,
        mga_konteksto=None,
        provider_tulong=None
    ):
        self.id = id
        self.handler = handler
        self.mga_konteksto = mga_konteksto
        self.provider_tulong = provider_tulong

    def magagamit_sa(self, konteksto):
        if self.mga_konteksto is None:
            return True

        return konteksto in self.mga_konteksto

    def isagawa(self, argumento=None):
        if argumento is None:
            argumento = []

        return self.handler(argumento)