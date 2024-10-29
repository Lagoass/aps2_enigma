import numpy as np

# Transforma uma palavra em um array de inteiros, onde cada coluna representa uma letra.
# O número 1 aparece uma vez em cada linha, indicando a letra da palavra.
def para_one_hot(palavra):
    letras = list(palavra)
    # Inicializa uma matriz de zeros com o tamanho adequado para armazenar a representação one-hot.
    one_hot = np.zeros((len(letras), 27))
    for i, letra in enumerate(letras):
        # Verifica se a letra é um espaço e atribui o índice 26 para o caractere de espaço.
        if letra == ' ':
            index = 26
        else:
            # Converte a letra para um índice, considerando 'a' como 0 e 'z' como 25.
            index = ord(letra) - ord('a')
            # Garante que caracteres fora do alcance das letras minúsculas tenham índice 0.
            if index < 0 or index >= 27:
                index = 0
        # Define o valor 1 na posição correspondente à letra, se ainda não estiver definido.
        if one_hot[i, index] != 1:
            one_hot[i, index] = 1
    return one_hot

# Converte uma matriz one-hot de volta para uma string.
def para_string(array):
    mensagem = ""
    for linha in array:
        # Obtém o índice da posição onde o valor é 1.
        index = np.argmax(linha)
        # Se o índice for 26, adiciona um espaço à mensagem.
        if index == 26:
            mensagem += " "
        else:
            # Converte o índice para o caractere correspondente e adiciona à mensagem.
            mensagem += chr(index + ord('a'))
    return mensagem

# Cifra uma palavra usando multiplicação de matrizes entre a palavra e a palavra-chave.
def cifrar(palavra, palavraChave):
    palavra = palavra.lower()
    matrizPalavra = para_one_hot(palavra)
    matrizChave = para_one_hot(palavraChave)
    # Realiza a multiplicação de matrizes para cifrar a mensagem.
    Y = matrizPalavra @ matrizChave
    return para_string(Y)

# Decifra uma palavra cifrada usando a matriz inversa da palavra-chave.
def de_cifrar(palavra, palavraChave):
    matrizChave = para_one_hot(palavraChave)
    matrizPalavra = para_one_hot(palavra)
    # Multiplica a palavra cifrada pela matriz inversa da palavra-chave para decifrar.
    X = matrizPalavra @ np.linalg.inv(matrizChave)
    return para_string(X)

# Codifica uma palavra usando a matriz Enigma e a matriz chave.
def enigma(palavra, palavraChave, E):
    matrizPalavra = para_one_hot(palavra)
    matrizChave = para_one_hot(palavraChave)
    matrizEnigma = []
    for i in range(len(palavra)):
        letra = matrizPalavra[i]
        # Codifica a letra usando a matriz Enigma e multiplica a matriz chave pela matriz Enigma.
        letraE = matrizChave @ letra
        matrizChave = E @ matrizChave
        matrizEnigma.append(letraE)
    matrizEnigma = np.array(matrizEnigma)
    return para_string(matrizEnigma)

# Decodifica uma palavra codificada usando a matriz inversa da palavra-chave e a matriz Enigma.
def de_enigma(palavra, palavraChave, E):
    matrizPalavra = para_one_hot(palavra)
    matrizChave = para_one_hot(palavraChave)
    matrizEnigma = []
    for i in range(len(palavra)):
        letra = matrizPalavra[i]
        # Decodifica a letra usando a matriz Enigma e a matriz inversa da palavra-chave.
        letraE = np.linalg.inv(matrizChave) @ letra
        matrizChave = E @ matrizChave
        matrizEnigma.append(letraE)
    matrizEnigma = np.array(matrizEnigma)
    return para_string(matrizEnigma)
