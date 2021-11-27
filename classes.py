class Atleta:
    def __init__(self, cpf, name, age, gender, paralisy, covid, modality):
        self.cpf = cpf
        self.name = name
        self.age = age
        self.gender = gender
        self.paralisy = paralisy
        self.covid = covid
        self.modality = modality # tem que alterar para o uso da classe modalidade no arquivo principal

class Modalidade:
    def __init__(self, modalidade, medals_gold, medals_silver, medals_bronze):
        self.modalidade = modalidade
        self.medals_gold = medals_gold
        self.medals_silver = medals_silver
        self.medals_bronze = medals_bronze