import jsonpickle as jp

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

def validation_limited_int(limitation, num): # validar as entradas se são int e se está de acordo com as opções
    while not num.isdigit or (int(num) > limitation) or (int(num) < 0):
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
        cpf_excluir = int(input("Digite o cpf do Atleta para excluí-lo: "))
    return int(cpf_excluir)

def excluir_cadastro(nome_arquivo, cpf_excluir):
    # abre o arquivo e salvar excluindo o que é pra excluir
    with open(nome_arquivo, "r+") as arquivo: #abri o arquivo como leitura e edição
        new_file = arquivo.readlines() # transforma em lista
        arquivo.seek(0)
        for line in new_file:
            line = jp.decode(line)
            if line.cpf != cpf_excluir: # verifica se é o a linha pra ser excluida
                arquivo.write(f'{jp.encode(line)}\n') # grava as linhas que não são a que deve ser excluida
        arquivo.truncate()