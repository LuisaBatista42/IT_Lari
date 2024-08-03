class Team:
    def __init__(self, name, warCry, foundedIn ):
        self.name = name
        self.warCry = warCry
        self.foundedIn = foundedIn

list = []
def newTeam():
    name = input('Digite o nome do time:') 
    warCry = input('Digite o grito de guerra do time:') 
    foundedIn = input('Digite o ano de fundação do time:') 
    team = Team(name, warCry, foundedIn)
    list.append(team)

def validationTeam():
    if (list % 2 == 0):
        print('pode continuar com o jogo!')
    else:
        print('O número de equipes precisa ser par, volte para cadastar mais time.')

def menu():
    print("Bem vindo ao jogo BALLIT CHAMPIONSHIP!!")
    print ("")

