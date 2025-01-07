numero1 = 3 #valor numerico INTEIRO
numero2 = 3.0 #valor numerico Float
texto1 = "texto" # valor texto String
verdadeiro = True #variavel tipo Booleana, SEMPRE COMEÇA COM MAIUSCULA
falso = False #variavel tipo Booleana, SEMPRE COMEÇA COM MAIUSCULA

print("Ola Mundo!")#escreva("") em portugol

numero1 = int(input("Digite um numero: "))#leia(numero1) em portugol

print("O numero é: ", numero1) #primeiro jeito de mostrar a variavel

#Operações basicas de matematica
somaExemplo = 1 + 2 #soma 2 inteiros
subtracaoExemplo = 2 - 1
multiplicacaoExemplo = 4 * 1
potenciaExemplo = 3 ** 2
divisaoExemplo = 6.0 / 2.0
divisãoParteInteira = 9.0 // 2.0
restoDivisaoExemplo = 3.0 % 2.0


print(f"A soma é {somaExemplo}, a subração é {somaExemplo} a multiplicação é {multiplicacaoExemplo} a potencia é {potenciaExemplo} a divisão é {divisaoExemplo}"
     + "divisão é  {divisãoParteInteira} o resto é {restoDivisaoExemplo}")

#TIPOS DE CONVERSÃO DE VARIAVEL

tipoInteiro = int(input("Numero convertido para inteiro !!!"))
int(tipoInteiro) #outra forma de converter

#O PYTHON ACEITA SOMENTE . PARA ENTENDER QUE É UM NUMERO REAL
tipoQuebrado = float(input("Numero convertido para real")) #numeros com casas depois da virgula 1.0
float(tipoQuebrado) #outra forma de converter

#Por padrão, o valor da variavel recebida pelo input é String
tipoTexto = input("Texto padrão String")
str(tipoTexto) #mas é possivel converter dessa forma se necessario

#Tipos de marcadores de posições 
print("O numero é: %i ", numero1) # %i numeros Inteiros
print("O numero é: %f ", float(numero1)) # %f numeros quebrados
print("O numero é: %.2f ", float(numero1)) # %.2f quantidade de numeros apos a virgula
print("O numero é: %s ", str(numero1)) #%s para string


#CONCATENAÇÃO

texto2 = "Parte1" + "Parte2" #CONCATENAÇÃO de STRINGS
print("O numero é: " + str(numero1)) #terceiro jeito de mostrar na tela #"Parte1" + "Parte2" #CONCATENAÇÃO





print(f"O numero é:{numero1} ") #quarto jeito de mostrar na tela


#OPERADORES LOGICOS 
#Operadores logicos sistema onde retorna uma condição de verdadeiro ou falso, só fazem sentido dentro de uma estrutura de CONDIÇÃO
numero1 >= numero2 # operador logico maior igual
numero1 <= numero2 # operador logico menor igual
numero1 == numero2 # operador logico igual
numero1 != numero2 # operador logico diferente

#Operações de atribuição
numero1 += 1 # Equivalente a numero1= numero1 + 1
numero1 += 2 # Equivalente a numero1= numero1 + 2
numero1 -= 1 # Equivalente a numero1= numero1 - 1
numero1 += numero2 # Equivalente a numero1= numero1 + numero 2
numero1 -= numero2 # Equivalente a numero1= numero1 - numero 2

#estruturas de CONDIÇÃO
if(numero1>=1):     #condição SE e um operador logico >=
    print(numero1)
elif(numero1 == 2): #junção de SENAO + SE, tornando SENAO SE, com o operador logico ==
    print(numero1)
else:               # O ELSE NAO TEM CONDIÇÃO, SOMENTE SERA MOSTRADA SE TODAS AS CONDIÇÕES ANTERIORES FOREM FALSAS
    print("numero invalido")

#estruturas de REPETIÇÃO
#existem 3 estruturas principais de repetição, FOR, WHILE, MATCH_CASE


#O for pode ser entendido em portugues como para_faça, ou seja, para contador na faixa de (0,10), passo 1 por padrão, faça:
for contador in range(0,10): # in range significa que ele vai comecar a contar de 0 a 10(9 numeros, ele nao chega no 10, sempre conta 1 antes) 
                             # a passo 1 por padrão, 
    print(contador)             
    
for contador in range(10,0,-1): #aqui ele começa do 10 e vai até o 0 (9 numeros), a passo -1 
    print(contador)             
    
#O while pode ser entendido como enquanto, traduzindo para portugues, enquanto o contador for menor ou igual a 10, repita
while(contador <=10):
    print(contador)
    contador +=1 # importante trecho do while, ele precisa incrementar o contador para que assim que o contador for igual a 10, ele pare a repetição

while(contador == True): #aqui um pouco mais complexo, o contador vai receber o valor booleano True
                         #enquanto eu nao estipular que o contador é falso, a estrutura vai se repetir infinitamente
      print(contador)
      contador +=1       #aqui eu incremento +1 no contador para que entre na estrutura de CONDIÇÃO
      if(contador == 5): 
          break     # aqui eu defino que assim que o contador chegar a 5, eu paro a estrutura de repetição
        #contador = False # tem o mesmo efeito do break    

#O Match_Case pode ser entendido como, Caso encontre um igual       

dias = [1,2,3,4,5]
match(dias):
    case 1: #caso o dia for 1
        print("dia 1")
    case 2: #caso o dia for 2
        print("dia 2")
    case 3: #caso o dia for 3
        print("dia 3")
    case 4: #caso o dia for 4
        print("dia 4")
    case 5: #caso o dia for 5
        print("dia 5")
    case _ : #caso o dia nao for nenhum desses
        print("dia invalido")

# Eu tambem posso pegar o valor digitado pelo usuario

opcaoMatchCase = int(input("entre com um numero de 1 a 5"))

match(opcaoMatchCase):
    case 1: #caso  1
        print("numero 1")
    case 2: #caso  2
        print("numero 2")
    case 3: #caso  3
        print("numero 3")
    case 4: #caso  4
        print("numero 4")
    case 5: #caso 5
        print("numero 5")
    case _ : #casonao for nenhum desses  # O simbolo _ "underscore" representa nenhum dos valores a cima
        print("invalido")

#continuação agora do segundo semestre
# funções internas ou (embutidas) ou builtin no python
#basicamente são as funções que já estão no próprio python
print("Funções internas - builtin ou embutidas")

maior_numero = max(5.5, 5.6, 5.7, 8.3) 
menor_numero = min(3, 6, 7, 10) 
maior_letra = max('a', 'b', 'c') 
menor_letra = min('a', 'b', 'c')

print("O Nro maximo da lista =", maior_numero) 
print("O Nro minimo da lista =", menor_numero) 
print("A maior letra da lista =", maior_letra) 
print("A menor letra da lista =", menor_letra)

nome = "henrique" 
nome.lower() 
nome.upper() 
nome.capitalize()

print("Nome em Upper case = " + nome.upper()) 
print("Nome em Lower case =" + nome.lower()) 
print("1ra letra com Maiscula = " + nome.capitalize())


len("é usado para contar quantos caracteres tem em um objeto")
# Exemplo com uma string
minha_string = "Olá, mundo!"
comprimento_da_string = len(minha_string) #voce coloca entre os colchetes aquilo que vc quer contar
print("A string tem", comprimento_da_string, "caracteres.")

# Exemplo com uma lista
minha_lista = [1, 2, 3, 4, 5]
comprimento_da_lista = len(minha_lista)
print("A lista tem", comprimento_da_lista, "elementos.")

#Em Python, a declaração import é usada para incluir módulos ou pacotes em seu programa. 
# Importando um módulo (math)
import math

raiz = math.sqrt(9)
print("Funções do modulo math")
print("Valor da raiz de 9%.2f = " %raiz)
print("Valor de Pi= ", math.pi)

Pi = math.pi

print("Valor de Pi = %.4f" %Pi)
print("Valor de e =",math.e)

seno= math.sin(math.radians(90))

print("Valor do senho de 90 Graus =", seno) # seno de 90 graus

#outro módulo seria o (random)
#utilizamos esse módulo para gerar numeros aleatórios 
#Geração de Números Aleatórios:
import random
num_aleatorio = random.random()
print(num_aleatorio)

#randrange(start, stop, step): Retorna um número aleatório de acordo com os parâmetros especificados (semelhante ao range()).

num_aleatorio = random.randrange(1, 10, 2)  # Número ímpar entre 1 e 10
print(num_aleatorio)

#Em Python, uma função é um bloco de código reutilizável que realiza uma tarefa específica. 
# Funções permitem organizar o código, torná-lo mais legível e modular, 
# além de facilitar a manutenção e a reutilização de trechos específicos de lógica.
def nome_da_funcao(parametro1, parametro2,):
    # Corpo da função
    # Código que realiza a tarefa desejada
    # Pode incluir instruções condicionais, loops, etc.
    
    # Opcional: Retornar um valor
    return "resultado"
#def: É a palavra-chave que indica o início da definição de uma função.
#nome_da_funcao: É o nome dado à função. Este nome deve seguir as mesmas regras que as variáveis em Python.
#parametro1, parametro2, ...: São os parâmetros que a função pode aceitar. 
# Eles são opcionais, e uma função pode não ter nenhum parâmetro.
#  ':'  Indica o início do bloco de código da função.
def soma(a, b):
    resultado = a + b
    return resultado
#Você pode chamar essa função fornecendo valores específicos para a e `b:
resultado_da_soma = soma(3, 5)
print(resultado_da_soma)  # Saída: 8

#Além disso, uma função pode ou não retornar um valor. Se a função não tiver uma instrução return, ela retornará automaticamente None. 
# No entanto, é comum usar return para devolver um resultado específico.
def saudacao(nome):
    mensagem = "Olá, " + nome + "!"
    print(mensagem)

# Chamando a função
saudacao("Alice")
# Saída: Olá, Alice!

#concatenar
#concatenação de 2 trechos de texto texto 1 = "123" texto2 = "456"

concatenacao = texto1 + texto2 
print("Resultado da variavel concatenação = " +concatenacao) # Saida = '123456

#declaração da variável 'a' que foi associado ao texto 'bra' 
a = "bra"

#declaração da variável 'b' que foi associado ao texto 'sil' 
b = "sil"

#ao escrevemos no prompt a + b temos que é impresso a CONCATENAÇÃO 
print("concatenação de a + b = " + (a+b)) #Saida = 'brasil'

#agora, concatenamos e o resultado associamos a variável 'c' 
c=a+b 
print("Resutado da variavel c = " + c) #Saida = 'brasil'

#agora, podemos dizer que o trecho de texto 'bra'

# foi adicionado a esquerda da variável 'b' 
print("concatenação de b + a = " +(b+a)) #Saida 'silbra

#interpolar
#Interpolar é a inserção de um trecho de texto dentro de outro.

#A interpolação, ocorre de várias formas, e, 
# algumas linguagens e bibliotecas proporcionam maneiras bastante interessantes e diferentes para interpolarmos valores.
sexo = "masculino"

nome = "Henrique"

interpolar = "Sexo é igual a %s e o nome é igual %s "%(sexo, nome)
print("Saida 1 da interpolação = " +interpolar)  

#agora, vamos colocar uma string entre chaves dentro do texto

#em seguida, com a função format(), vamos associar

#os nomes definidos entre chaves a texto passando-os

#como argumentos de função

interpolar = "Sexo é igual a {SEXO} e o nome é igual {NOME}".format(SEXO=sexo, NOME=nome)
print("Saida 2 da interpolação = " +interpolar)

#Saida = 'Sexo é igual a masculino e o nome é igual Henrique '
#LEMBRANDO QUE UMA STRING DECLARADA NÃO PODE SER ALTERADA 









