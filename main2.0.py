import datetime
import random
from datetime import date
import json
import os

from pyarrow import nulls


#Funções de procura
def encontraruser():
    if os.path.exists('users.json'):
        with open('users.json', 'r') as usuarios:
            users = json.load(usuarios)
    else:
        users = []
    return users

def escritauser(user):
    dici = encontraruser()
    users = dici["users"]
    print(users)
    users.append(user)
    with open('users.json', 'w') as usus:
        json.dump(dici, usus, indent=2)


def econtrarcamp():
    if os.path.exists('campeonatos.json'):
        with ('campeonatos.json', 'r') as camps:
            campeonatos = json.load(camps)
    else:
        campeonatos = []
    return campeonatos

def escritacamp(camp):
    dici = encontraruser()
    camps = dici["campeonatos"]
    print(camps)
    camps.append(camp)
    with open('camps.json', 'w') as campus:
        json.dump(dici, campus, indent=2)



def p():
    """
    Função utilizada para um retorno mais
    rápido ao menu, para economizar mais tempo
    e deixar mais organizado o código fonte.
    """
    a =input('\nDê enter para voltar ao menu principal\n\n')




def sub01():
    """
     Cadastro de usuárias na instalação
     recebe nome, data de nasc, altura e peso
     além de criar um rm aleatório unico
    """
    m = input('\nBem vindo ao submenu 1\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
    if m.upper() == 'SAIR':
        pass
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
                existe = False
                while True:
                    usuarios = users["users"]
                    regis = str(random.randint(100000,999999))
                    for i in usuarios:
                        if i["RM"] == regis:
                            existe = True
                    if not existe:
                        print('Você vai morrer')
                        break
                usuaria = {"nome": nome,
                  "data_nascimento": data,
                  "dia_entrada": entrada,
                  "RM": regis,
                  "time": time,
                  "numero_camisa": numero,
                  "posicao": posicao
                }
                print(usuaria)
                escritauser(usuaria)
            p()
            break

                        
                    




def sub02():
    """
    Leitura de todas as usuárias
    :return:
    """
    m = input('\nBem vindo ao submenu 2\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
    if m.upper() == 'SAIR':
        pass
    else:
        dici = encontraruser()
        users = dici["users"]
        for i in users:
            print(f"Nome: {i["nome"]}\nRM:{i["RM"]}\nData de Nascimento: {i["data_nascimento"]}\nDia de entrada: {i["dia_entrada"]}\nTime: {i["time"]}\nNúmero: {i["numero_camisa"]}\nPosição: {i["posicao"]}")
            print("\n###################################################\n")
        p()


def sub03():
    """
    Leitura de uma usuária em especifico
    """
    m = input('\nBem vindo ao submenu 3\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
    if m.upper() == 'SAIR':
        menuprincipal()
    else:
        dici = encontraruser()
        users = dici["users"]
        a = input('\nDiga o resgitro da usuária\n')
        exis = False
        for i in  users:
            if i["RM"]==a:
                print(f"Nome: {i["nome"]}\nRM:{i["RM"]}\nData de Nascimento: {i["data_nascimento"]}\nDia de entrada: {i["dia_entrada"]}\nTime: {i["time"]}\nNúmero: {i["numero_camisa"]}\nPosição: {i["posicao"]}")
                exis = True
        if not exis:
            print('\nA usuária não se encontra no registro.\n')
        p()

def sub04():
    """
    Alteração de dados de uma usuária em específico
    no caso de erros no cadastro
    """
    m = input('\nBem vindo ao submenu 4\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
    if m.upper() == 'SAIR':
        pass
    else:
        dici = encontraruser()
        users = dici["users"]
        existe = False
        a = input('Diga o número de registro (RM) da usuária\n')
        for i in  users:
            if a==i["RM"]:
                existe = True
                user = i
                break
        if existe:
            anterior = user
            b = input('Diga que dado deseja alterar \n(Números correspondentes aos dados: \n1 - Nome\n2 - Data de nascimento\n3 - Data de entrada\n4 - Time\n5 - Numero\n6 - Posição\nExemplos: Se o número de entrada for 1, você irá mudar o nome do user, se for 4, você irá mudar o time do user\nCaso não colocar nenhum dos tipos de dados citados ou escrever algo errado, consideraremos que não quer trocar nada e irá voltar ao menu principal\n')

            if b=="1":
                print(f"Nome atual: {user["nome"]}")
                c = input("Que nome novo deseja colocar no lugar?")
                user["nome"]=c
                print(f'Nome atualizado para {c}')
                dici["users"].remove(anterior)
                dici["users"].append(user)
                with open('users.json', 'w') as usus:
                    json.dump(dici, usus, indent=2)

            elif b == "2":
                print(f"Data de nascimento atual: {user["data_nascimento"]}")
                c = input("Que data de nascimento novo deseja colocar no lugar?\n(Em formato AAAA-MM-DD\nEx: 2000-01-17)")
                user["data_nascimento"] = c
                print(f'Data de nascimento atualizada para {c}')
                dici["users"].remove(anterior)
                dici["users"].append(user)
                with open('users.json', 'w') as usus:
                    json.dump(dici, usus, indent=2)

            elif b == "3":
                print(f"Data de entrada atual: {user["dia_entrada"]}")
                c = input("Que data de entrada nova deseja colocar no lugar?\n(Em formato AAAA-MM-DD\nEx: 2025-10-24)")
                user["dia_entrada"] = c
                print(f'Data de entrada atualizada para {c}')
                dici["users"].remove(anterior)
                dici["users"].append(user)
                with open('users.json', 'w') as usus:
                    json.dump(dici, usus, indent=2)

            elif b == "4":
                print(f"Time atual: {user["time"]}")
                c = input("Que time novo deseja colocar no lugar?")
                user["time"] = c
                print(f'Time atualizado para {c}')
                dici["users"].remove(anterior)
                dici["users"].append(user)
                with open('users.json', 'w') as usus:
                    json.dump(dici, usus, indent=2)

            elif b == "5":
                print(f"Camisa atual: {user["numero_camisa"]}")
                c = input("Que número de camisa novo deseja colocar no lugar?")
                user["numero_camisa"] = c
                print(f'Numero de camisa atualizado para {c}')
                dici["users"].remove(anterior)
                dici["users"].append(user)
                with open('users.json', 'w') as usus:
                    json.dump(dici, usus, indent=2)

            elif b == "6":
                print(f"Posição atual: {user["posicao"]}")
                c = input("Que posição nova deseja colocar no lugar?")
                user["posicao"] = c
                print(f'Posição atualizada para {c}')
                dici["users"].remove(anterior)
                dici["users"].append(user)
                with open('users.json', 'w') as usus:
                    json.dump(dici, usus, indent=2)

            else:
                p()

        else:
            print('Este número de registro não está na listagem, tem certeza que essa pessoa existe?\nSe sim, use a opção 3 do menu principal e coloque o número de registro para ver se esse usuário realmente existe')
            p()

def sub05():
    """
    Cadastro de cameponato
    recebe uma identidade prórpia
    que pode ser apenas números
    """
    m = input(
        '\nBem vindo ao submenu 4\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
    if m.upper() == 'SAIR':
        pass
    else:
        while True:
            dici = econtrarcamp()
            nome = input('Qual é o nome do campeonato?\n')
            data1 = input('Digite a data do >>INICIO<< do campeonato em formato AAAA-MM-DD\nEx: 2025-10-30\n')
            data2 = input('Digite a data do >>FIM<< do campeonato em formato AAAA-MM-DD\nEx: 2025-10-31\n')
            datatual = date.today()
            try:
                if int(data1[-2:-1]) and int(data1[-5:-4]) and int(data1[0:3]) >= int(datatual[-2:-1]) and int(datatual[-5:-4]) and int(datatual[0:3]):
                    estado ='terminado'
                else:
                    estado = 'a ocorrer'
            except ValueError:
                print('Você provavelmente colocou algum valor na data final errado\nA data final será declarada como nula e o estado "a ocorrer", mude depois no submenu 7')
                estado = 'a ocorrer'
                data2 = None

            if estado == 'terminado':
                vencedor = input('Qual é o time vencedor?')
                try:
                    gol1 = int(input('Quantos gols o primeiro time fez?'))
                    gol2 = int(input('Quantos gols o segundo time fez?'))
                    arti = input('Qual é a artilheira?')
                    golsart = int(input('Quantos gols a artilheira fez no total?'))
                except ValueError:
                    print('Erro: Valores não inteiros colocados, consideraremos o nome da artilheira, gols da artilheira, gols do primeiro, segundo time como nulos.\nMude isso no submenu 7 depois, ou reinicie o cadastro de campeonato depois')
                    gol1 = None
                    gol2 = None
                    golsart = None
                    arti= None
            else:
                vencedor = None
                gol1 = None
                gol2 = None
                arti = 'Tem alguma artilheira definida?\nSe não, deixe esse espaço vazio e apenas dê enter\n'
                if arti=='':
                    golsart = None
                    arti = None
                else:
                    try:
                        golsart = int(input('Quantos gols a artilheira fez?'))
                    except ValueError:
                        print('Erro: Você não colocou um número inteiro, iremos considerar o valo como nulo, mude isso depois no subemenu 7')
                        golsart = None
                times = []
                while True:
                    time = input('Quais são os timpes participantes?\nDIGITE "SAIR" QUANTO NÃO TIVER MAIS TIMES PARA ADICIONAR\n')
                    if time.upper()=='SAIR':
                        break
                    times.append(time)

                campeo ={
                  "id": len(dici)+1,
                  "nome": nome,
                  "data_inicio": data1,
                  "data_fim": data2,
                  "time_vencedor": vencedor,
                  "placar_final": f'{gol1}-{gol2}',
                  "artilheira": arti,
                  "gols_artilheira": golsart,
                  "times_participantes": times,
                  "estado": estado
                }
                fim = input(f'As informações abaixo estão corretas?\nNome: {campeo['nome']}\nData de inicio: {campeo['data_inicio']}\nData de fim: {campeo['data_fim']}\nTime vencedor: {campeo['time_vencedor']}\nPlacar final: {campeo['placar_final']}\nArtilheira: {campeo['artilheira'].split(',')}\nGols da artilheira: {campeo['gols_artilheira']}\nTimes participantes: {campeo['times_participantes']}\nEstado: {campeo['estado']}\n\nCaso não, digite "RECOMEÇAR" para fazer outro')
                if fim.upper()== 'RECOMEÇAR':
                    pass
                else:
                    escritacamp(campeo)
                    print('Arquivo salvo!')
                    break











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
        elif a==2:
            sub02()
        elif a == 3:
            sub03()
        elif a == 4:
            sub04()
        elif a == 5:
            sub05()
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
