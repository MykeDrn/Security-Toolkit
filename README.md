Security Toolkit: Entropy & Cryptographic Primitives

Este toolkit em Python está sendo desenvolvido como objeto de estudo, focando em alta entropia e conformidade com padrões de segurança modernos. O objetivo principal é fornecer utilitários robustos para a criação de segredos, tokens de API e chaves de derivação.

Objetivo do Projeto

O projeto serve como uma implementação prática de conceitos de CSPRNG (Cryptographically Secure Pseudo-Random Number Generator) e análise de entropia, demonstrando o uso correto de módulos críticos como secrets em oposição a geradores pseudo-aleatórios convencionais.
 Funcionalidades Atuais

    Geração de Primitivas de Alta Entropia: Strings de 64 caracteres com validação obrigatória de complexidade (letras maiúsculas, minúsculas, números e símbolos).

    Garantia de Entropia: Algoritmo projetado para entregar aproximadamente 419 bits de entropia, excedendo os requisitos para chaves de nível militar.

    CSPRNG Nativo: Utilização do módulo secrets, que acessa a fonte de entropia do sistema operacional.

Arquitetura do Algoritmo

O gerador implementa uma verificação de conformidade em tempo real:

    Seleção: Sorteio individual de caracteres de um pool de 94 símbolos.

    Validação: Teste de presença de subconjuntos de caracteres via compreensão de lista e análise booleana.

    Garantia: O loop só retorna a primitiva quando todos os critérios de segurança são satisfeitos.

Análise Matemática

A força das primitivas geradas pode ser calculada pela fórmula de Shannon:
H=L×log2​(R)

Onde o comprimento (L=64) e o pool (R=94) garantem a resistência contra ataques de força bruta e colisões.

Próximos Passos:

1.: Hashing de senhas com Salt
2.: Integração com API Have I Been Pwned
