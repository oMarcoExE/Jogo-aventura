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

def battle():
    #if enemyATKspeed > playerATKspeed
        #inimigo começa atacando
    #else
        #player começa atacando

    #dinamica batalha
    # randint(1, playerATK) para dano player
    # randint(1, enemyATK) para dano inimigo

    
    print(f"Batalha com {name}")

    while True:
        pass
        
        


def enemy_status(inimigo):

    Aranha = []
    Zumbi = []
    Esqueleto = []

    Aranha.append({
        'Vida': 10,
        'Ataque': 2,
        'speedATK': 6,
        'defesa': 3,
    })

    Zumbi.append({
        'Vida': 15,
        'Ataque': 4,
        'speedATK': 4,
        'defesa': 4,
    })

    Esqueleto.append({
        'Vida': 8,
        'Ataque': 6,
        'speedATK': 2,
        'defesa': 1
    })

    if inimigo == 'Aranha':
        inimigo = Aranha

        name = 'Aranha'

        vidaEnemy = inimigo[0]['Vida']
        ataqueEnemy = inimigo[0]['Ataque']
        speedATKEnemy = inimigo[0]['speedATK']
        defesaEnemy = inimigo[0]['defesa']

        return print ("Aranha \n", inimigo)
    
    elif inimigo == 'Zumbi':
        inimigo = Zumbi

        name = 'Zumbi'

        vidaEnemy = inimigo[0]['Vida']
        ataqueEnemy = inimigo[0]['Ataque']
        speedATKEnemy = inimigo[0]['speedATK']
        defesaEnemy = inimigo[0]['defesa']

        return print ("Zumbi \n", inimigo)
    
    elif inimigo == 'Esqueleto':
        inimigo = Esqueleto

        name = 'Esqueleto'

        vidaEnemy = inimigo[0]['Vida']
        ataqueEnemy = inimigo[0]['Ataque']
        speedATKEnemy = inimigo[0]['speedATK']
        defesaEnemy = inimigo[0]['defesa']

        return print ("Esqueleto \n", inimigo)
    



def cenario1():
    global PlayerLife, PlayerDef, PlayerAtk

    lista_achar = ['bau', 'inimigo', 'dinheiro']
    lista_bau = ['espada', 'armadura', 'maça',]
    lista_inimigo = ['Aranha', 'Zumbi', 'Esqueleto']
    bau = choice(lista_bau)
    achar = choice(lista_achar)
    inimigo = choice(lista_inimigo)
    print("Você está em um labirinto de floresta.")
    sleep(1)
    print("Voce verifica o mato e encontra um", achar, ".\n")
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
    
    if achar == 'inimigo':
        enemy_status(inimigo)


cenario1()