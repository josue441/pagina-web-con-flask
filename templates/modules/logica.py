import random

def gen_pass(pass_length):
    # Todos los elementos de la contraseña en una sola variable
    elements = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        # Se eligen los caracteres que estarán en la contraseña y los pasa a "password"
        password += random.choice(elements)
    
    return password