class Pessoa():
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=27):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return 'Olá'

    @staticmethod
    def metodo_estatico():
        return  42

    @classmethod
    def nome_atributo_classe(cls):
        return  f'{cls} - Olhos {cls.olhos}'


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
    joão.olhos = 1
    print(Pessoa.olhos)
    print(joão.olhos)
    print(jorge.olhos)
    print(joão.__dict__)
    print(jorge.__dict__)
    print(joão.cumprimentar())
    print(Pessoa.metodo_estatico(), jorge.metodo_estatico())
    print(Pessoa.nome_atributo_classe(), jorge.nome_atributo_classe())
