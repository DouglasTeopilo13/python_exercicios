# Lista de convidados para um jantar
# Neste exercício, vamos criar uma lista de convidados para um jantar e enviar mensagens personalizadas para cada um deles.
# Vamos também praticar a adição e remoção de convidados da lista.

convidados = ['julia', 'joão', 'ana', 'carlos', 'mariana']
for mensagem in convidados:
    print("Olá, " + mensagem.title() + " Vou dar uma jantar hoje a noite e você está convidado" +"!\n")

# Um convidado não pode comparecer, então vamos substituí-lo
# Usando o método pop() para remover o convidado que não pode comparecer
nao_pode_comparecer = convidados.pop(1)
print(f"Infelizmente, {nao_pode_comparecer.title()} não poderá comparecer ao jantar.")
convidados.insert(1, 'carol'.title())
for mensagem in convidados:
    print("Olá, " + mensagem.title() + " Vou dar uma jantar hoje a noite e você está convidado" +"!\n")

# Adicionando mais convidados
mais_convidados = ['douglas', 'ana clara', 'joão pedro']
print("Mais convidados foram adicionados à lista.")
convidados.append(mais_convidados[0].title())
convidados.append(mais_convidados[1].title()) 
convidados.append(mais_convidados[2].title())

# Mensagem personalizada para cada convidado, após adicionar mais convidados
for mensagem in convidados:
    print("Vou dar um jantar na minha casa hoje a noite, sua presença é muito importante para mim" "!\n")


# Reduzindo o número de convidados
remover = ['carol', 'julia', 'carlos', 'mariana', 'ana', 'joão pedro']
for nome in remover:
    if nome in convidados:
        convidados.remove(nome)
        print(f"{nome.title()}, estou retirando o seu convite.")


# Mensagem personalizada para os convidados restantes
for mensagem in convidados:
    print(f"Olá, {mensagem.title()}. Você ainda está convidado para o jantar!")

#Removendo os dos convidados restantes

convidados_restantes = ['Douglas', 'Ana Clara']
del convidados_restantes[0]  # Remove 'Douglas' 
del convidados_restantes[0]  # Remove 'Ana Clara'
print("Todos os convidados foram removidos da lista.")






