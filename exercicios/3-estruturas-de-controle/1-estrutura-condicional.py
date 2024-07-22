# Declare 4 variáveis do tipo numérica

a = 4
b = 30
y = 3
x = 36

# Crie uma estrutura condicional para comparar dois números

if x < y:
    print(True)
else:
    print(False)

# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor

if x > y:
    print(f'A condição foi cumprida. O número {x} é maior do que {y}')
else:
    print(False)

# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor

if x > y:
    print(f'A condição foi cumprida. O número {x} é maior do que {y}')
else:
    print(f'A condição não foi cumprida. Na verdade, o número {y} é maior do que {x}')

# Insira outras condições na estrutura condicional usando o elif

if x < y:
    print(f'A condição foi cumprida. O número {y} é maior do que {x}')
elif x > a:
    print(f'Nesse caso, verificamos que o número {x} é maior do que {a}')
else:
    print(f'A condição não foi cumprida. Na verdade, o número {y} é maior do que {x}')

# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"

if (x < y) or (x < a):
    print(f'A condição foi cumprida. O número {x} é maior do que {y} ou maior do que {a}')
elif (x == a) and (b > y):
    print(f'Nesse caso, verificamos que o número {x} é maior do que {a}')
else:
    print(f'Nenhuma das condições anteriores foram cumpridas.')

# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"

if y < a:
    print(f'A condição foi cumprida. O número {a} é maior do que {y}')
if b < x:
    print(f'Nesse caso, verificamos que o número {x} é maior do que {b}')