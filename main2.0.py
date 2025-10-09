import random
import json
import os


#Funções de procura
def encontraruser():
    if os.path.exists('users.json'):
        with ('users.json', 'r') as usuarios:
            users = json.load(usuarios)
    else:
        users = []
    return users


def econtrarcamp():
    if os.path.exists('campeonatos.json'):
        with ('campeonatos.json', 'r') as camps:
            campeonatos = json.load(camps)
    else:
        campeonatos = []
    return campeonatos


def p():
    """
    Função utilizada para um retorno mais
    rápido ao menu, para economizar mais tempo
    e deixar mais organizado o código fonte.
    """
    a =input('Dê enter para voltar ao menu principal\n\n')
    menuprincipal()


def sub01():
    """
     Cadastro de usuárias na instalação
     recebe nome, data de nasc, altura e peso
     além de criar um rm aleatório unico
    """
    m = input('\nBem vindo ao submenu 1\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
    if m.upper() == 'SAIR':
        menuprincipal()
    else:
        users = encontraruser()
        while True:
            nome = input('Diga o nome da usuária a ser cadastrada\n')
            data = input('Diga a data de nascimento em formato AAAA-MM-DD \nEX:(1980-01-17)')
            entrada = input('Diga o dia de entrada em formato AAAA-MM-DD \nEX:(2007-02-18)')
            time = input('Diga o time da usuária\nEX: (Kansas City)')
            numero = input('Diga o número da camisa da usuária\nEX: (10)')
            posicao = input('Diga a posição da jogadora\nEX: (Zagueira)')
            b = input('Tem certeza que os dados estão corretos?\nCaso não, digita "Recomeçar" para reiniciar os dados a serem colocados\nCaso sim, apenas dê enter\n')
            if not b.upper() == 'RECOMEÇAR':
                while True:
                    usuarios = users['users']
                    regis = str(random.randint(100000000,999999999))
                    regis = '123456789'
                    for i in usuarios:
                        if i["RM"] == regis:
                            x = 1
                    if x == 1:
                        print('Você vai morrer')
                        break
                        
                    




def sub02():
    """
    Leitura de todas as usuárias
    :return:
    """
    m = input('\nBem vindo ao submenu 2\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
    if m.upper() == 'SAIR':
        menuprincipal()
    else:
        users = encontraruser()
        for i in users.items():
            print(i)
        p()

# def sub03():
#     """
#     Leitura de uma usuária em especifico
#     """
#     m = input('\nBem vindo ao submenu 3\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
#     if m.upper() == 'SAIR':
#         menuprincipal()
#     else:
#         users = encontraruser()
#         a = int(input('\nDiga o resgitro da usuária\n'))
#         if a in users.keys():
#             print(users[a])
#             p()
#         else:
#             print('\nA usuária não se encontra no registro.\n')
#             p()

# def sub04():
#     """
#     Alteração de dados de uma usuária em específico
#     no caso de erros no cadastro
#     """
#     m = input('\nBem vindo ao submenu 4\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
#     if m.upper() == 'SAIR':
#         menuprincipal()
#     else:
#         a = int(input('Diga o número de registro da usuária\n'))
#         if a in users.keys():
#             b = input('Diga que dado deseja alterar (Nome, Data, Altura, Peso)\nEx:Altura / ALTURA / altura\nCaso não colocar nenhum dos tipos de dados citados ou escrever algo errado, consideraremos que não quer trocar nada e irá voltar ao menu principal\n')

#             if b.upper() == 'NOME':
#                 nome = input(f'Digite o nome que deseja colocar no lugar (Nome anterior: {(users.get(a)).get('Nome:')})\n')
#                 users[a].update({'Nome:': nome})

#             elif b.upper() == 'DATA':
#                 data = input(f'Diga a data de nascimento que deseja modificar como dd/mm/aaa (Data anterior: {(users.get(a)).get('Data:')})\n')
#                 users[a].update({'Data:': data})

#             elif b.upper() == 'ALTURA':
#                 alt = float(input(f'Digite aqui qual valor você quer colocar no lugar da altura antertior ({(users.get(a)).get('Altura:')}m²)\n'))
#                 users[a].update({'Altura:': alt})

#             elif b.upper() == 'PESO':
#                 peso = float(input(f'Digite aqui qual valor você quer colocar no lugar do peso antertior ({(users.get(a)).get('Peso:')}kg)\n'))
#                 users[a].update({'Peso:': peso})
#             else:
#                 p()
#             print(users[a])
#             p()
#         else:
#             print('Este número de registro não está na listagem, tem certeza que essa pessoa existe?\nSe sim, tente volte ao menu principal, use a opção 3 e coloque o número de registro para ver se esse usuário realmente existe')
#             p()

# def sub05():
#     """
#     Cadastro de cameponato
#     recebe uma identidade prórpia
#     pode ser número ou títulos
#     """
#     m = input(
#         '\nBem vindo ao submenu 5\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
#     if m.upper() == 'SAIR':
#         menuprincipal()
#     else:
#         a = input('Digite qual a identificação do campeonato')
#         if not a in campeonatos.keys():
#             vencedor = 'Indefinido'
#             gol1 = 0
#             gol2 = 0
#             nome = input('Diga o nome do campeonato a ser cadastrado\n')
#             data = input('Diga a data de nascimento da usuária em formato DD/MM/AAAA\n')
#             hora = input('Diga o horário do campeonato em formato HH:MM\n(Exemplo: 17:52)\n')
#             time1 = input('Diga o nome do primeiro time\n')
#             time2 = input('Diga o nome do segundo time\n')
#             estado = input('Digite 1 caso o campeonato já está terminado\nDigite 2 caso o campeonato ainda está em aguardo\nDigite 3 caso o campeonato irá acontecer hoje\n')
#             if estado == '1':
#                 estado = 'Terminado'
#                 gol1 = int(input('Digite quantos gols o primeiro time fez\n'))
#                 gol2 = int(input('Digite quantos gols o segundo time fez\n'))
#                 if gol1 > gol2:
#                     vencedor = time1
#                 elif gol2 == gol1:
#                     vencedor = 'Empate'
#                 else:
#                     vencedor = time2
#             elif estado == '2':
#                 estado = 'Em aguardo'
#             elif estado == '3':
#                 estado = 'Acontecerá hoje'
#             else:
#                 estado = 'Em aguardo'
#                 print('Como não foi colocado nenhum valor tratável, foi colocado como "Em aguardo"\nCaso queira modificar isso, utilize o submenu 7 para modificar o estado do campeonato.')
#             b = input(
#                 'Tem certeza que os dados estão corretos?\nCaso não, digita "Recomeçar" para reiniciar os dados a serem colocados\nCaso sim, apenas dê enter\n')
#             if not b.upper() == 'RECOMEÇAR':
#                 if nome not in campeonatos.keys():
#                     placar = f'{gol1}X{gol2}'
#                     campeonatos[a] = {'Nome:': nome, 'Data:': data, 'Horário:': hora, 'Time1:': time1,'Time2:': time2,'Placar:':placar,'Vencedor:': vencedor, 'Estado:': estado}
#                     print(campeonatos[a])
#                     print(f'Identificação do campeonato: {a}\n')
#                     p()
#         else:
#             print('Este campeonato já está registrado.')
#             p()

# #    'Campeonato Edição N01':{'Dia:':'19/09/2025','Horário:':'12:00','Time1:':'Time X1','Time2:':'Time Y1','Placar':'','Vencedor:':'','Estado':'Em aguardo'},




# def sub06():
#     """
#     Procurar um campeonato em específico por
#     sua identidade
#     """
#     m = input(
#         '\nBem vindo ao submenu 6\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
#     if m.upper() == 'SAIR':
#         menuprincipal()
#     else:
#         a = input('Digite o nome do campeonato\n')
#         if a in campeonatos.keys():
#             print(campeonatos[a])
#             p()
#         else:
#             print('Este campeonato não existe.')
#             p()

# def sub07():
#     """
#     Modificar um dado específico de um campeonato
#     para casos de mudanças de planos ou correção de erro
#     """
#     m = input(
#         '\nBem vindo ao submenu 7\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
#     if m.upper() == 'SAIR':
#         menuprincipal()
#     else:
#         a = input('Digite o número do campeonato\n')
#         if a in campeonatos.keys():
#             b = input('Digite o dado que deseja modificar\n(Dados modificáveis: NOME, DIA, HORÁRIO, TIME1, TIME2, PLACAR, ESTADO)\n')
#             if b.upper() == 'NOME':
#                 c = input(f'Digite o novo nome do campeonato\n(Nome anterior:{(campeonatos.get(a)).get("Nome:")})')
#                 campeonatos[a].update({'Nome:': c})
#             elif b.upper() == 'DIA':
#                 c = input(f'Digite a nova data do campeonato em formato DD/MM/AAAA\n(Data anterior:{(campeonatos.get(a)).get("Data:")})')
#                 campeonatos[a].update({'Data:': c})
#             elif b.upper() == 'TIME1':
#                 c = input(f'Digite o novo time 1 do campeonato\n(Time1 anterior:{(campeonatos.get(a)).get("Time1:")})')
#                 campeonatos[a].update({'Time1:': c})
#             elif b.upper() == 'TIME2':
#                 c = input(f'Digite o novo time 2 do campeonato\n(Time2 anterior:{(campeonatos.get(a)).get("Time2:")})')
#                 campeonatos[a].update({'Time2:': c})
#             elif b.upper() == 'PLACAR':
#                 print(f'Placar anterior: {(campeonatos.get(a)).get("Placar:")}')
#                 c1 = int(input('Quantos gols o time 1 tem?'))
#                 c2 = int(input('Quantos gols o time 2 tem?'))
#                 d = f'{c1}x{c2}'
#                 if c1 > c2:
#                     vencedor = (campeonatos.get(a)).get("Time1:")
#                 elif c2 == c1:
#                     vencedor = 'Empate'
#                 else:
#                     vencedor = (campeonatos.get(a)).get("Time2:")
#                 campeonatos[a].update({'Placar:': d})
#                 campeonatos[a].update({'Vencedor:': vencedor})
#             elif b.upper() == 'ESTADO':
#                 c = input(f'Digite o novo nome do campeonato\n(Estado anterior:{(campeonatos.get(a)).get("Estado:")})')
#                 campeonatos[a].update({'Estado:': c})
#             elif b.upper() == 'HORÁRIO' or b.upper()=='HORARIO':
#                 c = input(f'Digite o novo nome do campeonato\n(Horário anterior:{(campeonatos.get(a)).get("Horário:")})')
#                 campeonatos[a].update({'Horário:': c})
#             else:
#                 print('Aparentemente você errou o tipo de dado que quer modificar, tente novamente.')
#             p()
#         else:
#             print('Esse campeonato não existe pelos nossos dados\nOu talvez você errou seu número, verifique no submenu 6 ou 10')
#             p()




# def sub08():
#     """
#     Deleção de um campeonato.
#     """
#     m = input(
#         '\nBem vindo ao submenu 7\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
#     if m.upper() == 'SAIR':
#         menuprincipal()
#     else:
#         a = input('Diga o número de identificação do campeonato')
#         if a in campeonatos.keys():
#             b = input('Deseja mesmo DELETAR o campeonato?\nDigitar "Deletar" caso sim')
#             if b.upper() == 'DELETAR':
#                 campeonatos.pop(a)
#                 print('Campeonato deletado')
#                 p()
#             else:
#                 print('Operação cancelada, voltando ao menu principal')
#                 p()
#         else:
#             print('Esse campeonato não existe, tente ver no submenu 6 ou 10')
#             p()


# def sub09():
#     """
#     Deleção de uma usuária
#     """
#     m = input(
#         '\nBem vindo ao submenu 9\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
#     if m.upper() == 'SAIR':
#         menuprincipal()
#     else:
#         a = int(input('Diga o número de registro da jogadora a ser deletada'))
#         if a in users.keys():
#             print(users.get(a))
#             b = input('Deseja mesmo DELETAR essa usuária?\nDigitar "Deletar" caso sim')
#             if b.upper() == 'DELETAR':
#                 users.pop(a)
#                 print('Usuária deletada, voltando ao menu principal')
#                 p()
#             else:
#                 print('Operação cancelada, voltando ao menu principal')
#         else:
#             print('Usuária não se encontra no sistema, tente ver se ela existe mesmo no submenu 2 ou 3')
#             p()





# def sub10():
#     """
#     Procura por todos os campeonatos alistados
#     """
#     m = input(
#         '\nBem vindo ao submenu 10\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
#     if m.upper() == 'SAIR':
#         menuprincipal()
#     else:
#         for i in campeonatos.items():
#             print(i)
#         p()



def menuprincipal():
    while True:
        print('Bem vindo(a) ao menu principal')
        print('1 - Cadastrar usuário')
        print('2 - Verificar todos os cadastros atuais')
        print('3 - Verificar um usuário pelo número de registro')
        print('4 - Modificar um dado em especifico de um usuário')
        print('5 - Cadastrar campeonato')
        print('6 - Verificar informações  de um campeonato em específico')
        print('7 - Modificar informações de um campeonato em específico')
        print('8 - Deletar campeonato')
        print('9 - Deletar usuário')
        print('10 - Ver todos os Campeonatos')
        print('11 - Sair')
        a = int(input('Digite o número do submenu que deseja acessar\n\n'))
        if a==1:
            sub01()
#         elif a==2:
#             sub02()
#         elif a == 3:
#             sub03()
#         elif a == 4:
#             sub04()
#         elif a == 5:
#             sub05()
#         elif a == 6:
#             sub06()
#         elif a == 7:
#             sub07()
#         elif a == 8:
#             sub08()
#         elif a == 9:
#             sub09()
#         elif a == 10:
#             sub10()
#         elif a== 11:
#             break
#         else:
#             print('Tente novamente')





menuprincipal()
