#1 FUNÇÃO DE BOAS-VINDAS.
def boas_vindas():
    print("Bem-vindo(a)  à disciplina ALLP")
boas_vindas()


#2 FUNÇÃO QUE RETORNARÁ O QUADRADO DE UM NÚMERO.
def quadrado(numero):
    return numero ** 2
print(quadrado(4))


#3 FUNÇÃO QUE SOMARÁ DOIS NÚMEROS.
def somar (a, b):
 return a + b 
print(somar(7,7))


#4 FUNÇÃO QUE IMPRIMIRÁ UMA CONTAGEM.
def contagem(inicio = 1, fim = 5):
   for x in range(inicio, fim +1):
      print(x)
contagem()
contagem(2, 8)


#5 FUNÇÃO QUE CALCULARÁ O IMC.
def calcula_imc(peso = 70, altura = 1.75):
   return peso / (altura **2)
print(calcula_imc())
print(calcula_imc(80, 1.80))


# 6. Função que verifica se o número é par ou ímpar
def par_ou_impar(numero):
    if numero % 2 == 0:
        print(f"{numero} é par.")
    else:
        print(f"{numero} é ímpar.")
par_ou_impar(7)
par_ou_impar(10)


# 7. Função que exibe uma saudação com nome
def saudacao(nome = "Visitante"):
    print(f"Olá, {nome}! Seja bem-vindo(a).")
saudacao()
saudacao("Enzo Alzaga")