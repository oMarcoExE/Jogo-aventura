from random import choice, randint
from time import sleep

playerLife = 100



def main():
    print("Bem vindo ao jogo de aventura!")
    print("Você tem", PlayerLife, "vidas!")
    while True:
        print("Qual seu comando?")


def cenario1():
    global PlayerLife
    lista_achar = ['bau', 'inimigo', 'dinheiro']
    print("Você está em um labirinto de floresta.")
    sleep(1)
    print("Voce verifica o mato e encontra um", choice(lista_achar), ".")


cenario1()