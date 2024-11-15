import random
lista = ["celula", "mitocondria", "lisossomo"] #Adicione aqui novas palavras que comporão a lista de possibilidades de escolha

palavra_escolhida = random.choice(lista)
print(palavra_escolhida) #Printa a palavra escolhida da lista. Apague para tornar secreta a palavra

display = ["_"] * len(palavra_escolhida)
gameover = False
vidas = 5
letras_digitadas = []

while not gameover:
    print(f"Você tem {vidas} vidas.")
    escolha = input("Escolha uma letra: ").lower()

    if escolha in letras_digitadas:
        print("Você já digitou essa letra. Tente outra.")
        continue
    letras_digitadas.append(escolha)

    if escolha in palavra_escolhida:
        for position in range(len(palavra_escolhida)):
            letra = palavra_escolhida[position]
            if letra == escolha:
                display[position] = letra
    else:
        vidas -= 1
        print("Letra incorreta. Você perdeu uma vida.")
    print(" ".join(display))

    if "_" not in display:
        gameover = True
        print("Você ganhou!")
    elif vidas == 0:
        gameover = True
        print("Você perdeu! :(")
