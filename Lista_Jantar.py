# Lista de convidados para um jantar
# Neste exercício, vamos criar uma lista de convidados para um jantar e enviar mensagens personalizadas para cada um deles.
# Vamos também praticar a adição e remoção de convidados da lista.

convidados = [nome.title() for nome in ['julia', 'joão', 'ana', 'carlos', 'mariana']]
for mensagem in convidados:
    print(f"Olá, {mensagem.title()}. Vou dar uma jantar hoje a noite e você está convidado(a)" +"!\n")

# Um convidado não pode comparecer, então vamos substituí-lo
# Usando o método pop() para remover o convidado que não pode comparecer
nao_pode_comparecer = convidados.pop(1)
print(f"Infelizmente, {nao_pode_comparecer.title()} não poderá comparecer ao jantar. Vamos convidar outra pessoa!\n")

# Substituindo o convidado que não pode comparecer
convidados.insert (1, 'carol'.title())
print(f"Olá, {convidados[1].title()} Vou dar uma jantar hoje a noite e você está convidado(a)!\n")

# Adicionando mais convidados
mais_convidados = [nome.title() for nome in ['douglas', 'ana clara', 'joão pedro']]
for nome in mais_convidados:
    convidados.append(nome)
    print(f"Olá, {nome.title()}. Você está convidado para o jantar! Sua prenseça é muito importante para mim!\n")

# Reduzindo o número de convidados
remover = [nome.title() for nome in ['carol', 'julia', 'carlos', 'mariana', 'ana', 'joão pedro']]
for nome in remover:
    if nome in convidados:
        convidados.remove(nome)
        print(f"{nome.title()}, estou retirando o seu convite.!\n")

# Mensagem personalizada para os convidados restantes
for mensagem in convidados:
    print(f"Olá, {mensagem.title()}. Você ainda está convidado(a) para o jantar!\n")

#Removendo os dos convidados restantes
del convidados[:]  # Remove 'Douglas' # Remove 'Ana Clara'
print("Todos os convidados foram removidos da lista.")






