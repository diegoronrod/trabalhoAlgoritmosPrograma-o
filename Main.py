# Diego Roncatto e Rodrigo dos Santos

from Cidades import Cidades
from Estados import Estados
import csv


def valida_sigla():
    while True:
        sigla = input('Sigla: ').upper()
        if not sigla.isnumeric():
            return sigla
        else:
            print('\nA sigla deve constituida de duas letras.')


def valida_nomest():
    while True:
        nomeest = input('Estado: ').upper()
        if not nomeest.isnumeric():
            return nomeest
        else:
            print('\nNome inválido')


def valida_cid():
    while True:
        nome = input('Cidade: ').upper()
        if not nome.isnumeric():
            return nome
        else:
            print('\nNome inválido')


def escolhe_est():
    if len(lst_estado) > 0:
        while True:
            try:
                escolha = int(input('\nEstado: '))
                if 0 <= escolha < len(lst_estado):
                    estesc = lst_estado[escolha]
                    return estesc
                print('\nNão consta na lista.')
            except:
                print('\nDigite o indice.')
    return None


def escolherEstado():
    relatorio_estados2()
    estadoEscolha = int(input('\nQual Estado: '))
    estadoEscolhido = lst_estado[estadoEscolha]
    if estadoEscolhido in lst_estado:
        return estadoEscolhido


def atual_casos():
    relatorio_cidades2()
    esccid = int(input('\nCidade: '))
    cidesc = lst_cidade[esccid]
    qtnova = int(input('\nAtualizar número de casos: '))
    cidesc.atualiza(qtnova)


def set_qtest():
    qtest = int(0)
    return qtest


def set_qtcasos():
    qtcasos = int(0)
    return qtcasos


def cadastro_estados():
    print('\n*CADASTRAR ESTADO*\n')
    lst_estado.append(Estados(valida_nomest(), valida_sigla(), set_qtest()))
    input('\nEstado cadastrado. [ENTER]')


def cadastro_cidades():
    print('\n*CADASTRAR CIDADE*\n')
    lst_cidade.append(Cidades(valida_cid(), escolherEstado(), set_qtcasos()))
    input('\nCidade cadastrada. [ENTER]')


def relatorio_estados1():
    print('\n*ESTADOS CADASTRADOS*\n')
    for r, e in enumerate(lst_estado):
        print(str(r) + ' ... ' + str(e.get_nomeest()) + ' ... ' + str(e.get_sigla()) + ' ... ' + str(e.get_qtest()))
    input('\nRetorna ao menu. [ENTER]')


def relatorio_estados2():
    print('\n*ESTADOS CADASTRADOS*\n')
    for r, e in enumerate(lst_estado):
        print(str(r) + ' ... ' + str(e.get_nomeest()) + ' ... ' + str(e.get_sigla()) + ' ... ' + str(e.get_qtest()))


def relatorio_cidades1():
    print('\n*CIDADES CADASTRADAS*\n')
    for r, e in enumerate(lst_cidade):
        print(str(r) + ' ... ' + str(e.get_nome()) + ' ... Casos: ' + str(e.get_qtcasos()))
    input('\nRetorna ao menu. [ENTER]')


def relatorio_cidades2():
    print('\n*CIDADES CADASTRADAS*\n')
    for r, e in enumerate(lst_cidade):
        print(str(r) + ' ... ' + str(e.get_nome()) + ' ... Casos: ' + str(e.get_qtcasos()))


def atualizar_casos():
    print('\n*ATUALIZAR CASOS*\n')
    atual_casos()


def salvar_Arquivos():
    with open('Estado.csv', 'w', newline='') as arquivo:
        wr = csv.writer(arquivo)
        for Estado in lst_estado:
            wr.writerow([Estado.nomeest, Estado.sigla, Estado.qtest])

    # Salvar lista de Cidades ainda com problema,
    # Tem o obj Estado na segunda posição.

    with open('Cidade.csv', 'w', newline='') as arquivo:
        wr = csv.writer(arquivo)
        for Cidade in lst_cidade:
            wr.writerow([Cidade.nome, Cidade.estado.get_sigla, Cidade.qtcasos])

    input('\nArquivos salvos!! [ENTER]')


lst_estado = []
lst_cidade = []


with open('Estado.csv') as est:
    reader = csv.reader(est)
    for row in reader:
       lst_estado.append(Estados(row[0], row[1], int(row[2])))

with open('Cidade.csv') as cid:
    reader = csv.reader(cid)
    for row in reader:
       lst_cidade.append(Cidades(row[0], row[1], int(row[2])))




menu = '''
*******************************************************
* Registro de Casos de Covid-19 por Estados e Cidades *
*******************************************************

Menu

     1-	Cadastrar Estados
     2-	Cadastrar Cidades
     3-	Relatório de Estados
     4-	Relatório de Cidades
     5-	Atualizar números de casos
     6- Salvar Arquivos
     7-	Finalizar o Programa

     Escolha: '''

while True:
    escolha = input(menu)

    if escolha == '1':
        cadastro_estados()
    elif escolha == '2':
        cadastro_cidades()
    elif escolha == '3':
        relatorio_estados1()
    elif escolha == '4':
        relatorio_cidades1()
    elif escolha == '5':
        atualizar_casos()
    elif escolha == '6':
        salvar_Arquivos()
    elif escolha == '7':
        break
    else:
        input('\nOpção inválida.  [ENTER]')
