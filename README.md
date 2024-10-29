# Detalhamento das Funçoes

- Funcao - to_one_hot();
    Esta função codifica uma mensagem em formato de matriz, onde cada coluna representa uma letra.

- Funcao - to_string()
    Esta funcao transforma a mensagem em matriz para uma string

## Enigma

A função `enigma` realiza a codificação da mensagem usando a matriz Enigma.

### Detalhes da Codificação de Cada Letra:

- matrizPalavra se refere a matriz da mensagem a ser encriptada
- matrizChave é a primeira forma de encriptacao do sistema
- E é a encriptacao auxiliar

Dentro do loop que percorre cada letra na mensagem:

1. **Obtenção da Letra Correspondente na Matriz:**
   - `letra = matrizPalavra[i]`: Extrai a letra correspondente da matriz `matrizPalavra` para a posição atual no loop.

2. **Codificação da Letra com a Matriz Enigma:**
   - `letraE = matrizChave @ letra`: Multiplica a matriz da chave `matrizChave` pela letra para codificá-la usando a matriz Enigma.

3. **Atualização da Matriz da Chave com a Matriz Enigma:**
   - `matrizChave = E @ matrizChave`: Multiplica a matriz Enigma (`E`) pela matriz da chave atual (`matrizChave`), preparando para a próxima iteração.

4. **Adição da Letra Codificada à Lista:**
   - `matrizEnigma.append(letraE)`: Adiciona a letra codificada à lista `matrizEnigma`.

## De Enigma

A função `de_enigma` realiza a decodificação da mensagem previamente codificada pela matriz Enigma.

### Detalhes da Decodificação de Cada Letra:

- matrizPalavra se refere a matriz da mensagem a ser encriptada
- matrizChave é a primeira forma de encriptacao do sistema
- E é a encriptacao auxiliar

Dentro do loop que percorre cada letra na mensagem codificada:

1. **Obtenção da Letra Correspondente na Matriz:**
   - `letra = matrizPalavra[i]`: Extrai a letra correspondente da matriz `matrizPalavra` para a posição atual no loop.

2. **Decodificação da Letra com a Matriz Enigma:**
   - `letraE = np.linalg.inv(matrizChave) @ letra`: Multiplica a inversa da matriz da chave (`np.linalg.inv(matrizChave)`) pela letra para decodificá-la usando a matriz Enigma.

3. **Atualização da Matriz da Chave com a Matriz Enigma:**
   - `matrizChave = E @ matrizChave`: Multiplica a matriz Enigma (`E`) pela matriz da chave atual (`matrizChave`), preparando para a próxima iteração.

4. **Adição da Letra Decodificada à Lista:**
   - `matrizEnigma.append(letraE)`: Adiciona a letra decodificada à lista `matrizEnigma`.

# Demo de Cifra com Funções Personalizadas

Este é um exemplo de como utilizar as funções personalizadas para cifrar e decifrar mensagens usando a Máquina Enigma simulada.

## Passos para Executar o Demo:

1. **Importação das Funções:**
   - Certifique-se de ter o arquivo `funcoes.py` na mesma pasta do script de demo. Importe as funções usando `import funcoes`.

2. **Definição de Palavra, Palavra-Chave e Matriz Enigma:**
   - Defina a palavra a ser cifrada (`palavra`), a palavra-chave (`palavraChave`), e a matriz Enigma (`E`). Neste exemplo:
     ```python
     palavra = "ola meu nome e gustavo"
     palavraChave = "ijkl mnopqrstuvwxyzabcdefgh"
     E = funcoes.para_one_hot("bcdefghijkl mnopqrstuvwxyza")
     ```

3. **Cifrar e Decifrar usando Funções `cifrar` e `de_cifrar`:**
   - Utilize as funções `cifrar` e `de_cifrar` para cifrar e decifrar utilizando a matriz chave.
     ```python
     print("Cifra de enigma")
     palavraCifrada = funcoes.cifrar(palavra, palavraChave)
     print(palavraCifrada)
     print("Decifra de enigma")
     print(funcoes.de_cifrar(palavraCifrada, palavraChave))
     ```

4. **Cifrar e Decifrar usando Funções `enigma` e `de_enigma`:**
   - Utilize as funções `enigma` e `de_enigma` para cifrar e decifrar utilizando a matriz Enigma.
     ```python
     print("Cifra de enigma")
     palavraCifrada = funcoes.enigma(palavra, palavraChave, E)
     print(palavraCifrada)
     print("Decifra de enigma")
     print(funcoes.de_enigma(palavraCifrada, palavraChave, E))
     ```

5. **Resultado:**
   - Execute o script e observe os resultados da cifra e decifra usando ambas as abordagens.

Este demo demonstra a utilização das funções personalizadas para cifrar e decifrar mensagens tanto com uma matriz chave padrão quanto com a Máquina Enigma simulada.
