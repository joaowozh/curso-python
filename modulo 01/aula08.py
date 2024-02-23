# Estrutura de dados - Tuplas

# Tuplas

# Tuplas são coleções de itens em uma ordem específica. Podem conter qualquer tipo de dado, inclusive outras tuplas.
# A tupla é definida por parênteses () e os itens são separados por vírgula.
# Tuplas são imutáveis, ou seja, os itens não podem ser alterados, adicionados ou removidos.

empty_tuple = ()
print(empty_tuple)

# Tupla de números inteiros
numbers = (1, 2, 3, 4, 5)
print(numbers)
print(numbers[0])
print(numbers[1])

# Tupla de strings
names = ("Ana", "Bia", "Carlos", "Daniel")
print(names)
print(names[0])
print(names[-1])

# Tupla de tipos diferentes
mixed = (1, "Ana", 3.14, True)
print(mixed)
print(mixed[0])
print(mixed[1])

# Tupla de tuplas
tuple_of_tuples = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(tuple_of_tuples)
print(tuple_of_tuples[0])
print(tuple_of_tuples[2])
print(tuple_of_tuples[0][0])

# Desempacotamento de tuplas
# O desempacotamento de tuplas é uma forma de atribuir os itens de uma tupla a variáveis
# O número de variáveis deve ser igual ao número de itens da tupla

print(numbers)
a, b, c, d, f = numbers
print(a)
print(b)
print(c)
print(d)
print(f)

# O desempacotamento de tuplas pode ser utilizado para trocar os valores de variáveis
a = 1
b = 2
print(a, b)
a, b = b, a
print(a, b)

# Outros métodos de tuplas
# O método count() retorna o número de vezes que um item aparece na tupla

print(numbers)
print(numbers.count(1))
print(numbers.count(2))

# O método index() retorna o índice da primeira ocorrência de um item na tupla
print(numbers)
print(numbers.index(1))
print(numbers.index(2))
