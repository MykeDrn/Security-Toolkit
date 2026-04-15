'''Gerador de primitivas'''
'''Este algoritmo usa o módulo 'secrets' para gerar primitivas seguras.'''

import string
import secrets 

class generator:
    def __init__(self, tamanho=64):
        self.caracteres = string.ascii_letters + string.digits + string.punctuation # Define os caracteres permitidos para a senha
        self.tamanho=tamanho # Define o tamanho da senha ou token a ser gerado
    
    def password(self):
        while True:
            primitiva = ''.join(secrets.choice(self.caracteres) for _ in range(self.tamanho))
            # Validação técnica
            if (any(c.islower() for c in primitiva) 
                and any(c.isupper() for c in primitiva) 
                and any(c.isdigit() for c in primitiva) 
                and any(c in string.punctuation for c in primitiva)):
                return primitiva
    
    def token(self):
        return secrets.token_hex(self.tamanho // 2)  # Gera um token hexadecimal

    def token_urlsafe(self):
        return secrets.token_urlsafe(self.tamanho)  # Gera um token seguro para URLs
 
    
# teste de uso

senha = generator(tamanho=16).password()
print(f'Primitiva de senha: {senha}')
token = generator(tamanho=32).token()
print(f'Primitiva de token: {token}')
token_urlsafe = generator(tamanho=32).token_urlsafe()
print(f'Primitiva de token URL seguro: {token_urlsafe}')
