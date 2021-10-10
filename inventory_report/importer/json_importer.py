import json
from inventory_report.importer.importer import Importer

class JsonImporter(Importer):
    @staticmethod
    def import_data(caminho):
        extensao = 'json'
        tipoArquivo = caminho.split('.')[1].lower()
        try:
            if tipoArquivo != extensao:
                raise ValueError('Arquivo inválido')
            else:
                li = list()
                with open(caminho, 'r') as file:
                    li = json.load(file)
        except:
            return 'Arquivo inválido'

        else:
            file.close()
            return li
