'''/*******************************************************************************
Autor: Gabriel Santos Cruz
Componente Curricular: Algoritmos I
Concluido em: 06/12/2021
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
from os import system

sports = ['Atletismo', 'Badminton', 'Basquetebol em cadeira de rodas', 'Bocha', 'Canoagem', 'Ciclismo (estrada e pista)', 'Esgrima em cadeira de rodas', 'Futebol de 5', 'Goalball', 'Hipismo', 'Judô', 'Levantamento de peso', 'Natação', 'Remo', 'Rugby em cadeira de rodas', 'Taekwondo', 'Tênis de mesa', 'Tênis em cadeira de rodas', 'Tiro', 'Tiro com arco', 'Triatlo', 'Voleibol sentado']
deficiency = ['Deficiência mental', 'Visual', 'Amputação', 'Deficiência física']
modalidades = dados = []
medals_gold = medals_silver = medals_bronze = 0
medal = {}
option = 1

# inicio do programa
while option != 4:
    limpar_tela()
    print('''+------------------------------------------+
| Bem vindo ao sistema "UEFS pelos Atletas |
|     Paralimpicos"! Escolha uma opção     |
+------------------------------------------+''')
    print('''OPÇÕES:
[0] - Cadastrar
[1] - Editar Cadastro
[2] - Excluir Cadastro/Modalidade
[3] - Gerar Relatório

[4] - Sair\n''')
    #inputs
    nome_arquivo = 'cadastros.json'
    option = validation_limited_int(4,(input("Digite a opção: ")))
    cpfs = list_cpfs(nome_arquivo) # lista com todos cpfs já cadastrados, para validar a duplicidade

    if option == 0:
        limpar_tela(1)
        cpfs = list_cpfs(nome_arquivo)
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
        with open(nome_arquivo, 'a', encoding='utf-8') as cadastrar:
            cadastrar.write(f'{dados}\n')
        input("Aperte ENTER para continuar!!!")

    elif option == 1:
        limpar_tela(1)
        exibir_cadastros(nome_arquivo)
        cpf_editar = validation_cpf_digit(input("Digite o cpf do Atleta para editá-lo: "))
        validation_excluir_cpf(cpf_editar, cpfs)
        editar_cadastro(nome_arquivo, cpf_editar, deficiency, sports)
        input("Aperte ENTER para continuar!!!")

    elif option == 2:
        limpar_tela(1)
        print("Opções:\n[0] - Excluir cadastro completo\n[1] - Excluir Modalidade")
        option_2 = validation_limited_int(1, input("Digite a opção: "))

        if option_2 == 0:
            exibir_cadastros(nome_arquivo)
            cpf_excluir = validation_cpf_digit(input("Digite o cpf do Atleta para excluí-lo: "))
            validation_excluir_cpf(cpf_excluir, cpfs)
            excluir_cadastro(nome_arquivo, cpf_excluir)
            print('Cadastro excluído com sucesso!!!')
            input("Aperte ENTER para continuar!!!")

        else:
            exibir_cadastros(nome_arquivo)
            cpf_excluir = validation_int(input('Digite o cpf do Atleta: '))
            validation_excluir_cpf(cpf_excluir, cpfs)
            excluir_modalidade(nome_arquivo, cpf_excluir)
            input("Aperte ENTER para continuar!!!")

    elif option == 3:
        option_3 = 0
        while option_3 != 5:
            limpar_tela(1)
            print('''Devido ao enorme tamanho dos relatórios, separamos eles entre as opções:\n
[0] - A quantidade total de atletas que participaram dos Jogos Paraolímpicos por modalidade e sexo e o total geral;
[1] - Relação dos atletas diagnosticados com Covid-19 por modalidade e sexo;
[2] - Quadro de medalhas: quantitativo de medalhas de ouro, prata e bronze por modalidade, ordenadas primeiramente pelo número de medalhas de ouro, seguidas pelo número de medalhas de prata e de bronze;
[3] - Um recorte por modalidade e por gênero (M/F) dos atletas que ganharam medalhas, com a informação do nome do atleta, idade, tipo de paralisia e medalha(s) conquistada(s)
[4] - Das 22 modalidades disponíveis nos Jogos Paralímpicos de Tóquio, quantas o Brasil teve participação! Em quais modalidades ganhou medalha(s)! Quais modalidades que o Brasil participou e não ganhou medalha(s)! Quantas e quais modalidades o Brasil não participou! Apresentando as modalidades em ordem alfabética;

[5] - Voltar para o menu principal\n''')
            option_3 = validation_limited_int(5, input('Digite a opção: '))
            if option_3 == 0:
                limpar_tela(1)
                print('='*30,'RELATÓRIO','='*30)
                relatorio1(nome_arquivo)
                input("Aperte ENTER para continuar!!!")
            elif option_3 == 1:
                print('='*30,'RELATÓRIO','='*30)
                relatorio2(nome_arquivo)
                input("Aperte ENTER para continuar!!!")
            elif option_3 == 2:
                print('='*30,'RELATÓRIO','='*30)
                relatorio3(nome_arquivo)
                input("Aperte ENTER para continuar!!!")
            elif option_3 == 3:
                print('='*30,'RELATÓRIO','='*30)
                relatorio4(nome_arquivo)
                input("Aperte ENTER para continuar!!!")
            elif option_3 == 4:
                print('='*30,'RELATÓRIO','='*30)
                relatorio5(nome_arquivo)
                input("Aperte ENTER para continuar!!!")