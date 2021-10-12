import sys
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

from inventory_report.inventory.inventory_refactor import InventoryRefactor

def main():
    if len(sys.argv) != 3:
        sys.stderr.write('Verifique os argumentos\n')
    else:
        try:
            arquivo = sys.argv[1]
            tipoRelatorio = sys.argv[2]
            tipoArquivo = arquivo.split('.')[1].lower()
            if tipoArquivo == 'xml':
                InventoryRefactor(XmlImporter).import_data(arquivo, tipoRelatorio)
            elif tipoArquivo == 'csv':
                InventoryRefactor(CsvImporter).import_data(arquivo, tipoRelatorio)
            elif tipoArquivo == 'json':
                InventoryRefactor(JsonImporter).import_data(arquivo, tipoRelatorio)
            else:
                raise ValueError("Arquivo inválido")
        except:
            assert 'Arquivo inválido'


if __name__ == '__main__':
    main()
