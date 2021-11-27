'''/*******************************************************************************
Autor: Gabriel Santos Cruz
Componente Curricular: Algoritmos I
Concluido em: xx/11/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
O código e sua evolução pode ser encontrado em: https://github.com/GabrielSantosCruz/atletas-paralimpicos-na-pandemia
******************************************************************************************/'''
from biblioteca_de_funcoes import *
from classes import Atleta, Modalidade
import jsonpickle as jp

sports = ['Atletismo', 'Badminton', 'Basquetebol em cadeira de rodas', 'Bocha', 'Canoagem', 'Ciclismo (estrada e pista)', 'Esgrima em cadeira de rodas', 'Futebol de 5', 'Goalball', 'Hipismo', 'Judô', 'Levantamento de peso', 'Natação', 'Remo', 'Rugby em cadeira de rodas', 'Taekwondo', 'Tênis de mesa', 'Tênis em cadeira de rodas', 'Tiro', 'Tiro com arco', 'Triatlo', 'Voleibol sentado']
deficiency = ['Deficiência mental', 'Visual', 'Amputação', 'Deficiência física']
modalidades = dados = []
medals_gold = medals_silver = medals_bronze = 0
medal = {}
option = 1

# inicio do programa
while option != 5:
    print('''OPÇÕES:
[0] - Cadastrar
[1] - Editar Cadastro
[2] - Excluir Cadastro
[3] - Gerar Relatório
[4] - Sair''')
    #inputs
    option = validation_limited_int(4,(input("Digite a opção: ")))
    if option == 0:
        cpfs = list_cpfs('cadastros.json')
        cpf = validation_cpf_digit(input("Digite o cpf do Atleta: "))
        validation_cpf(cpf, cpfs)
        name = input("Nome do Atleta: ")
        age = validation_int(input("Digite a idade do Atleta: "))
        gender = validation_str(input("Sexo do Atleta: [M/F] "), 'MF')
        print("Digite apenas o número da opção correspondente a deficiência que o Atleta possui")
        paralisy = cadastrar_lista(deficiency)
        covid = validation_str(input("Foi diagnosticado com Covid-19?: [S/N] "), 'SN')

        sports_quant = validation_int(input("De quantas modalidades o Atleta paticipou: "))
        print("Digite apenas o número da opção correspondente a modalidade que o atleta participou")
        # assim que pegar qual foi a modalidade, cadastrar as medalhas da mesma
        for i in range(sports_quant):
            #modalidades.append(cadastrar_lista(sports))
            modalidade = cadastrar_lista(sports)
            have_medal = validation_str(input("Ganhou alguma medalha?: [S/N] "), 'SN')
            #provavelmente vou ter que voltar aqui para ver o caso desa 
            if have_medal == 'Sim':
                # falta separar as medalhas por modalidade
                medals_gold = validation_int(input("Quantas medalhas de ouro: "))
                medals_silver = validation_int(input("Quantas medalhas de prata: "))
                medals_bronze = validation_int(input("Quantas medalhas de bonze: "))
            modality = Modalidade(modalidade, medals_gold, medals_silver, medals_bronze)
            modalidades.append(modality)
        # criando a classe e salvando no arquivo
        dados = jp.encode(Atleta(cpf, name, age, gender, paralisy, covid, modalidades))
        with open('cadastros.json', 'a', encoding='utf-8') as cadastrar:
            cadastrar.write(f'{dados}\n')
    elif option == 1:
        exibir_cadastros('cadastros.json')
    
    elif option == 2:
        exibir_cadastros('cadastros.json')
        cpfs = list_cpfs('cadastros.json')
        cpf_excluir = validation_cpf_digit(input("Digite o cpf do Atleta para excluí-lo: "))
        validation_excluir_cpf(cpf_excluir, cpfs)
        excluir_cadastro('cadastros.json', cpf_excluir)