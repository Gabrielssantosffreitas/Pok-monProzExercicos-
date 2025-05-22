import random
# escolha do porkemon
jogador = int(input(" Bem vindo ! \nEscolha seu pokemon: \n1 - Charmander \n2 - Squirtle \n3 - Bubassaur\n >> "))
porkemonDesponiveis = ["",
                       {"nome":"Charmander","vida":80,"dano":40,"defesa":25},
                       {"nome":"Squirtle","vida":100,"dano":35,"defesa":35},
                       {"nome":"Bubassaur","vida":120,"dano":30,"defesa":20}]

pokemonDoJogador = porkemonDesponiveis[jogador]
print("esse é seu pokemon ", pokemonDoJogador)
#escolha do adversario
pokemonAdiversario = random.randint(1, 3)
pokemonAdiversario = porkemonDesponiveis[pokemonAdiversario] 
print("esse é o pokemon  do seu adversario ",pokemonAdiversario)

print("________Agora a batalha vai começar________")

while pokemonAdiversario['vida'] > 0  or pokemonDoJogador['vida'] > 0: 
    # turno do jogador 
    escolha = input("deseja \n 1- atacar \n 2- defender \n3- fugir \n >> ")
    if escolha == "1": 
        pokemonAdiversario['vida'] = pokemonAdiversario['vida'] - (pokemonDoJogador['dano'] - pokemonAdiversario['defesa']) 
        print("vc atacou o ", pokemonAdiversario['nome'] ," vc causou ", (pokemonDoJogador['dano'] - pokemonAdiversario['defesa']))
    elif escolha == "2" : 
        pokemonDoJogador['vida'] = pokemonDoJogador['vida'] - (pokemonAdiversario.dano // 2)
        print(" vc defendeu o ataca vc sofreu ", (pokemonAdiversario.dano // 2) )
    else: 
        break
    # turno do adviersario
    escolhaDoAdiversario = random.randint(1,2)
    if escolha == 1: 
        pokemonAdiversario['vida'] = pokemonAdiversario['vida'] - (pokemonDoJogador['dano'] - pokemonAdiversario['defesa'])
        print("o adversario  atacou o ", pokemonDoJogador['nome'] ," vc causou ", (pokemonAdiversario['dano'] - pokemonDoJogador['defesa'])) 
    elif escolha == 2 : 
        pokemonDoJogador['vida'] = pokemonDoJogador['vida'] - (pokemonAdiversario['dano'] // 2)
        print(" o adiversario  defendeu o ataca vc sofreu ", (pokemonDoJogador.dano // 2) )
    
    
