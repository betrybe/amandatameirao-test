from inventory_report.reports.simple_report import SimpleReport


class CompleteReport():
    @staticmethod
    def generate(lista):
        report = SimpleReport.generate(lista) + '\n'
        report += 'Produtos estocados por empresa: \n'

        nomeEmpresa = list()
        nomeEmpresa = (SimpleReport.dadosEmp).most_common()
        for nome, qtde in nomeEmpresa:
            report += f'- {nome}: {qtde}\n'

        return report
