class FilaDeImpressao:
    _instancia = None
    def __init__(self):
        pass

    @classmethod
    def get_instancia(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia

   
    def adicionar_documento(self, documento):
        pass

    def imprimir(self):
        pass


fila = FilaDeImpressao.get_instancia()
fila.adicionar_documento("Documento 1")
fila.imprimir()

outra_fila = FilaDeImpressao.get_instancia()
print(fila is outra_fila) 
