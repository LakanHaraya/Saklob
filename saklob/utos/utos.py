class Utos:
    def __init__(
        self,
        id,
        handler,
        mga_konteksto=None,
        mga_mode=None,
        provider_tulong=None,
        malayang_input=False,
        kailangan_magulang=False
    ):
        self.id = id
        self.handler = handler
        self.mga_konteksto = mga_konteksto
        self.mga_mode = mga_mode
        self.provider_tulong = provider_tulong
        self.malayang_input = malayang_input
        self.kailangan_magulang = kailangan_magulang

    def magagamit_sa(self, konteksto):
        if self.mga_konteksto is None:
            return True

        return konteksto in self.mga_konteksto

    def magagamit_sa_mode(self, mode):
        if self.mga_mode is None:
            return True

        return mode in self.mga_mode

    def isagawa(self, argumento=None):
        if argumento is None:
            argumento = []

        return self.handler(argumento)