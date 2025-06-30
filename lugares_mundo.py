lugares_mundo = ['Vancouver', 'Munique', 'Seattle', 'Nova York', 'Madrid']
print(lugares_mundo) # Exibe a lista original de lugares do mundo
print(sorted(lugares_mundo))  # Exibe a lista em ordem alfabética
print(sorted(lugares_mundo, reverse=True)) # Exibe a lista em ordem alfabética invertida
print(lugares_mundo)  # Exibe a lista original novamente, que não foi alterada
lugares_mundo.reverse()  # Inverte a ordem da lista de lugares do mundo
print(lugares_mundo)  # Exibe a lista de lugares do mundo após a inversão
lugares_mundo.reverse()  # Inverte a ordem da lista de lugares do mundo novamente
print(lugares_mundo)  # Exibe a lista de lugares do mundo após a segunda inversão
lugares_mundo.sort()
print(lugares_mundo)  # Exibe a lista de lugares do mundo ordenada em ordem alfabética
lugares_mundo.sort(reverse=True) # Ordena a lista de lugares do mundo em ordem alfabética inversa
print(lugares_mundo)  # Exibe a lista de lugares do mundo ordenada em ordem alfabética inversa

lista_convidados = ['Ana', 'João', 'Maria', 'Pedro', 'Luiza']
print(len(lista_convidados))  # Exibe o comprimento da lista de convidados