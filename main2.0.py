import random
from datetime import date
import datetime
import json
import os



#Funções de procura


def encontraruser():
    """
    Recebe nenhum valor
    Busca pelo arquivo users.json
    Se o arquivo existir, abre e carrega o json
    Caso contrário, retorna um dicionário vazio igual, mas com nada dentro
    """
    if os.path.exists('users.json'):
        with open('users.json', 'r') as usuarios:
            users = json.load(usuarios)
    else:
        users = {'users':[]} #Se o arquivo users.json a função retorna à variável um dicionário identico à estrustura orginal (O mesmo é feito em econtrarcamp())
    return users

def escritauser(user): 
    """
    Recebe como parâmetro um dicionário com as informações do usuário
    Realiza o dump de informações de um usuário
    no arquivo users.json
    """
    dici = encontraruser()
    users = dici["users"]
    users.append(user)
    with open('users.json', 'w') as usus:
        json.dump(dici, usus, indent=2)


def econtrarcamp():
    """
    Recebe nenhum parâmetro
    Busca pelo arquivo camps.json
    Se o arquivo existir, abre e carrega o json
    Caso contrário, retorna um dicionário vazio igual, mas com nada dentro
    """
    if os.path.exists('camps.json'):
        with open('camps.json', 'r') as camps:
            campeonatos = json.load(camps)
    else:
        campeonatos = {'campeonatos':[]}
    return campeonatos

def escritacamp(camp):
    """
    Recebe como parâmetro um dicionário com as informações de um campeonato
    Realiza o dump de informações do campeonato
    no arquivo camps.json
    """
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
            try:
                DD1 = int(input('Diga o dia de nascimento (DD) \nEX:(17)\n'))
                MM1 = int(input('Diga o mês de nascimento (MM) \nEX:(01)\n'))
                AAAA1 = int(input('Diga o ano de nascimento (AAAA) \nEX:(1980)\n'))

                data = f'{AAAA1}-{MM1}-{DD1}'
            except ValueError:
                print('Erro: Data inválida, data será considerada a mesma de hoje, arrume isso depois no submenu 4')
                data = date.today()
            try:
                DD2 = int(input('Diga o dia de entrada (DD) \nEX:(18)\n'))
                MM2 = int(input('Diga o mês de entrada (MM) \nEX:(02)\n'))
                AAAA2 = int(input('Diga o ano de entrada (AAAA) \nEX:(2007)\n'))
                entrada = f'{AAAA2}-{MM2}-{DD2}'
            except ValueError:
                print('Erro: Data inválida, data será considerada a mesma de hoje, arrume isso depois no submenu 4')
                entrada = date.today()
            print(entrada)
            print(data)
            time = input('Diga o time da usuária\nEX: (Kansas City)')
            numero = input('Diga o número da camisa da usuária\nEX: (10)')
            posicao = input('Diga a posição da jogadora\nEX: (Zagueira)')
            b = input('Tem certeza que os dados estão corretos?\nCaso não, digita "Recomeçar" para reiniciar os dados a serem colocados\nCaso sim, apenas dê enter\n')
            if not b.upper() == 'RECOMEÇAR':
                while True:
                    existe = False
                    usuarios = users["users"]
                    regis = str(random.randint(100000,999999))
                    for i in usuarios:
                        if i["RM"] == regis:
                            existe = True
                    if not existe:
                        print(f'RM da usuária {nome}: {regis}')
                        break
                usuaria = {"nome": nome,
                  "data_nascimento": data,
                  "dia_entrada": entrada,
                  "RM": regis,
                  "time": time,
                  "numero_camisa": numero,
                  "posicao": posicao
                }
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
            if not users == []: 
                if i["RM"]==a:
                    exis = True
            else:
                break
        if not exis:
            print('\nA usuária não se encontra no registro.\n')
        else:
            print(f"Nome: {i["nome"]}\nRM:{i["RM"]}\nData de Nascimento: {i["data_nascimento"]}\nDia de entrada: {i["dia_entrada"]}\nTime: {i["time"]}\nNúmero: {i["numero_camisa"]}\nPosição: {i["posicao"]}")

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
    Cadastro de camepeonato
    recebe e cria times, nomes, datas e etc
    """
    m = input(
        '\nBem vindo ao submenu 5\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
    if m.upper() == 'SAIR':
        pass
    else:
        while True:
            dici = econtrarcamp()
            nome = input('Qual é o nome do campeonato?\n')
            try:
                DD1 = int(input('Diga o dia de nascimento (DD) \nEX:(17)\n'))
                MM1 = int(input('Diga o mês de nascimento (MM) \nEX:(01)\n'))
                AAAA1 = int(input('Diga o ano de nascimento (AAAA) \nEX:(1980)\n'))
                if DD1<=1:
                    DD1 = ('0'+str(DD1))
                elif MM1<=1:
                    MM1 = ('0'+str(AAAA1))

                data1 = f'{AAAA1}-{MM1}-{DD1}'
            except ValueError:
                print('Erro: Data inválida, data será considerada a mesma de hoje, arrume isso depois no submenu 7')
                data1 = str(date.today())
            try:
                DD2 = int(input('Diga o dia de entrada (DD) \nEX:(18)\n'))
                MM2 = int(input('Diga o mês de entrada (MM) \nEX:(02)\n'))
                AAAA2 = int(input('Diga o ano de entrada (AAAA) \nEX:(2007)\n'))
                if DD2<=9:
                    DD2 = ('0'+str(DD2))
                elif MM2<=1:
                    MM2 = ('0'+str(MM2))
                data2 = f'{AAAA2}-{MM2}-{DD2}'
            except ValueError:
                print('Erro: Data inválida, data será considerada a mesma de hoje, arrume isso depois no submenu 7')
                data2 = str(date.today())
            datatual = str(date.today())
            if not datatual<data2:
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
                    gol1 = 0
                    gol2 = 0
                    golsart = None
                    arti= 0
            else:
                vencedor = None
                gol1 = 0
                gol2 = 0
                arti = input('Tem alguma artilheira definida?\nSe não, deixe esse espaço vazio e apenas dê enter\n')
                if arti=='':
                    golsart = None
                    arti = None
                else:
                    try:
                        golsart = int(input('Quantos gols a artilheira fez?'))
                    except ValueError:
                        print('Erro: Você não colocou um número inteiro, iremos considerar o valo como nulo, mude isso depois no subemenu 7')
                        golsart = 0
            times1 = []
            while True:
                time = input('Quais são os timpes participantes?\nDIGITE "SAIR" QUANTO NÃO TIVER MAIS TIMES PARA ADICIONAR\n')
                if time.upper()=='SAIR':
                    if not len(times1)<=1:
                        break
                    elif not len(times1)%2==1:
                        print('Quantidade de times é impar, com coloque mais um time por favor')
                    else:
                        print('Por favor, coloque mais de um time')
                times1.append(time)
            times2 = ''
            for i in times1:
                times2+=i+', ' #Variável criada apenas para valor estético que será utilizado quando printar as informações
            while True:
                exis = False
                id = str(random.randint(1000,9999))
                if not dici['campeonatos']==[]:
                    for i in dici['campeonatos']:
                        if i['id']==id:
                            exis = True
                    if not exis:
                        break
            campeo ={
              "id": id,
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
            fim = input(f'As informações abaixo estão corretas?\nNome: {campeo['nome']}\nData de inicio: {campeo['data_inicio']}\nData de fim: {campeo['data_fim']}\nTime vencedor: {campeo['time_vencedor']}\nPlacar final: {campeo['placar_final']}\nArtilheira: {campeo['artilheira']}\nGols da artilheira: {campeo['gols_artilheira']}\nTimes participantes: {(times2[0:-2])+'.'}\nEstado: {campeo['estado']}\n\nCaso não, digite "RECOMEÇAR" para fazer outro')
            if fim.upper()== 'RECOMEÇAR':
                pass
            else:
                print(f'Arquivo salvo!\nID do campeonato: {campeo['id']}')
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
                a = input('Digite o ID do campeonato\n')
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
                    b = input('Opções de novos estados:\n1 - A ocorrer\n2 - Terminado\n3 - Cancelado\n')
                    if b=='1':
                        campeo['estado']='a ocorrer'
                    elif b=='2':
                        campeo['estado']='terminado'
                    elif b=='3':
                        campeo['estado']='cancelado'
                    else:
                        print('Essa opção não existe')
                    
            print(
                f'\nID: {campeo['id']}\nNome: {campeo['nome']}\nData de inicio: {campeo['data_inicio']}\nData de fim: {campeo['data_fim']}\nTime vencedor: {campeo['time_vencedor']}\nPlacar final: {campeo['placar_final']}\nArtilheira: {campeo['artilheira']}\nGols da artilheira: {campeo['gols_artilheira']}\nTimes participantes: {(campeo['times_participantes'])}\nEstado: {campeo['estado']}\n\nCaso não, digite "RECOMEÇAR" para fazer outro')
            dici['campeonatos'].remove(estadoantigo)
            dici['campeonatos'].append(campeo)
            with open('camps.json', 'w') as campeos:
                json.dump(dici, campeos, ident=2)
            m = input('Se deseja voltar ao menu, digite "VOLTAR"\nSe quiser continuan editando, dê apenas enter')
            if m.upper()=='VOLTAR':
                break
    p()

def sub08():
    """
    Excluir um campeonato.
    Requer ID do campeonato
    """
    m = input(
        '\nBem vindo ao submenu 8\nCaso tenha entrado aqui por engano\ne queira voltar o menu principal escreva "Sair"\nCaso não, apenas dê enter\n')
    if m.upper() == 'SAIR':
        menuprincipal()
    else:
        dici = econtrarcamp()
        camps = dici['campeonatos']
        achou = False
        while True:
            try:
                a = input('Digite o ID do campeonato\n')
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
            validar = input(f"Deseja MESMO deleter esse campeonato? Caso sim, digite DELETAR  e dê enter\n\nID: {campeo['id']}\nNome: {campeo['nome']}\nData de inicio: {campeo['data_inicio']}\nData de fim: {campeo['data_fim']}\nTime vencedor: {campeo['time_vencedor']}\nPlacar final: {campeo['placar_final']}\nArtilheira: {campeo['artilheira']}\nGols da artilheira: {campeo['gols_artilheira']}\nTimes participantes: {(campeo['times_participantes'])}\nEstado: {campeo['estado']}\n\n")
            if validar.upper()=='DELETAR':
                dici['campeonatos'].remove(campeo)
                with open('camps.json', 'w') as campeos:
                    json.dump(dici, campeos)
            else:
                print('Operação cancelada')
    p()




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
                        json.dump(dici, usus, ident=2)
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
