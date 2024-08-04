from random import choice, randint
from time import sleep

PlayerLife = 100
PlayerDef = 10
PlayerAtk = 5



def main():
    print("Bem vindo ao jogo de aventura!")
    print("Você tem", PlayerLife, "vidas!")
    while True:
        print("Qual seu comando?")


def cenario1():
    global PlayerLife, PlayerDef, PlayerAtk

    lista_achar = ['bau', 'inimigo', 'dinheiro']
    lista_bau = ['espada', 'armadura', 'maça',]
    bau = choice(lista_bau)
    achar = choice(lista_achar)
    print("Você está em um labirinto de floresta.")
    sleep(1)
    print("Voce verifica o mato e encontra um", achar, ".")
    if achar == 'bau':
        sleep(1)
        if bau == 'espada':
            print("Você encontra uma espada e aumento o ataque.")
            PlayerAtk += randint(1, 6)
            sleep(1)
        elif bau == 'armadura':
            print("Você encontra uma armadura e aumento o defesa.")
            PlayerDef += randint(1, 6)
            sleep(1)
        elif bau == 'maça':
            print("Você encontra uma maça. e recupera 10 vidas.")
            PlayerLife += 10
            sleep(1)


cenario1()