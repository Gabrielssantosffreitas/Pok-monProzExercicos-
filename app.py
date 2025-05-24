import random
from colorama import Fore, Back, Style

# escolha do porkemon
jogador = int(input(" Bem vindo ! \nEscolha seu pokemon: \n1 - Charmander \n2 - Squirtle \n3 - Bubassaur\n >> "))
print("\n")

porkemonDesponiveis = ["",
                       {"nome":"Charmander","vida":80,"dano":40,"defesa":25,"modoDefesa":False},
                       {"nome":"Squirtle","vida":100,"dano":35,"defesa":35,"modoDefesa":False},
                       {"nome":"Bubassaur","vida":120,"dano":30,"defesa":20,"modoDefesa":False}]

pokemonDoJogador = porkemonDesponiveis[jogador]
print(Fore.BLUE + "esse é seu pokemon ", pokemonDoJogador,""+ Style.RESET_ALL)
print("\n") 

#escolha do adversario
pokemonAdiversario = random.randint(1, 3)
pokemonAdiversario = porkemonDesponiveis[pokemonAdiversario] 
print(Fore.GREEN + "esse é o pokemon  do seu adversario ",pokemonAdiversario,""+ Style.RESET_ALL)
print("\n")


print(Fore.LIGHTYELLOW_EX + Style.BRIGHT+ "________Agora a batalha vai começar________",""+ Style.RESET_ALL)
print("\n")


# batalha 

while pokemonAdiversario['vida'] > 0  and  pokemonDoJogador['vida'] > 0: 


    #Turno do Jogador 

    escolhaJogador = int(input("Escolha Uma Dessas Açoes: \n" +  Fore.RED + " 1- ATACAR \n" + Style.RESET_ALL + Fore.LIGHTCYAN_EX + " 2- DEFENDER \n" + Style.RESET_ALL +  Fore.LIGHTMAGENTA_EX + " 3-FUGIR " + Style.RESET_ALL ))
    print("\n")

    if escolhaJogador == 1: 
        if pokemonAdiversario["modoDefesa"]: 
            danoCausado = (pokemonDoJogador["dano"] - pokemonAdiversario["defesa"])//2
            pokemonAdiversario["vida"] = pokemonAdiversario["vida"] - danoCausado
        else: 
            danoCausado = pokemonDoJogador["dano"] - pokemonAdiversario["defesa"]
            pokemonAdiversario["vida"] = pokemonAdiversario["vida"] - danoCausado
        print(Fore.BLUE + "Voce Causou ",danoCausado, " de dano no adiversaio a vida dele agora e de : ", pokemonAdiversario["vida"],"" + Style.RESET_ALL )
        print("\n")

    elif escolhaJogador == 2:
        pokemonDoJogador["modoDefesa"] = True
        print(Fore.BLUE + "Voce se Defendeu " + Style.RESET_ALL )
        print("\n")
    else:
        print(Fore.LIGHTMAGENTA_EX + "VOCÊ FUGIU " + Style.RESET_ALL ) 
        break

    
    pokemonAdiversario["modoDefesa"]=False

    #turno do adiversario 
    escolhaAdiversario = int(random.randint(1,2))
    if escolhaAdiversario == 1: 
        if pokemonDoJogador['modoDefesa']:
            danoCausadoAdiversario = (pokemonAdiversario["dano"] - pokemonDoJogador["defesa"])//2
            pokemonDoJogador["vida"] = pokemonDoJogador["vida"] - danoCausadoAdiversario
        else: 
            danoCausadoAdiversario = pokemonAdiversario["dano"] - pokemonDoJogador["defesa"]
            pokemonDoJogador["vida"] = pokemonDoJogador["vida"] - danoCausadoAdiversario
        print(Fore.GREEN + " O adiversario te atacou  e causou ", danoCausadoAdiversario, " agora vc tem ", pokemonDoJogador["vida"], ""+ Style.RESET_ALL)
        print("\n")
    else: 
        pokemonAdiversario["modoDefesa"] = True
        print(Fore.GREEN + " O adevesario se defendeu"+ Style.RESET_ALL)

    pokemonDoJogador["modoDefesa"] = False
    print(Fore.BLUE + "sua vida: ",pokemonDoJogador['vida'],"" + Fore.LIGHTYELLOW_EX + "|" + Fore.GREEN + " vida inimigo: ",pokemonAdiversario["vida"],""+ Style.RESET_ALL)

if pokemonDoJogador["vida"] > pokemonAdiversario["vida"]: 
    print(Fore.LIGHTMAGENTA_EX+ "VOCÊ GANHOU " + Style.RESET_ALL)
else: 
    print(Fore.RED + "VOCÊ PERDEU"+ Style.RESET_ALL)