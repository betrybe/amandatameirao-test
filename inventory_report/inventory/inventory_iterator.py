from collections.abc import Iterator

class InventoryIterator(Iterator):
    def __init__(self, colecao):
        self.colecao = colecao
        self.indice = 0

    def __next__(self):
        try:
            valor = self.colecao[self.indice]
            self.indice += 1
        except IndexError:
            raise StopIteration
        else:
            return valor
