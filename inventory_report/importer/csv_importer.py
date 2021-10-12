import pandas as pd
from inventory_report.importer.importer import Importer

class CsvImporter(Importer):
    @staticmethod
    def import_data(arquivo):
        tipoArquivo = arquivo.split('.')[1].lower()
        extensao = 'csv'
        try:
            if tipoArquivo != extensao:
                raise ValueError('Arquivo inválido')
            else:
                li = list()
                with open(arquivo, 'r') as file:
                    dados = pd.read_csv(arquivo, delimiter=',')
                    li = dados.to_dict('records')
        except:
             print('Arquivo inválido')
        else:
            file.close()
            return li
