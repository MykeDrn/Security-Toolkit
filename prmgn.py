'''Gerador de primitivas'''
'''Este algoritmo usa o módulo 'secrets' para gerar primitivas seguras.'''

import string
import secrets 

caracteres = string.ascii_letters + string.digits + string.punctuation

def prim_gen():
    while True:
        primitiva = ''.join(secrets.choice(caracteres) for _ in range(64)) # gera uma primitiva aleatória de 64 caracteres.
        if (any(c.islower() for c in primitiva) 
            and any(c.isupper() for c in primitiva) 
            and any(c.isdigit() for c in primitiva) 
            and any(c in string.punctuation for c in primitiva)):
            return primitiva # verifica se a primitiva tem ao menos um caractere de cada tipo.
        
    
# teste de uso
primitiva_gerada = prim_gen()
if primitiva_gerada:
    print("Primitiva gerada:", primitiva_gerada)
    