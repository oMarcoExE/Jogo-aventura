import random
from time import sleep

PlayerLife = 15
PlayerDef = 10
PlayerAtk = 5
PlayerMoney = 0
playerATKspeed = 1


def main():
    print("Bem vindo ao jogo de aventura!")
    print("Você tem", PlayerLife, "vidas!")
    while True:
        print("Qual seu comando?")

def battle(name, inimigo, statusEnemy):
    global PlayerLife, PlayerDef, PlayerAtk, PlayerMoney, playerATKspeed

    enemyATKspeed = statusEnemy['speedATK']
    enemyATK = statusEnemy['Ataque']
    enemyLife = statusEnemy['Vida']
    

    print(f"Inimigo: {name}")
    print(f"Vida: {enemyLife}, Ataque: {enemyATK}, Speed: {enemyATKspeed} \n")

    while True:
        if enemyATKspeed > playerATKspeed:
            print("Inimigo começa a atacar")
            sleep(1)
            ataqueEnemy = random.randint(1, enemyATK)
            PlayerLife -= ataqueEnemy
            print(f"Inimigo ataca com {ataqueEnemy} de dano")
            sleep(1)
            print("Seu turno: ")
            ataquePlayer = random.randint(1, PlayerAtk)
            enemyLife -= ataquePlayer
            print(f"Você ataca com {ataquePlayer} de dano")
            sleep(1)
        else:
            print("Você começa a atacar")
            sleep(1)
            ataquePlayer = random.randint(1, PlayerAtk)
            enemyLife -= ataquePlayer
            print(f"Você ataca com {ataquePlayer} de dano")
            sleep(1)
            print("Turno inimigo: ")
            sleep(1)
            ataqueEnemy = random.randint(1, enemyATK)
            PlayerLife -= ataqueEnemy
            print(f"Inimigo ataca com {ataqueEnemy} de dano")
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
    
    elif inimigo == 'Zumbi':
        inimigo = Zumbi

        name = 'Zumbi'

        enemyStatus = {
            'Vida': inimigo[0]['Vida'],
            'Ataque': inimigo[0]['Ataque'],
            'speedATK': inimigo[0]['speedATK'],
            'defesa': inimigo[0]['defesa']
        }
    
    elif inimigo == 'Esqueleto':
        inimigo = Esqueleto

        name = 'Esqueleto'

        enemyStatus = {
            'Vida': inimigo[0]['Vida'],
            'Ataque': inimigo[0]['Ataque'],
            'speedATK': inimigo[0]['speedATK'],
            'defesa': inimigo[0]['defesa']
        }

    
    battle(name,inimigo, enemyStatus)



def cenario1():
    global PlayerLife, PlayerDef, PlayerAtk, PlayerMoney
    runs = 0

    lista_achar = ['bau', 'inimigo', 'dinheiro']
    lista_bau = ['espada', 'armadura', 'maça',]
    lista_inimigo = ['Aranha', 'Zumbi', 'Esqueleto']

    pesos = [0.4, 0.5, 0.1]

    print("Você está em um labirinto de floresta.")
    sleep(1)
    
    while runs < 3:

        achar = random.choices(lista_achar, weights=pesos, k=1)[0]
        bau = random.choice(lista_bau)
        inimigo = random.choice(lista_inimigo)

        print("Voce verifica o mato e encontra um", achar, ".\n")

        if achar == 'bau':
            sleep(1)
            if bau == 'espada':
                PlayerAtk += random.randint(1, 6)
                print(f"Você encontra uma espada e aumento o ataque. Seu ataque atual é {PlayerAtk}\n")
                sleep(1)
            elif bau == 'armadura':
                PlayerDef += random.randint(1, 6)
                print(f"Você encontra uma armadura e aumento o defesa. Sua defesa atual é {PlayerDef}\n")
                sleep(1)
            elif bau == 'maça':
                PlayerLife += 4
                print(f"Você encontra uma maça. e recupera 4 vidas. Vida atual: {PlayerLife}\n")
                sleep(1)

            runs += 1
        
        if achar == 'inimigo':
            enemy_status(inimigo)

        if achar == 'dinheiro':
            acharDinheiro = randint(1, 10)
            print("Você encontra", acharDinheiro, "dólars. \n")
            PlayerMoney += acharDinheiro
            sleep(1)
        
        print("Você continua a explorar o labirinto. \n")

cenario1()