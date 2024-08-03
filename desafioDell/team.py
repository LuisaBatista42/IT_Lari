import random
import time

class Team:
    def __init__(self, name, warCry, foundedIn ):
        self.name = name
        self.warCry = warCry
        self.foundedIn = foundedIn
    
    def __str__(self):
        return self.name

def validationTeam(amountTeam):
    if amountTeam >= 1:
        if (amountTeam % 2 == 0):
            print('Pode continuar com o jogo!')
            return True
        
        else:
            print('O número de equipes precisa ser par, volte para cadastar mais time.')
            return False
        
    else:
        print('Precisa ter no mínimo 8 times para poder iniciar')
        return False


list =  [
    Team("Cruzeiro", "É o Azul que te emociona!", 1921),
    Team("Flamengo", "Uh, Flamengo, uh, uh, tetracampeão de tudo!", 1895),
    Team("Palmeiras", "Avanti Palestra!", 1914),
    Team("Grêmio", "É tricolor, com toda a força!", 1903),
    Team("São Paulo", "Aqui é São Paulo!", 1930),
    Team("Internacional", "Colorado que te amarga!", 1909),
    Team("Atlético Mineiro", "Massa Bruta!", 1908),
    Team("Corinthians", "Vai, Corinthians!", 1910),
]

def newTeam():
    name = input('Digite o nome do time:') 
    warCry = input('Digite o grito de guerra do time:') 
    foundedIn = input('Digite o ano de fundação do time:') 
    team = Team(name, warCry, foundedIn)
    list.append(team)

def sortTeams():
    random.shuffle(list)

def match():
    for i in range(len(list)):
        if i % 2 == 0:
            print(f"Jogo {i//2 + 1}: {list[i]} vs {list[i+1]}")

results = {}
def game(teamA, teamB):
    pointA = 50
    pointB = 50

    while True:
        print(f"Jogo ", teamA,"vs ", teamB)
        print(f"1 - Registrar um 'blot' para o time", teamA)
        print(f"2 - Registrar um 'blot' para o time", teamB)
        print(f"3 - Registrar um 'plif' para o time", teamA)
        print(f"4 - Registrar um 'plif' para o time", teamB)
        print("5 - Encerrar a partida")

        try:
            option = int(input("Digite sua opção: "))
        except ValueError:
            print("Opção inválida. Digite um número inteiro.")
            continue

        if option == 1:
            pointA += 5
        elif option == 2:
            pointB += 5
        elif option == 3:
            pointA += 1
        elif option == 4:
            pointB += 1
        elif option == 5:
            break
        else:
            print("Opção inválida.")

        print(f"{teamA} {pointA} x {pointB} {teamB}")

    if pointA > pointB:
        print(teamA, 'venceu e avança para a próxima fase.')
    elif pointB > pointA:
        print(teamB, 'venceu e avança para a próxima fase.')
    else:
        print('Grusht - ocorreu um empate!')
        for i in range(10):
            result = random.randint(0,10)
            if(result % 2 == 0):
                resA = i+1
                print('grito do time',teamA)
            else:
                resB = i+1
                print('grito do time',teamB)
    
        if (resA>resB):
            print(teamA, 'venceu e avança para a próxima fase.')
        else:
            print(teamB, 'venceu e avança para a próxima fase.')

def chooseMatch():
    print('Escolha qual das partidas você deseja jogar:')
    while True:
        try:
            escolha = int(input())
            if 1 <= escolha <= len(list) // 2:
                jogo_escolhido = (escolha * 2) - 2  
                print(f"Você escolheu o jogo {escolha}:")
                print(f"{list[jogo_escolhido]} vs {list[jogo_escolhido + 1]}")
                game(f"{list[jogo_escolhido]}", f"{list[jogo_escolhido + 1]}")
                break
            else:
                print("Escolha inválida. Digite um número entre 1 e", len(list) // 2)
        except ValueError:
            print("Por favor, digite um número inteiro.")

# crio uma lista que vai colocando os que foram classificados e comparo
# com a lista de cadastro inicial 
# time que venceu vai direto para a lista

def registerTeams():
    amountTeam = int(input("Deseja cadastrar quantas equipes?"))
    validationTeam(amountTeam)

    for team in range(amountTeam):
        print('Cadastando equipe',team+1)
        newTeam()
    
#registerTeams()
sortTeams()  
match()
chooseMatch()
