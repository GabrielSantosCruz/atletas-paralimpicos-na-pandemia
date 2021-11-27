def validation_str(var, palavras_chave): # validar strings de cadastro com S ou N ou M e F
    while var.upper() not in palavras_chave or len(var) == 0:
        var = input(f'Erro, digite apenas [{palavras_chave[0]}/{palavras_chave[1]}]: ')
    return var.upper()

def validation_int(var): # validar números inteiros
    while not var.isdigit() or len(var) == 0:
        var = input('Erro, Digite apenas números: ')
    return int(var)

def validation_cpf_digit(cpf): # validar se o cpf digitado é considerado válido
    while not cpf.isdigit() or len(cpf) != 11:
        cpf = input("Erro! Cpf inválido, digite novamente: ")
    return int(cpf)

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
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for cadastro in arquivo:
            atleta = jp.decode(cadastro)
            print(f'Cpf: {atleta.cpf}, Nome: {atleta.name}, Idade: {atleta.age}, Sexo: {atleta.gender}, Tipo de paralisia: {atleta.paralisy}, Teve covid: {atleta.covid}')
            exibir_modalidade(atleta.modality)

def exibir_modalidade(modality):
    import jsonpickle as jp
    for modalidade in modality:
        #modalidade = jp.decode(modalidade)
        print(f'Modalidade: {modalidade.modalidade}, Medalhas de ouro: {modalidade.medals_gold}, Medalhas de prata: {modalidade.medals_silver}, Medalhas de bronze: {modalidade.medals_bronze}')

def list_cpfs(nome_arquivo):
    import jsonpickle as jp
    lista = []
    with open(nome_arquivo, 'r') as cadastrados:
        for cpf in cadastrados:
            cpfs = jp.decode(cpf)
            lista.append(cpfs.cpf)
    return lista

def validation_cpf(cpf, lista_cpfs):
    while cpf in lista_cpfs:
        print('Cpf já cadastrado!')
        cpf = int(input("Digite o cpf do Atleta: "))
    return int(cpf)