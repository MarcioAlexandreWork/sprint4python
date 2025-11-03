import datetime
import random
from datetime import date
import json
import os

from nltk.sem.chat80 import items
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
    if os.path.exists('camps.json'):
        with open('camps.json', 'r') as camps:
            campeonatos = json.load(camps)
    else:
        campeonatos = {'campeonatos':[]}
    return campeonatos

def escritacamp(camp):
    dici = econtrarcamp()
    dici['campeonatos'].append(camp)
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
        '\nBem vindo ao submenu 5\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
    if m.upper() == 'SAIR':
        pass
    else:
        while True:
            dici = econtrarcamp()
            nome = input('Qual é o nome do campeonato?\n')
            data1 = input('Digite a data do >>INICIO<< do campeonato em formato AAAA-MM-DD\nEx: 2025-10-30\n')
            data2 = input('Digite a data do >>FIM<< do campeonato em formato AAAA-MM-DD\nEx: 2025-10-31\n')
            datatual = str(date.today())
            if data1=='' or data2=='':
                print(
                    'Você provavelmente colocou algum valor na data final errado\nA data final e inicial serão declaradas como nula e o estado "a ocorrer", mude depois no submenu 7')
                estado = 'a ocorrer'
                data1 = None
                data2 = None
            elif not datatual<data2:
                estado ='terminado'
            else:
                estado = 'a ocorrer'

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
                arti = input('Tem alguma artilheira definida?\nSe não, deixe esse espaço vazio e apenas dê enter\n')
                if arti=='':
                    golsart = None
                    arti = None
                else:
                    try:
                        golsart = int(input('Quantos gols a artilheira fez?'))
                    except ValueError:
                        print('Erro: Você não colocou um número inteiro, iremos considerar o valo como nulo, mude isso depois no subemenu 7')
                        golsart = None
            times1 = []
            while True:
                time = input('Quais são os timpes participantes?\nDIGITE "SAIR" QUANTO NÃO TIVER MAIS TIMES PARA ADICIONAR\n')
                if time.upper()=='SAIR':
                    if not len(times1)==1:
                        break
                    else:
                        print('Por favor, coloque mais de um time')
                times1.append(time)
            times2 = ''
            for i in times1:
                times2+=i+', '
            campeo ={
              "id": len(dici['campeonatos'])+1,
              "nome": nome,
              "data_inicio": data1,
              "data_fim": data2,
              "time_vencedor": vencedor,
              "placar_final": f'{gol1}-{gol2}',
              "artilheira": arti,
              "gols_artilheira": golsart,
              "times_participantes": times1,
              "estado": estado
            }
            print(times2)
            fim = input(f'As informações abaixo estão corretas?\nNome: {campeo['nome']}\nData de inicio: {campeo['data_inicio']}\nData de fim: {campeo['data_fim']}\nTime vencedor: {campeo['time_vencedor']}\nPlacar final: {campeo['placar_final']}\nArtilheira: {campeo['artilheira']}\nGols da artilheira: {campeo['gols_artilheira']}\nTimes participantes: {(times2[0:-2])+'.'}\nEstado: {campeo['estado']}\n\nCaso não, digite "RECOMEÇAR" para fazer outro')
            if fim.upper()== 'RECOMEÇAR':
                pass
            else:
                print(f'Arquivo salvo!\nID do campeonato: {campeo['id']}')
                print(dici)
                escritacamp(campeo)
                print('Arquivo salvo!')
                break
    p()


def sub06():
    """
    Procurar um campeonato em específico por
    sua identidade
    """
    m = input(
        '\nBem vindo ao submenu 6\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
    if m.upper() == 'SAIR':
        pass
    else:
        dici = econtrarcamp()
        camps = dici['campeonatos']
        try:
            a = int(input('Digite o ID do campeonato\n'))
            achou = False
            for i in camps:
                if i['id']==a:
                    achou = True
                    campeo = i
                    break
            if not achou:
                print('Esse campeonato não existe, se quer ter certeza que ele existe, então utilize o submenu 10')
            else:
                print(f'\nID: {campeo['id']}\nNome: {campeo['nome']}\nData de inicio: {campeo['data_inicio']}\nData de fim: {campeo['data_fim']}\nTime vencedor: {campeo['time_vencedor']}\nPlacar final: {campeo['placar_final']}\nArtilheira: {campeo['artilheira']}\nGols da artilheira: {campeo['gols_artilheira']}\nTimes participantes: {(campeo['times_participantes'])}\nEstado: {campeo['estado']}\n\nCaso não, digite "RECOMEÇAR" para fazer outro')
        except ValueError:
            print('Coloque um número')
    p()

def sub07():
    """
    Modificar um dado específico de um campeonato
    para casos de mudanças de planos ou correção de erro
    """
    m = input(
        '\nBem vindo ao submenu 7\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
    if m.upper() == 'SAIR':
        pass
    else:
        while True:
            dici = econtrarcamp()
            camps = dici['campeonatos']
            achou = False
            try:
                a = int(input('Digite o ID do campeonato\n'))
            except ValueError:
                print('Coloque um número')
            for i in camps:
                if i['id'] == a:
                    achou = True
                    campeo = i
            if not achou:
                print('Esse campeonato não existe, se quer ter certeza que ele existe, então utilize o submenu 10')
            else:
                estadoantigo = campeo
                a = input(f'Que informação você gostaria de modificar?\n1 - Nome\n2 - Data de inicio\n3 - Data Final\n4 - Time vencedor\n5 - Placar final\n6 - Artilheira\n7 - Gols de artilheira\n8 - Times participantes\n 9 - Estado do campeonato')
                if a == '1':
                    print(f'Nome antigo:{campeo['nome']}')
                    b = input('Qual é o nome novo?\n')
                    print(f'Novo novo colocado: {b}')
                    campeo['nome'] = b
                elif a == '2':
                    print(f'Data antiga:{campeo['data_inicio']}')
                    b = input('Qual é a data inicial nova??\n')
                    print(f'Nova data colocada: {b}')
                    campeo['data_inicio'] = b
                elif a=='3':
                    print(f'Data antiga:{campeo['data_fim']}')
                    b = input('Qual é a data final nova??\n')
                    print(f'Nova data colocado: {b}')
                    campeo['data_fim'] = b
                elif a=='4':
                    print(f'Vencedor antigo:{campeo['time_vencedor']}')
                    b = input('Qual é o time vencedor novo?\n')
                    print(f'Novo time vencedor colocado: {b}')
                    campeo['time_vencedor'] = b
                elif a=='5':
                    print(f'Placar final antigo:{campeo['placar_final']}')
                    b1 = input('Quantos gols o primeiro time fez?\n')
                    b2 = input('Quantos gols o segundo time fez?')
                    c = f'{b1}-{b2}'
                    print(f'Novo placar final colocado: {c}')
                    campeo['placar_final'] = c
                elif a=='6':
                    print(f'Artilheira antiga:{campeo['artilheira']}')
                    b = input('Qual é a nova artilheira?\n')
                    print(f'Nova artilheira colocada: {b}')
                    campeo['artilheira'] = b
                elif a=='7':
                    print(f'Gols de artilheira antigo:{campeo['gols_artilheira']}')
                    while True:
                        try:
                            b = int(input('Qual são os novos gols de artilheira?\n'))
                            break
                        except ValueError:
                            print('Números inteiros apenas')
                    print(f'Novos gols: {b}')
                    campeo['gols_artilheira'] = b
                elif a=='8':
                    times = campeo['times_participantes']
                    print(f'Time: {times}')
                    b = input('O que deseja?\n1 - Adicionar time\n2 - Excluir time\n3 - Editar time')
                    if b=='1':
                        c = input('Nome do time?\n')
                        campeo['times_participantes'].append(c)
                    elif b=='2':
                        for i in times:
                            print(i)
                        c = input('Qual desses times você deseja excluir?')
                        if not c in times:
                            print('Esse time não existe')
                        else:
                          campeo['times_participantes'].pop(times.index(c))
                    elif b=='3':
                        for i in times:
                            print(i)
                        c = input('Qual desses times você deseja modificar?')
                        if not c in times:
                            print('Esse time não existe')
                        else:
                            d = input(f'O que deseja colocar no lugar do item {c}?')
                            campeo['times_participantes'].append(d)
                            campeo['times_participantes'].pop(times.index(c))

                    else:
                        print('Essa opção não existe')
                elif a=='9':
                    print(f'Estado antigo:{campeo['estado']}')
                    b = input('Qual é o novo estado?\n')
                    print(f'Novo estado colocado: {b}')
                    campeo['estado'] = b
            print(
                f'\nID: {campeo['id']}\nNome: {campeo['nome']}\nData de inicio: {campeo['data_inicio']}\nData de fim: {campeo['data_fim']}\nTime vencedor: {campeo['time_vencedor']}\nPlacar final: {campeo['placar_final']}\nArtilheira: {campeo['artilheira']}\nGols da artilheira: {campeo['gols_artilheira']}\nTimes participantes: {(campeo['times_participantes'])}\nEstado: {campeo['estado']}\n\nCaso não, digite "RECOMEÇAR" para fazer outro')
            dici['campeonatos'].remove(estadoantigo)
            dici['campeonatos'].append(campeo)
            with open('camps.json', 'w') as campeos:
                json.dump(dici, campeos)
            m = input('Se deseja voltar ao menu, digite "VOLTAR"\nSe quiser continuan editando, dê apenas enter')
            if m.upper()=='VOLTAR':
                break
    p()

def sub08():
    """
    Deletação de um campeonato.
    """
    m = input(
        '\nBem vindo ao submenu 7\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
    if m.upper() == 'SAIR':
        menuprincipal()
    else:
        dici = econtrarcamp()
        camps = dici['campeonatos']
        achou = False
        while True:
            try:
                a = int(input('Digite o ID do campeonato\n'))
                break
            except ValueError:
                print('Coloque um número')
        for i in camps:
            if i['id'] == a:
                achou = True
                campeo = i
                break
        if not achou:
            print('Esse campeonato não existe, se quer ter certeza que ele existe, então utilize o submenu 10')
        else:
            dici['campeonatos'].remove(campeo)
            with open('camps.json', 'w') as campeos:
                json.dump(dici, campeos)




def sub09():
    """
    Deleção de uma usuária
    """
    m = input(
        '\nBem vindo ao submenu 9\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
    if m.upper() == 'SAIR':
        menuprincipal()
    else:
        dici = encontraruser()
        users = dici['users']
        a = input('Diga o número de registro da jogadora a ser deletada')
        existe = False
        for i in users:
            if i['RM']==a:
                existe = True
                user = i
            if existe:
                b = input(f'Deseja mesmo remover a usuária {i['nome']} portadora do RM {i['RM']}?\nCaso sim, digite "SIM", caso não, apenas dê enter\n---->')
                if b.upper() == 'SIM':
                    dici['users'].remove(user)
                    with open('users.json', 'w') as usus:
                        json.dump(dici, usus)
                else:
                    print('Operação cancelada')
            else:
                print('Essa usuária não existe')
    p()






def sub10():
    """
    Procura por todos os campeonatos alistados
    """
    m = input(
        '\nBem vindo ao submenu 10\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
    if m.upper() == 'SAIR':
        menuprincipal()
    else:
        dici = econtrarcamp()
        camps = dici['campeonatos']
        for i in camps:
            print('###########################################################################################################################')
            print(f'\nID: {i['id']}\nNome: {i['nome']}\nData de inicio: {i['data_inicio']}\nData de fim: {i['data_fim']}\nTime vencedor: {i['time_vencedor']}\nPlacar final: {i['placar_final']}\nArtilheira: {i['artilheira']}\nGols da artilheira: {i['gols_artilheira']}\nTimes participantes: {(i['times_participantes'])}\nEstado: {i['estado']}\n')
        p()



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
        a = input('Digite o número do submenu que deseja acessar\n\n')
        if a=='1':
            sub01()
        elif a=='2':
            sub02()
        elif a == '3':
            sub03()
        elif a == '4':
            sub04()
        elif a == '5':
            sub05()
        elif a == '6':
            sub06()
        elif a == '7':
            sub07()
        elif a == '8':
            sub08()
        elif a == '9':
            sub09()
        elif a == '10':
            sub10()
        elif a== '11':
            break
        else:
            print('Tente novamente')





menuprincipal()
