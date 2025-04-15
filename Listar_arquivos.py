import os
import csv

class ListarArquivos:
    def __init__(self, diretorio, exportar_csv=False, nome_arquivo='lista_arquivos.csv'):
        self.diretorio = diretorio
        self.exportar_csv = exportar_csv
        self.nome_arquivo = nome_arquivo

    def listar(self):
        arquivos = []
        try:
            with os.scandir(self.diretorio) as entradas:
                for entrada in entradas:
                    if entrada.is_file() and not os.path.islink(entrada.path):
                        arquivos.append([entrada.name, entrada.path])
                        print(f"Arquivo: {entrada.name}")
        except OSError as e:
            print(f"Erro ao acessar o diretório: {e}")

        if self.exportar_csv and arquivos:
            self.exportar_para_csv(arquivos)

    def exportar_para_csv(self, dados):
        try:
            with open(self.nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
                escritor = csv.writer(arquivo_csv)
                escritor.writerow(['Nome do Arquivo', 'Caminho Completo'])
                escritor.writerows(dados)
            print(f"\n✅ Lista exportada com sucesso para: {self.nome_arquivo}")
        except Exception as e:
            print(f"Erro ao exportar para CSV: {e}")

# Executar
if __name__ == '__main__':
    diretorio_atual = os.getcwd()
    listador = ListarArquivos(diretorio=diretorio_atual, exportar_csv=True)
    listador.listar()
