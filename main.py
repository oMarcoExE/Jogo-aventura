import random
from time import sleep

PlayerLife = 10
PlayerDef = 10
PlayerAtk = 5
PlayerMoney = 5550
playerATKspeed = 5


def loja():
    global PlayerLife, PlayerDef, PlayerAtk, PlayerMoney

    print("Bem vindo à loja!")
    print("1. Comprar espada de longo alcance (+5 de dano) - $10")
    print("2. Comprar espada com lâmina de titanium(+15 de dano) - $35")
    print("3. Comprar armadura de pele de urso (+10 de defesa) - $29")
    print("4. Comprar manga do lago kor (+10 de vida maxima) - $50")
    print("5. Comprar maça de ouro (recupere 5 vidas) - $20")
    print("6. Sair")

    while True:
        print("Qual seu comando?")
        comando = input()
        if comando == '1':
            if PlayerMoney >= 10:
                print("Você comprou uma espada de longo alcance.")
                PlayerAtk += 5
                print("Agora você tem", PlayerAtk, "de ataque.")
                PlayerMoney -= 10
                break
            else:
                print("Você não tem dinheiro suficiente.")
                break
        elif comando == '2':
            if PlayerMoney >= 35:
                print("Você comprou uma espada com lâmina de titanium.")
                PlayerAtk += 15
                print("Agora você tem", PlayerAtk, "de ataque.")
                PlayerMoney -= 35
                break
            else:
                print("Você não tem dinheiro suficiente.")
                break
        elif comando == '3':
            if PlayerMoney >= 29:
                print("Você comprou uma armadura de pele de urso.")
                PlayerDef += 10
                print("Agora você tem", PlayerDef, "de defesa.")
                PlayerMoney -= 29
                break
            else:
                print("Você não tem dinheiro suficiente.")
                break
        elif comando == '4':
            if PlayerMoney >= 50:
                print("Você comprou uma manga do lago kor.")
                PlayerLife += 10
                print("Agora você tem", PlayerLife, "de vida.")
                PlayerMoney -= 50
                break
            else:
                print("Você não tem dinheiro suficiente.")
                break
        elif comando == '5':
            if PlayerMoney >= 20:
                print("Você comprou uma maça de ouro.")
                PlayerLife += 5
                print("Agora você tem", PlayerLife, "de vida.")
                PlayerMoney -= 20
                break
            else:
                print("Você não tem dinheiro suficiente.")
                break
        elif comando == '6':
            print("Você saiu da loja.")
            break

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
                print(f"Você encontra uma armadura e aumenta a defesa. Sua defesa atual é {PlayerDef}\n")
                sleep(1)
            elif bau == 'maça':
                PlayerLife += 4
                print(f"Você encontra uma maça. e recupera 4 vidas. Vida atual: {PlayerLife}\n")
                sleep(1)

            runs += 1
        
        if achar == 'inimigo':
            enemy_status(inimigo)

        if achar == 'dinheiro':
            acharDinheiro = random.randint(1, 10)
            print("Você encontra", acharDinheiro, "dólars. \n")
            PlayerMoney += acharDinheiro
            sleep(1)
        
        if PlayerLife <= 0:
            print("Você morreu")
            break
        else:
            print("Você continua a explorar o labirinto. \n")


    print("Você finalizou o primeiro campo de exploração.")
    print("Você tem", PlayerLife, "de vida!")
    print("Ataque: ", PlayerAtk)
    print("Defesa: ", PlayerDef)
    print(f"$ {PlayerMoney}\n")

def cenario2():
    pass

def cenario3():
    pass

def FinalMatch():
    pass

cenario1()

print("Deseja entrar na loja antes de iniciar sua nova aventura?")

if input() == 'yes':
    loja()
else:
    cenario2()
