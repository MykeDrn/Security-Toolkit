"""Gerador de primitivas"""
'''Este algoritmo usa o módulo 'secrets' para gerar primitivas seguras.'''

import string
import secrets
import math
from collections import Counter

class Generator:
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

    def entropia(self, data):
        if not data:
            return 0

        counts = Counter(data)
        total_len = len(data)
        entropia = 0

        for count in counts.values():
            p = count / total_len
            entropy -= p * math.log2(p)
        return entropia

    def avaliar(self, primitiva):
        entropia = self.entropia(primitiva)
        score = (entropia / 6.55) * 100

        if score > 70:
            return f"Nível de Confiança: ALTO ({score:.1f}%)"
        else:
            return f"Nível de Confiança: MÉDIO ({score:.1f}%)"

# teste de uso
gen = Generator(tamanho=64)
senha = gen.password()
print(f'Primitiva de senha: {senha}')
token = gen.token()
print(f'Primitiva de token: {token}')
token_urlsafe =gen.token_urlsafe()
print(f'Primitiva de token URL seguro: {token_urlsafe}')
teste = gen.avaliar(senha)
print(teste)
