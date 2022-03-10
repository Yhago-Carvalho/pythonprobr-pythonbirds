from unittest import TestCase

from oo.carros import Motor, Direcao, Carro


class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)
        motor.acelerar()
        self.assertEqual(2, motor.velocidade)
        motor.acelerar()
        self.assertEqual(3, motor.velocidade)
        motor.frear()
        self.assertEqual(1, motor.velocidade)
        motor.frear()
        self.assertEqual(0, motor.velocidade)

    def teste_direcao(self):
        direcao = Direcao()
        direcao.girar_direita()
        self.assertEqual('Leste', direcao.valor)
        direcao.girar_direita()
        self.assertEqual('Sul', direcao.valor)
        direcao.girar_direita()
        self.assertEqual('Oeste', direcao.valor)
        direcao.girar_esquerda()
        self.assertEqual('Sul', direcao.valor)

