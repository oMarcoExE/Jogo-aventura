from random import choice, randint
from time import sleep

PlayerLife = 100
PlayerDef = 10
PlayerAtk = 5
PlayerMoney = 0
playerATKspeed = 8


def main():
    print("Bem vindo ao jogo de aventura!")
    print("Você tem", PlayerLife, "vidas!")
    while True:
        print("Qual seu comando?")

def battle(inimigo, statusEnemy):
    global PlayerLife, PlayerDef, PlayerAtk, PlayerMoney, playerATKspeed

    enemyATKspeed = statusEnemy['speedATK']
    enemyATK = statusEnemy['Ataque']
    enemyLife = statusEnemy['Vida']
    

    print(f"Inimigo: {inimigo}")

    while True:
        if enemyATKspeed > playerATKspeed:
            print("Inimigo começa a atacar")
            sleep(1)
            ataqueEnemy = randint(1, enemyATK)
            PlayerLife -= ataqueEnemy
            print(f"Inimigo ataca com {ataqueEnemy} de dano")
            sleep(1)
            ataquePlayer = randint(1, PlayerAtk)
            enemyLife -= ataquePlayer
            print(f"Você ataca com {ataquePlayer} de dano")
            sleep(1)
        else:
            print("Você começa a atacar")
            sleep(1)
            ataquePlayer = randint(1, PlayerAtk)
            enemyLife -= ataquePlayer
            print(f"Você ataca com {ataquePlayer} de dano")
            sleep(1)

        if enemyLife <= 0:
            print("Inimigo morreu")
            sleep(1)
            break
        elif PlayerLife <= 0:
            print("Você morreu")
            sleep(1)
            break
        else:
            sleep(1)
        
        


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

        enemyStatus = {
            'Vida': inimigo[0]['Vida'],
            'Ataque': inimigo[0]['Ataque'],
            'speedATK': inimigo[0]['speedATK'],
            'defesa': inimigo[0]['defesa']
        }

      #  return print ("Aranha \n", inimigo)
    
    elif inimigo == 'Zumbi':
        inimigo = Zumbi

        name = 'Zumbi'

        enemyStatus = {
            'Vida': inimigo[0]['Vida'],
            'Ataque': inimigo[0]['Ataque'],
            'speedATK': inimigo[0]['speedATK'],
            'defesa': inimigo[0]['defesa']
        }

      #  return print ("Zumbi \n", inimigo)
    
    elif inimigo == 'Esqueleto':
        inimigo = Esqueleto

        name = 'Esqueleto'

        enemyStatus = {
            'Vida': inimigo[0]['Vida'],
            'Ataque': inimigo[0]['Ataque'],
            'speedATK': inimigo[0]['speedATK'],
            'defesa': inimigo[0]['defesa']
        }

       # return print ("Esqueleto \n", inimigo)
    
    battle(inimigo, enemyStatus)



def cenario1():
    global PlayerLife, PlayerDef, PlayerAtk, PlayerMoney

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

    if achar == 'dinheiro':
        acharDinheiro = randint(1, 10)
        print("Você encontra", acharDinheiro, "dólars.")
        PlayerMoney += acharDinheiro
        sleep(1)


cenario1()