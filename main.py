from biblioteca_de_funcoes import *
from atleta import Atleta
import jsonpickle as jp

sports = ['Atletismo', 'Badminton', 'Basquetebol em cadeira de rodas', 'Bocha', 'Canoagem', 'Ciclismo (estrada e pista)', 'Esgrima em cadeira de rodas', 'Futebol de 5', 'Goalball', 'Hipismo', 'Judô', 'Levantamento de peso', 'Natação', 'Remo', 'Rugby em cadeira de rodas', 'Taekwondo', 'Tênis de mesa', 'Tênis em cadeira de rodas', 'Tiro', 'Tiro com arco', 'Triatlo', 'Voleibol sentado']
deficiency = ['Deficiência mental', 'Visual', 'Amputação', 'Deficiência física']
modalidades = dados = []
medal_gold = medal_silver = medal_bronze = 0
print('''OPÇÕES:
1 - Cadastrar
2 - Editar Cadastro
3 - Excluir Cadastro''')

while True:
    cpf = validation_cpf(input("Digite o cpf do Atleta: "))
    name = input("Nome do Atleta: ")
    age = validation_int(input("Digite a idade do Atleta: "))
    gender = validation_str(input("Sexo do Atleta: [M/F] "), 'MF')
    print("Digite apenas o número da opção correspondente a dezficiência que o Atleta possui")
    paralisy = cadastrar_lista(deficiency)
    covid = validation_str(input("Foi diagnosticado com Covid-19?: [S/N] "), 'SN')
    sports_quant = validation_int(input("De quantas modalidades o Atleta paticipou: "))

    print("Digite apenas o número da opção correspondente a modalidade que o atleta participou")
    for i in range(sports_quant):
        modalidades.append(cadastrar_lista(sports))

    medal = validation_str(input("Ganhou alguma medalha?: [S/N] "), 'SN')
    if medal == 'S':
        medal_gold = validation_int(input("Quantas medalhas de ouro: "))
        medal_silver = validation_int(input("Quantas medalhas de prata: "))
        medal_bronze = validation_int(input("Quantas medalhas de bonze: "))
    
    # lista com os dados
    dados = [cpf, name, age, gender, paralisy, covid, modalidades, medal, medal_gold, medal_silver, medal_bronze]

    # Salvar em um arquivo
    with open('cadastros.txt', 'a', encoding='utf-8') as cadastrar:
        cadastrar.write(f'{dados}\n')