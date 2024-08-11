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
        else: print("Você não escolheu uma opção válida.")

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
        

def enemy_status1(inimigo):

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

def enemy_status2(inimigo):

    Dracorcego  = []
    urso = []
    louco = []
    fanático = []

    Dracorcego.append({
        'Vida': 25,
        'Ataque': 7,
        'speedATK': 9,
        'defesa': 1,
    })

    urso.append({
        'Vida': 20,
        'Ataque': 10,
        'speedATK': 2,
        'defesa': 3,
    })

    louco.append({
        'Vida': 10,
        'Ataque': 4,
        'speedATK': 15,
        'defesa': -1,
    })

    fanático.append({
        'Vida': 15,
        'Ataque': 5,
        'speedATK': 2,
        'defesa': 4,
    })

    if inimigo == 'Dracorcego':
        inimigo = Dracorcego

        name = 'Dracorcego'

        enemyStatus = {
            'Vida': inimigo[0]['Vida'],
            'Ataque': inimigo[0]['Ataque'],
            'speedATK': inimigo[0]['speedATK'],
            'defesa': inimigo[0]['defesa']
        }
    
    elif inimigo == 'urso':
        inimigo = urso

        name = 'urso'

        enemyStatus = {
            'Vida': inimigo[0]['Vida'],
            'Ataque': inimigo[0]['Ataque'],
            'speedATK': inimigo[0]['speedATK'],
            'defesa': inimigo[0]['defesa']
        }
    
    elif inimigo == 'louco':
        inimigo = louco

        name = 'louco'

        enemyStatus = {
            'Vida': inimigo[0]['Vida'],
            'Ataque': inimigo[0]['Ataque'],
            'speedATK': inimigo[0]['speedATK'],
            'defesa': inimigo[0]['defesa']
        }
    
    elif inimigo == 'fanático':
        inimigo = fanático

        name = 'fanático'

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
    
    while runs < 2:

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
            enemy_status1(inimigo)

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
    global PlayerLife, PlayerDef, PlayerAtk, PlayerMoney

    achar = random.choices(['bau', 'inimigo', 'dinheiro'], weights=[0.4, 0.5, 0.1], k=1)[0]
    bau = random.choice(['espada', 'armadura', 'maça'])
    lista_inimigo = random.choice(['Dracorcego', 'urso', 'louco', 'fanático'])

    inimigo = random.choices(['Dracorcego', 'urso', 'louco', 'fanático'], weights=[0.2, 0.3, 0.5, 0.1], k=1)[0]


    enemy_status2(inimigo)



def Chefe():
    global PlayerLife, PlayerDef, PlayerAtk, PlayerMoney

    print("Voce descobre que encontrou o lar de um cyclope de 4 metros de altura")
    print("e que estava preso por um chefe de uma cidade distante.")

    print("Voce se esconde e se prepara para lutar")
    print("Voce encotra uma manga banhada a diamante, come e ganha buffs")
    
    PlayerLife += 15
    PlayerDef += 10
    PlayerAtk += 8
    
    print("Ataque aumentado temporariamente")
    sleep(1)
    print("Defesa aumentada temporariamente")
    sleep(1)
    print("Vida aumentada temporariamente")
    input()

    print("Voce se sente confiante e parte para a luta...")
    sleep(1)

    cyclope = []

    cyclope.append({
        'Vida': 60,
        'Ataque': 20,
        'speedATK': 1,
        'defesa': 15,
    })

    cyclopeATKspeed = cyclope[0]['speedATK']
    cyclopeATK = cyclope[0]['Ataque']
    cyclopeLife = cyclope[0]['Vida']


    while True:
        if cyclopeATKspeed > playerATKspeed:
            print("Cyclope começa o ataque")
            sleep(1)
            ataqueEnemy = random.randint(1, cyclopeATK)
            PlayerLife -= ataqueEnemy
            if PlayerLife <= 0:
                print("voce morreu")
                break
            print(f"Cyclope ataca com {ataqueEnemy} de dano")
            sleep(1)
            print("Seu turno: ")
            ataquePlayer = random.randint(1, PlayerAtk)
            cyclopeLife -= ataquePlayer
            if cyclopeLife <= 0:
                print("\nCyclope morto!\n")
                break
            print(f"Voce ataca com {ataquePlayer} de dano")
            sleep(1)
        else:
            print("Voce começa a atacar")
            sleep(1)
            ataquePlayer = random.randint(1, PlayerAtk)
            cyclopeLife -= ataquePlayer
            print(f"Voce ataca com {ataquePlayer} de dano")
            if cyclopeLife <= 0:
                print("\nCyclope morto!\n")
                break
            print("Turno inimigo: ")
            sleep(1)
            ataqueEnemy = random.randint(1, cyclopeATK)
            PlayerLife -= ataqueEnemy
            print(f"Cyclope ataca com {ataqueEnemy} de dano")
            if PlayerLife <= 0:
                print("voce morreu")
                break


def cenario3():
    pass

def FinalMatch():
    pass

cenario1()

print("Deseja entrar na loja antes de iniciar sua nova aventura?")
option = input()
while True:
    if option == 'yes':
        loja()
        break
    elif option == 'no':
        break
    else: print("Você não escolheu uma opção válida.")


print("2 caminhos vistos a sua frente")
sleep(1)
print("oque deseja fazer? \n")
print("1. ir a direita e entrar dentro de uma montanha")
print("2. cair em um buraco escuro e misterioso")
option = input()

if option == '1':
    cenario2()
elif option == '2':
    Chefe()
elif option == '3':
    print("Você avista uma misteriosa cachoeira secreta, e decide entrar nela.")
    cenario3()
else:
    print("Opção inválida")