#######################################################################
##                                                                   ##
##ESTE CÓDIGO TRATA ERROS DE INSERÇÃO DE LINHAS EM BANCO DE DADOS SQL##
##                                                                   ##
#######################################################################

linha_anterior = ''
lista = []
arquivo = "Caminho\do\Arquivo"
with open(arquivo) as texto:
    for linha in texto:
        if "ERROR" in linha:
            if linha_anterior != '':
                lista.append(linha_anterior)
        else:
            linha_anterior = linha
    for saida in lista:
        print(saida.rstrip('\n'))
