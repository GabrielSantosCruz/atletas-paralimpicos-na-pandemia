def validation_str(var, palavras_chave): # validar strings de cadastro com S ou N ou M e F
    while var.upper() not in palavras_chave or len(var) == 0:
        var = input(f'Erro, digite apenas [{palavras_chave[0]}/{palavras_chave[1]}]: ')
    return var.upper()

def validation_int(var): # validar números inteiros
    while not var.isdigit() or len(var) == 0:
        var = input('Erro, Digite apenas números: ')
    return int(var)

def validation_cpf(cpf): # validar se o cpf digitado é considerado válido
    while not cpf.isdigit() or len(cpf) != 11:
        cpf = input("Erro! Cpf inválido, digite novamente: ")
    return cpf

def validation_limited_int(limitation, num):
    while not num.isdigit or int(num) > limitation:
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

def exibir_cadastros(nome_arquivo):
    import jsonpickle as jp
    with open(nome_arquivo, 'r') as arquivo:
        for cadastro in arquivo:
            atleta = jp.decode(cadastro)
            print(f'Cpf: {atleta.cpf}, Nome: {atleta.name}, Idade: {atleta.age},Sexo: {atleta.gender},Tipo de paralisia: {atleta.paralisy},Teve covid: {atleta.covid},Modalidades: {atleta.modality}')

def list_cpfs(nome_arquivo):
    lista = []
    try:
        with open(nome_arquivo, 'r') as cadastrados:
            for cpf in cadastrados:
                cpfs = jp.decode(cpf)
                lista.append(cpfs.cpf)
    except:
        None
def validation_cpf(cpf, lista_cpfs):
    try:
        while cpf in lista_cpfs:
            print('Cpf já cadastrado!')
            cpf = int(input("Cpf: "))
    except TypeError:
        return cpf