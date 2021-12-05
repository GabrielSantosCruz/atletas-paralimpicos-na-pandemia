import jsonpickle as jp
from classes import Atleta, Modalidade

def validation_str(var, palavras_chave): # validar strings de cadastro com S ou N ou M e F
    var = var.upper()
    while var not in palavras_chave or len(var) == 0:
        var = input(f'Erro, digite apenas [{palavras_chave[0]}/{palavras_chave[1]}]: ')
    
    if var == 'S':
        var = 'Sim'
    elif var == 'N':
        var = 'Nao'
    elif var == 'M':
        var = 'Masculino'
    elif var == 'F':
        car = 'Feminino'
    return var

def validation_int(var): # validar números inteiros
    while not var.isdigit() or len(var) == 0:
        var = input('Erro, Digite apenas números: ')
    return int(var)

def validation_cpf_digit(cpf): # validar se o cpf digitado é considerado válido
    while not cpf.isdigit() or len(cpf) != 11:
        cpf = input("Erro! Cpf inválido, digite novamente: ")
    return int(cpf)

## se digitar string ainda da erro
def validation_limited_int(limitation, num): # validar as entradas se são int e se está de acordo com as opções
    num = str(num)
    while not num.isdigit:
        while not (int(num) > limitation) or (int(num) < 0):
            num = input("Erro, digite um número válido: ")
    return int(num)
    
def cadastrar_lista(lista): # usa uma lista com as opções para transformar em opções númericas para cadastrar
    for numero, nome in enumerate(lista): # transforma em opção
        print(f'[{numero}] - {nome}')
    
    cadastro = validation_limited_int(len(lista), input("Digite a opção: "))
    for numero, nome in enumerate(lista): # compara a opção digitada com os da lista
        if cadastro == numero:
            cadastro = nome  

    return cadastro

def limpar_tela(time=0):
    from os import system
    from time import sleep
    sleep(time)
    system('cls')

def exibir_cadastros(nome_arquivo): # função para exibir as informações de todos atletas cadastrados
    try: 
        import jsonpickle as jp
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for cadastro in arquivo:
                atleta = jp.decode(cadastro)
                print(f'Cpf: {atleta.cpf}, Nome: {atleta.name}, Idade: {atleta.age}, Sexo: {atleta.gender}, Tipo de paralisia: {atleta.paralisy}, Teve covid: {atleta.covid}')
                exibir_modalidade(atleta.modality)
    except FileNotFoundError:
        print("Nenhum atleta foi cadastrado ainda")

def exibir_modalidade(modality): # função para exibir todas as informações das modalidades em que o atleta foi cadastrado
    import jsonpickle as jp
    for num, modalidade in enumerate(modality):
        #modalidade = jp.decode(modalidade)
        print(f'Modalidade {num+1}: {modalidade.modalidade}, Medalhas de ouro: {modalidade.medals_gold}, Medalhas de prata: {modalidade.medals_silver}, Medalhas de bronze: {modalidade.medals_bronze}')
    print('\n')

def list_cpfs(nome_arquivo): # função para criar uma lista com todos os cpfs dos atletas cadastrados
    import jsonpickle as jp
    lista = []
    with open(nome_arquivo, 'r') as cadastrados:
        for cpf in cadastrados:
            cpfs = jp.decode(cpf)
            lista.append(cpfs.cpf)
    return lista

def validation_cpf(cpf, lista_cpfs): # valida se o cpf digitado já foi cadastrado
    while cpf in lista_cpfs:
        print('Cpf já cadastrado!')
        cpf = int(input("Digite o cpf do Atleta: "))
    return int(cpf)

def validation_excluir_cpf(cpf_excluir, lista_cpfs): # valida se o cpf digitado já foi cadastrado
    while cpf_excluir not in lista_cpfs:
        print('O cpf digitado não está cadastrado! Digite um cpf válido!')
        cpf_excluir = int(input("Digite o cpf do Atletao: "))
    return int(cpf_excluir)

def excluir_cadastro(nome_arquivo, cpf_excluir):
    # abre o arquivo e salva excluindo o que é pra excluir
    with open(nome_arquivo, "r+") as arquivo: #abri o arquivo como leitura e edição
        new_file = arquivo.readlines() # transforma em lista
        arquivo.seek(0)
        for line in new_file:
            line = jp.decode(line)
            if line.cpf != cpf_excluir: # verifica se é o a linha pra ser excluida
                arquivo.write(f'{jp.encode(line)}\n') # grava as linhas que não são a que deve ser excluida
        arquivo.truncate()

def cadastrar_objeto(lista): # usa uma lista com as opções para transformar em opções númericas para cadastrar
    import jsonpickle as jp
    print('Modalidades que o Atleta participou: ')
    for numero, nome in enumerate(lista): # transforma em opção
        #nome = jp.decode(nome)
        print(f'[{numero}] - {nome.modalidade}')
    
    cadastro = validation_limited_int(len(lista), input("Digite a opção: "))
    return cadastro

def excluir_modalidade(nome_arquivo, cpf_excluir):
    with open(nome_arquivo, "r+") as arquivo:
        new_file = arquivo.readlines() # transforma em lista
        arquivo.seek(0)
        for line in new_file:
            line = jp.decode(line)
            lista = line.modality
            if line.cpf == cpf_excluir: # verifica se é o a linha do arquivo pra ser excluida
                
                if len(lista) == 1:
                    print('Não é possível excluir a unica modalidade em que o atleta participou!!!')
                ## ainda exclui quando tem só 1
                else:
                    modalidade_excluir = cadastrar_objeto(lista)
                    del lista[modalidade_excluir]
                    line.modality = lista
                    # converter em uma lista, depois trocar a lista com o parametro
                    arquivo.write(f'{jp.encode(line)}\n')
            else: 
                arquivo.write(f'{jp.encode(line)}\n') # grava as linhas que não são a que deve ser excluida
        arquivo.truncate()


def editar_cadastro(nome_arquivo, cpf_editar, deficiency, sports):
    from classes import Modalidade, Atleta
    import jsonpickle as jp
    with open(nome_arquivo, "r+") as cadastros:
        new_cadastro = cadastros.readlines()
        cadastros.seek(0)
        #altera o cadastro
        for line in new_cadastro:
            line = jp.decode(line)
            if line.cpf == cpf_editar:
                line.name = input("Digite o nome do Atleta: ")
                line.age = validation_int(input("Digite a idade do Atleta: "))
                line.gender = validation_str(input("Digite o sexo do Atleta: [M/F] "), "MF")
                line.paralisy = cadastrar_lista(deficiency)
                line.covid = validation_str(input("O Atleta teve covid: [S/N] "), "SN")
                sports_quant = validation_int(input("De quantas modalidades o Atleta paticipou: "))
                # caso haja só 1 modalidade de inicio apenas edita 1 e não consegue adicionar
                modalidades = []
                for i in range(sports_quant):
                    modalidade = cadastrar_lista(sports)
                    have_medal = validation_str(input("Ganhou alguma medalha?: [S/N] "), 'SN')
                    #provavelmente vou ter que voltar aqui para ver o caso dessa 
                    medals_gold = medals_silver = medals_bronze = 0
                    if have_medal == 'Sim':
                        medals_gold = validation_int(input("Quantas medalhas de ouro: "))
                        medals_silver = validation_int(input("Quantas medalhas de prata: "))
                        medals_bronze = validation_int(input("Quantas medalhas de bonze: "))
                    modalidade_ = Modalidade(modalidade, medals_gold, medals_silver, medals_bronze)
                    modalidades.append(modalidade_)

                line.modality = modalidades

                cadastros.write(f'{jp.encode(line)}\n')
            else:
                cadastros.write(f'{jp.encode(line)}\n')
        cadastros.truncate()

def relatorio1(nome_arquivo):
    # A quantidade total de atletas que participaram dos Jogos Paraolímpicos por modalidade e sexo, informando também o total geral;
    sports = ['Atletismo', 'Badminton', 'Basquetebol em cadeira de rodas', 'Bocha', 'Canoagem', 'Ciclismo (estrada e pista)', 'Esgrima em cadeira de rodas', 'Futebol de 5', 'Goalball', 'Hipismo', 'Judô', 'Levantamento de peso', 'Natação', 'Remo', 'Rugby em cadeira de rodas', 'Taekwondo', 'Tênis de mesa', 'Tênis em cadeira de rodas', 'Tiro', 'Tiro com arco', 'Triatlo', 'Voleibol sentado']
    import jsonpickle as jp
    quant_modality = fem = masc = 0
    try:
        
        for modalidade in sports: # a modalidade de cada um
            quant_modality = fem = masc = 0 # pra resetar o valor
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                for atleta in arquivo: # ler o cadastro de cada atleta
                    atleta = jp.decode(atleta)
                # tem que dar um len(atleta.modality)
                    for i in range(len(atleta.modality)): # porque podem haver mais de uma modalidade cadastrada
                        #print(atleta.modality[i].modalidade)
                        if atleta.modality[i].modalidade == modalidade:
                            quant_modality += 1
                            if atleta.gender == 'Masculino':
                                masc += 1
                            elif atleta.gender == 'Feminino':
                                fem += 1

            if quant_modality > 0:
                
                if masc == 0:
                    print(f'A modalidade {modalidade} teve {quant_modality} atleta(s) participando. Sendo dentre eles: {fem} Mulher(es) e nenhum Homem!')
                elif fem == 0:
                    print(f'A modalidade {modalidade} teve {quant_modality} atleta(s) participando. Sendo dentre eles: {masc} Homem(ns) e nenhuma Mulher!')
                else:
                    print(f'A modalidade {modalidade} teve {quant_modality} atleta(s) participando. Sendo dentre eles: {masc} homem(ns) e {fem} mulher(es)!')
            else:
                print(f'A modalidade {modalidade} não teve nenhum atleta participando!')

    except FileNotFoundError:
        print("Nenhum atleta foi cadastrado ainda")

def relatorio2(nome_arquivo):
    #Relação dos atletas diagnosticados com Covid-19 por modalidade e sexo;
    # modalidade tal teve tantos com covid e tantos sem
    sports = ['Atletismo', 'Badminton', 'Basquetebol em cadeira de rodas', 'Bocha', 'Canoagem', 'Ciclismo (estrada e pista)', 'Esgrima em cadeira de rodas', 'Futebol de 5', 'Goalball', 'Hipismo', 'Judô', 'Levantamento de peso', 'Natação', 'Remo', 'Rugby em cadeira de rodas', 'Taekwondo', 'Tênis de mesa', 'Tênis em cadeira de rodas', 'Tiro', 'Tiro com arco', 'Triatlo', 'Voleibol sentado']
    import jsonpickle as jp
    quant_covid = fem = masc = 0
    try:
        
        for modalidade in sports: # a modalidade de cada um
            quant_covid = fem = masc = 0 # pra resetar o valor
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                for atleta in arquivo: # ler o cadastro de cada atleta
                    atleta = jp.decode(atleta)
                # tem que dar um len(atleta.modality)
                    for i in range(len(atleta.modality)): # porque podem haver mais de uma modalidade cadastrada
                        #print(atleta.covid)
                        if atleta.modality[i].modalidade == modalidade:
                            if atleta.covid == 'Sim':
                                quant_covid += 1
                                if atleta.gender == 'Masculino':
                                    masc += 1
                                elif atleta.gender == 'Feminino':
                                    fem += 1

            if quant_covid > 0:
                
                if masc == 0:
                    print(f'A modalidade {modalidade} teve {quant_covid} atleta(s) diagnosticados com covid. Sendo dentre eles: {fem} Mulher(es) e nenhum Homem!')
                elif fem == 0:
                    print(f'A modalidade {modalidade} teve {quant_covid} atleta(s) diagnosticados com covid. Sendo dentre eles: {masc} Homem(ns) e nenhuma Mulher!')
                else:
                    print(f'A modalidade {modalidade} teve {quant_covid} atleta(s) diagnosticados com covid. Sendo dentre eles: {masc} homem(ns) e {fem} mulher(es)!')

            else:
                print(f'A modalidade {modalidade} não teve nenhum atleta diagnosticados com covid!')

    except FileNotFoundError: # verificar essa parte nos outros
        None

def relatorio3(nome_arquivo):
    #Quadro de medalhas: quantitativo de medalhas de ouro, prata e bronze por modalidade, ordenadas primeiramente pelo número de medalhas de ouro, seguidas pelo número de medalhas de prata, finalmente, de bronze;
    sports = ['Atletismo', 'Badminton', 'Basquetebol em cadeira de rodas', 'Bocha', 'Canoagem', 'Ciclismo (estrada e pista)', 'Esgrima em cadeira de rodas', 'Futebol de 5', 'Goalball', 'Hipismo', 'Judô', 'Levantamento de peso', 'Natação', 'Remo', 'Rugby em cadeira de rodas', 'Taekwondo', 'Tênis de mesa', 'Tênis em cadeira de rodas', 'Tiro', 'Tiro com arco', 'Triatlo', 'Voleibol sentado']
    import jsonpickle as jp
    gold = silver = bronze = tot = 0
    try:
        
        for modalidade in sports: # a modalidade de cada um
            gold = silver = bronze = tot = 0 # pra resetar o valor
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                for atleta in arquivo: # ler o cadastro de cada atleta
                    atleta = jp.decode(atleta)
                # tem que dar um len(atleta.modality)
                    for i in range(len(atleta.modality)): # porque podem haver mais de uma modalidade cadastrada
                        #print(atleta.covid)
                        if atleta.modality[i].modalidade == modalidade:
                            gold += atleta.modality[i].medals_gold
                            silver += atleta.modality[i].medals_silver
                            bronze += atleta.modality[i].medals_bronze
            tot = gold+silver+bronze
            if tot > 0:
                
                print(f'Na modalidade {modalidade} as medalhas foram: {gold} de Ouro, {silver} de Prata e {bronze} de Ouro')

            else:
                print(f'Nenhum Atleta ganhou medalha na modalidade {modalidade}')

    except FileNotFoundError: # verificar essa parte nos outros
        None

def relatorio4(nome_arquivo):
    #Um recorte por modalidade e por gênero (M/F) dos atletas que ganharam medalhas, com a informação do nome do atleta, idade, tipo de paralisia e medalha(s) conquistada(s)
    sports = ['Atletismo', 'Badminton', 'Basquetebol em cadeira de rodas', 'Bocha', 'Canoagem', 'Ciclismo (estrada e pista)', 'Esgrima em cadeira de rodas', 'Futebol de 5', 'Goalball', 'Hipismo', 'Judô', 'Levantamento de peso', 'Natação', 'Remo', 'Rugby em cadeira de rodas', 'Taekwondo', 'Tênis de mesa', 'Tênis em cadeira de rodas', 'Tiro', 'Tiro com arco', 'Triatlo', 'Voleibol sentado']
    import jsonpickle as jp
    masc_gold = masc_silver = masc_bronze = tot = 0
    try:
        for modalidade in sports: # a modalidade de cada um
            texto_masc = texto_fem = ''
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                for atleta in arquivo: # ler o cadastro de cada atleta
                    atleta = jp.decode(atleta)
                    # tem que dar um len(atleta.modality)
                    for i in range(len(atleta.modality)): # porque podem haver mais de uma modalidade cadastrada
                        #print(atleta.covid)
                        if atleta.modality[i].modalidade == modalidade:
                            if atleta.gender == 'Masculino':
                                if (atleta.modality[i].medals_gold + atleta.modality[i].medals_silver + atleta.modality[i].medals_bronze) > 0:
                                    texto_masc += f'Nome: {atleta.name}, Idade: {atleta.age}, Tipo de paralisia: {atleta.paralisy} - Medalhas: Ouro: {atleta.modality[i].medals_gold}, Prata {atleta.modality[i].medals_silver}, Bronze: {atleta.modality[i].medals_bronze}.\n'
                                else: 
                                    texto_masc += f'Nome: {atleta.name}, Idade: {atleta.age}, Tipo de paralisia: {atleta.paralisy} - O Atleta não ganhou Medalhas\n'

                            elif atleta.gender == 'Feminino':
                                if (atleta.modality[i].medals_gold + atleta.modality[i].medals_silver + atleta.modality[i].medals_bronze) > 0:
                                    texto_fem += f'Nome: {atleta.name}, Idade: {atleta.age}, Tipo de paralisia: {atleta.paralisy} - Medalhas: Ouro: {atleta.modality[i].medals_gold}, Prata {atleta.modality[i].medals_silver}, Bronze: {atleta.modality[i].medals_bronze}.\n'
                                else: 
                                    texto_fem += f'Nome: {atleta.name}, Idade: {atleta.age}, Tipo de paralisia: {atleta.paralisy} - A Atleta não ganhou Medalhas\n'

            print(f'\n============= Modalidade: {modalidade} =============')
            # Não teve nenhum atleta
            # só houve atleta masculino
            # ó houve atleta feminino
            # houve os 2
            if len(texto_masc) == 0 and len(texto_fem) == 0:
                print('Não Houve nenhum Atleta cadastrado nesta modalidade!')
            else:
                if len(texto_masc) == 0:
                    print('Não Houveram Atletas Masculinos nesta modalidade!')
                else:
                    print(f'=====> Atletas Masculinos\n{texto_masc}')
                if len(texto_fem) == 0:
                    print('Não Houveram Atletas Femininas nesta modalidade!')
                else:
                    print(f'=====> Atletas Femininas\n{texto_fem}')
    #Um recorte por modalidade e por gênero (M/F) dos atletas que ganharam medalhas, com a informação do nome do atleta, idade, tipo de paralisia e medalha(s) conquistada(s)
    except FileNotFoundError: # verificar essa parte nos outros
        None