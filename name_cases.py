#27/06/2025 Exercício de nomes e formatação de strings. Foi o mais longo que escrevi até agora

name = 'Douglas'
message = f"Olá , {name} gostaria de aprender um pouco sobre python hoje?"
print(message)

name = 'Ana'
print(name.lower())  # Minúsculas
print(name.upper())  # Maiúsculas
print(name.title())  # Capitalização de cada palavra

citacao = "Se você não acha que é o melhor, então fique em casa"
first_name = 'Max'
last_name = 'Verstappen' 
message = f"Certa vez {first_name.title()} {last_name.title()} disse: '{citacao}'"
print(message)

citacao = "Se você não acha que é o melhor, então fique em casa"
famous_person = 'Max Verstappen'
message = f"{famous_person.title()} uma vez disse: '{citacao}'"
print(message)

name = ' Douglas ' 
print(name)
name = name.lstrip()
print(name)
name = name.rstrip()
print(name)
name = name.strip()
print(name)

age = 23
name = 'Julia'
message = f"Happy {age}rd bithday, {name.title()}!"
print(message)



