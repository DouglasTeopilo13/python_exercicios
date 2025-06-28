convidados = ['Julia', 'João', 'Ana', 'Carlos', 'Mariana']

# Mensagem personalizada para cada convidado, antes da troca de convidado
# Usando o método title() para formatar os nomes
mensgem_1 = f"Olá, {convidados[0].title()}. Vou dar um juntar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensgem_2 = f"Olá, {convidados[1].title()}. Vou dar um juntar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensgem_3 = f"Olá, {convidados[2].title()}. Vou dar um juntar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensgem_4 = f"Olá, {convidados[3].title()}. Vou dar um juntar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensgem_5 = f"Olá, {convidados[4].title()}. Vou dar um juntar na minha casa hoje a noite, sua presença é muito importante para mim!"
print(mensgem_1)
print(mensgem_2)
print(mensgem_3)
print(mensgem_4)
print(mensgem_5)

# Um convidado não pode comparecer, então vamos substituí-lo
# Usando o método pop() para remover o convidado que não pode comparecer
nao_pode_comparecer = convidados.pop(1)
print(f"Infelizmente, {nao_pode_comparecer.title()} não poderá comparecer ao jantar.")
convidados.insert(1, 'carol'.title())

# Mensagem personalizada para cada convidado, após a troca de convidado
mensgem_1 = f"Olá, {convidados[0].title()}. Vou dar um juntar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensgem_2 = f"Olá, {convidados[1].title()}. Vou dar um juntar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensgem_3 = f"Olá, {convidados[2].title()}. Vou dar um juntar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensgem_4 = f"Olá, {convidados[3].title()}. Vou dar um juntar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensgem_5 = f"Olá, {convidados[4].title()}. Vou dar um juntar na minha casa hoje a noite, sua presença é muito importante para mim!"
print(mensgem_1)
print(mensgem_2)
print(mensgem_3)
print(mensgem_4)
print(mensgem_5)

# Adicionando mais convidados
mais_convidados = ['Douglas', 'Ana Clara', 'João Pedro']
print("Mais convidados foram adicionados à lista.")
convidados.append(mais_convidados[0].title())
convidados.append(mais_convidados[1].title()) 
convidados.append(mais_convidados[2].title())

# Mensagem personalizada para cada convidado, após adicionar mais convidados
mensgem_1 = f"Olá, {convidados[0].title()}. Vou dar um juntar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensgem_2 = f"Olá, {convidados[1].title()}. Vou dar um juntar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensgem_3 = f"Olá, {convidados[2].title()}. Vou dar um juntar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensgem_4 = f"Olá, {convidados[3].title()}. Vou dar um juntar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensgem_5 = f"Olá, {convidados[4].title()}. Vou dar um juntar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensgem_6 = f"Olá, {convidados[5].title()}. Vou dar um juntar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensgem_7 = f"Olá, {convidados[6].title()}. Vou dar um juntar na minha casa hoje a noite, sua presença é muito importante para mim!"
mensgem_8 = f"Olá, {convidados[7].title()}. Vou dar um juntar na minha casa hoje a noite, sua presença é muito importante para mim!"        
print(mensgem_1)
print(mensgem_2)
print(mensgem_3)
print(mensgem_4)
print(mensgem_5)
print(mensgem_6)
print(mensgem_7)
print(mensgem_8)

# Reduzindo o número de convidados
removido = convidados.pop(3)
print("Infelizmente, só posso convidar duas pessoas para o jantar.")
print(f"Desculpe, {removido.title()}, mas você não pode comparecer ao jantar.")
mensagem_1 = f"Olá, {convidados[0].title()}. Você ainda está convidado para o jantar."
mensagem_2 = f"Olá, {convidados[1].title()}. Você ainda está convidado para o jantar!"
mensagem_3 = f"Olá, {convidados[2].title()}. Você ainda está convidado para o jantar!"
mensagem_4 = f"Olá, {convidados[4].title()}. Você ainda está convidado para o jantar!"
mensagem_5 = f"Olá, {convidados[5].title()}. Você ainda está convidado para o jantar!"
mensagem_6 = f"Olá, {convidados[6].title()}. Você ainda está convidado para o jantar!"
print(mensagem_1)
print(mensagem_2)
print(mensagem_3)
print(mensagem_4)
print(mensagem_5)
print(mensagem_6)


