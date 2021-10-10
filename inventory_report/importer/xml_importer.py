import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer

class XmlImporter(Importer):
    @staticmethod
    def import_data(arquivo):
        tipoArquivo = arquivo.split('.')[1].lower()
        extensao = 'xml'
        try:
            if tipoArquivo != extensao:
                raise ValueError('Arquivo inválido')
            else:
                li = list()
                with open(arquivo, 'r') as file:
                    dicionario = dict()
                    dados = ET.parse(file)
                    raiz = dados.getroot()
                    noRaiz = raiz.tag
                    noFilho = raiz[0].tag
                    for item in raiz.iter():
                        if item.tag == noFilho and dicionario:
                            li.append(dicionario.copy())
                            dicionario.clear()
                        elif noRaiz not in item.tag and noFilho not in item.tag:
                            dicionario[item.tag] = item.text

        except:
            return 'Arquivo inválido'
        else:
            file.close()
            return li
