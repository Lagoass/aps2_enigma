import funcoes


palavra = "ola meu nome e gustavo"
palavraChave = "ijkl mnopqrstuvwxyzabcdefgh"
E = funcoes.para_one_hot("bcdefghijkl mnopqrstuvwxyza")
print("Palavra: ", palavra)
print("Palavra chave: ", palavraChave)
print("********************************************************")
#Teste da função cifrar e de_cifrar
print("Teste da função cifrar e de_cifrar")
print("Cifra de enigma")
palavraCifrada = funcoes.cifrar(palavra, palavraChave)
print(palavraCifrada)
print("Decifra de enigma")
print(funcoes.de_cifrar(palavraCifrada, palavraChave))
print("********************************************************")
#Teste da função enigma e de_enigma
print("Teste da função enigma e de_enigma")
print("Cifra de enigma")
palavraCifrada = funcoes.enigma(palavra, palavraChave, E)
print(palavraCifrada)
print("Decifra de enigma")
print(funcoes.de_enigma(palavraCifrada, palavraChave, E))
print("********************************************************")