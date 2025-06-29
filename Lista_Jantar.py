# Lista de convidados para um jantar
# Neste exercício, vamos criar uma lista de convidados para um jantar e enviar mensagens personalizadas para cada um deles.
# Vamos também praticar a adição e remoção de convidados da lista.

convidados = ['Julia', 'João', 'Ana', 'Carlos', 'Mariana']

# Mensagem personalizada para cada convidado, antes da troca de convidado
# Usando o método title() para formatar os nomes
mensagem_1 = f"Olá, {convidados[0].title()}. Vou dar um jantar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensagem_2 = f"Olá, {convidados[1].title()}. Vou dar um jantar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensagem_3 = f"Olá, {convidados[2].title()}. Vou dar um jantar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensagem_4 = f"Olá, {convidados[3].title()}. Vou dar um jantar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensagem_5 = f"Olá, {convidados[4].title()}. Vou dar um jantar na minha casa hoje a noite, sua presença é muito importante para mim!"
print(mensagem_1)
print(mensagem_2)
print(mensagem_3)
print(mensagem_4)
print(mensagem_5)

# Um convidado não pode comparecer, então vamos substituí-lo
# Usando o método pop() para remover o convidado que não pode comparecer
nao_pode_comparecer = convidados.pop(1)
print(f"Infelizmente, {nao_pode_comparecer.title()} não poderá comparecer ao jantar.")
convidados.insert(1, 'carol'.title())

# Mensagem personalizada para cada convidado, após a troca de convidado
mensagem_1 = f"Olá, {convidados[0].title()}. Vou dar um jantar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensagem_2 = f"Olá, {convidados[1].title()}. Vou dar um jantar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensagem_3 = f"Olá, {convidados[2].title()}. Vou dar um jantar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensagem_4 = f"Olá, {convidados[3].title()}. Vou dar um jantar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensagem_5 = f"Olá, {convidados[4].title()}. Vou dar um jantar na minha casa hoje a noite, sua presença é muito importante para mim!"
print(mensagem_1)
print(mensagem_2)
print(mensagem_3)
print(mensagem_4)
print(mensagem_5)

# Adicionando mais convidados
mais_convidados = ['Douglas', 'Ana Clara', 'João Pedro']
print("Mais convidados foram adicionados à lista.")
convidados.append(mais_convidados[0].title())
convidados.append(mais_convidados[1].title()) 
convidados.append(mais_convidados[2].title())

# Mensagem personalizada para cada convidado, após adicionar mais convidados
mensagem_1 = f"Olá, {convidados[0].title()}. Vou dar um jantar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensagem_2 = f"Olá, {convidados[1].title()}. Vou dar um jantar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensagem_3 = f"Olá, {convidados[2].title()}. Vou dar um jantar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensagem_4 = f"Olá, {convidados[3].title()}. Vou dar um jantar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensagem_5 = f"Olá, {convidados[4].title()}. Vou dar um jantar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensagem_6 = f"Olá, {convidados[5].title()}. Vou dar um jantar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensagem_7 = f"Olá, {convidados[6].title()}. Vou dar um jantar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensagem_8 = f"Olá, {convidados[7].title()}. Vou dar um jantar na minha casa hoje a noite, sua presença é muito importante para mim!"        
print(mensagem_1)
print(mensagem_2)
print(mensagem_3)
print(mensagem_4)
print(mensagem_5)
print(mensagem_6)
print(mensagem_7)
print(mensagem_8)

# Reduzindo o número de convidados

indice_carol = convidados.index('Carol')
removido_1 = convidados.pop(indice_carol)
print(f"{removido_1.title()} não poderá comparecer ao jantar.")

indice_julia = convidados.index('Julia')
removido_2 = convidados.pop(indice_julia)
print(f"{removido_2.title()} não poderá comparecer ao jantar.")

indice_carlos = convidados.index('Carlos')
removido_3 = convidados.pop(indice_carlos)
print(f'{removido_3.title()} não poderá comparecer ao jantar.')

indice_mariana = convidados.index('Mariana')
removido_4 = convidados.pop(indice_mariana)
print(f'{removido_4.title()} não poderá comparecer ao jantar.')

indice_ana = convidados.index('Ana')
removido_5 = convidados.pop(indice_ana)
print(f'{removido_5.title()} não poderá comparecer ao jantar.')

indice_joao_pedro = convidados.index('João Pedro')
removido_6 = convidados.pop(indice_joao_pedro)  
print(f'{removido_6.title()} não poderá comparecer ao jantar.')

# Mensagem personalizada para os convidados restantes

mensagem_1 = f"Olá, {convidados[0].title()}. Você ainda está convidado(a) para o jantar."
mensagem_2 = f"Olá, {convidados[1].title()}. Você ainda está convidado(a) para o jantar!"
print(mensagem_1)
print(mensagem_2)





