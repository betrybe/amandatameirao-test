from collections.abc import Iterable
from os import stat
from typing import Any, List

from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport

class InventoryRefactor(Iterable):
    def __init__(self, classe, colecao: List[Any] = []):
        self.importer = classe
        self.data = list()
        self.colecao = colecao

    def __iter__(self) -> InventoryIterator:
        return InventoryIterator(self.colecao)

    def import_data(self, caminho, tipoRelatorio):
        try:
            instancia = self.importer()
            self.data = instancia.import_data(caminho)
            if tipoRelatorio == 'completo':
                print(CompleteReport.generate(self.data))
            else:
                print(SimpleReport.generate(self.data))

        except:
            return 'Arquivo inválido'
