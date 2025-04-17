# Condicionais

"""
-> Condicional Simples
if condição:
    comando1
    comando2
--------------------------------
-> Condicional Composta
if condição
    comando1
    comando2
else:
    comando1
    comando2
--------------------------------
-> Condicional Encadeada
if condição1:
    comando1
    comando2
elif condição2:
    comando3
    comando4
else:
    comando5
    comando6
--------------------------------
-> Operadores Aritméticos
+ => Adição
- => Subtração
* => Multiplicação
/ => Divisão
% => Resto da Divisão
** => Potenciação
// => Divisão inteira
--------------------------------
-> Operadores Comparativos
< - Menor que
> - Maior que
<= - Menor ou igual
>= - Maior ou igual
== - Igual a
!= ou <> - Diferente de
--------------------------------
-> Operadores Lógicos
and
or
not

"""

# Condicional Simples
"""hora = int(input("Digite uma hora do dia: "))

if hora <= 12:
    print("Bom dia!")
else:
    print("Boa tarde!")"""


"""var1 = int(input("Digite um valor: "))
var2 = int(input("Digite um segundo valor: "))

if var1 != var2:
    print("\n-> Os valores não são iguais")
    if var1 > var2:
        print(f"-> O primeiro número: {var1} é maior que o segundo número: {var2}")
    else:
        print(f"->O segundo número: {var2} é maior que o primeiro número: {var1}")
else:
    print("-> Os valores são iguais")"""

"""var1 = int(input("Digite um valor: "))

if var1 % 2 == 0:
    print("O número é par!")
else:
    print("O número é ímpar")"""