from datetime import datetime
from typing import Counter


class SimpleReport:
    dadosEmp = list()

    @staticmethod
    def generate(lista):
        dataAtual = datetime.today()
        listaDataAntiga = list()
        listaDataValidade = list()
        maiorEmpresa = list()
        for itens in lista:
            listaDataAntiga.append(itens['data_de_fabricacao'])

            dataValidadeAtual = itens['data_de_validade']
            if (datetime.strptime(dataValidadeAtual, "%Y-%m-%d") > dataAtual):
                listaDataValidade.append(dataValidadeAtual)

            maiorEmpresa.append(itens['nome_da_empresa'])

        dataAntiga = min(listaDataAntiga)
        dataValidade = min(listaDataValidade)
        SimpleReport.dadosEmp = Counter(maiorEmpresa)
        nomeMaiorEmpresa = (SimpleReport.dadosEmp).most_common(1)
        report = f'Data de fabricação mais antiga: {dataAntiga}'
        report += f'\nData de validade mais próxima: {dataValidade}'
        report += f'\nEmpresa com maior quantidade de produtos estocados: {nomeMaiorEmpresa[0][0]}\n'
        return report
