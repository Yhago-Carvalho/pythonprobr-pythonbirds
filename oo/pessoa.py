class Pessoa():
    def __init__(self, *filhos, nome=None, idade=27):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá'


if __name__ == '__main__':
    jorge = Pessoa(nome='Jorge', idade=25)
    joão = Pessoa(jorge, nome='joão', idade=50)
    print(joão.cumprimentar())
    print(joão.nome)
    print(joão.idade)
    for filho in joão.filhos:
        print(filho.nome)
    joão.sobrenome = 'Carvalho'
    del joão.filhos
    print(joão.__dict__)
    print(jorge.__dict__)
    