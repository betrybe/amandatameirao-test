from os import stat
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:
    @staticmethod
    def import_data(arquivo, tipoRelatorio):
        tipoArquivo = arquivo.split('.')[1].lower()
        if tipoArquivo == 'xml':
            inst = XmlImporter();
        elif tipoArquivo == 'json':
            inst = JsonImporter();
        elif tipoArquivo == 'csv':
            inst = CsvImporter();
        else:
            tipoArquivo = ''

        if tipoArquivo:
            try:
                lista = inst.import_data(arquivo)
                if tipoRelatorio == 'completo':
                    print(CompleteReport.generate(lista))
                else:
                    print(SimpleReport.generate(lista))

            except:
                print('Arquivo invalido.') 

        else:
            print('Extensao invalida. Os tipos de arquivos permitidos sao: csv, json e xml.')
