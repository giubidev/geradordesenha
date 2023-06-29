# Importando bibliotecas
import random
import string 

# Definindo uma função
def password_generator(len_pass = 8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    # Somar as strings para elas ficarem juntas
    options = ascii_options + number_options + punt_options

    password_user = ''

    # Loop de 8 vezes
    for i in range(0, len_pass):
        # [0, 1, 2, 3, 4, 5, 6, 7]
        digit = random.choice(options)
        password_user = password_user + digit
    
    return password_user # Função encerra

user_choice = input('Quantos digitos na senha?')

if user_choice.isdigit():
    user_choice = int(user_choice)
else: 
    print("Entrada inválida!")
    quit()

response = password_generator(len_pass = user_choice)

print(f"Senha gerada:\n{response}")





