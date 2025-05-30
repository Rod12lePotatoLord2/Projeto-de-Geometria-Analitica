# Operações com Vetores em Python: Multiplicação por Escala (Produto Escalar)
# Obs: O usuário deve entrar com as coordenadas dos vetores (podendo ser bidimensional ou tridimensional).

# Usuário deve fornecer as coordenadas do primeiro vetor
vetor1 = input('Digite as coordenadas do primeiro vetor (separadas por vírgula): ')
vetor1 = list(map(float, vetor1.split(',')))

# Usuário deve fornecer as coordenadas do segundo vetor
vetor2 = input('Digite as coordenadas do segundo vetor (separadas por vírgula): ')
vetor2 = list(map(float, vetor2.split(',')))

# Verificando se os vetores têm o mesmo número de dimensões
if len(vetor1) != len(vetor2):
    print('Erro: Os vetores devem ter o mesmo número de dimensões.')
else:
    # Calculando o produto escalar
    produto_escalar = sum(v1 * v2 for v1, v2 in zip(vetor1, vetor2))

    # Resultado
    print('Resultado do Produto Escalar:', produto_escalar)