# Estrutura de Dados - Listas

# Listas

# Listas são coleções de itens em uma ordem específica. Podem conter qualquer tipo de dado, inclusive outras listas.
# A lista é definida por colchetes [] e os itens são separados por vírgula.

empty_list = []
print(empty_list)

# Lista de números inteiros
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[0]) # Os indices começam em 0 e avançam de 1 em 1
print(numbers[1])
print(numbers[4])
print(numbers[-1]) # O índice -1 retorna o último item da lista

# Lista de strings
names = ["Ana", "Bia", "Carlos", "Daniel"]
print(names)
print(names[0])
print(names[-1])
print(names[2])

# Lista de tipos diferentes
mixed = [1, "Ana", 3.14, True]
print(mixed)
print(mixed[0])
print(mixed[1])
print(mixed[2])
print(mixed[3])

# Lista de listas
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_of_lists)
print(list_of_lists[0])
print(list_of_lists[2])

print(list_of_lists[0][0])
print(list_of_lists[1][-1])

# Adicionando itens a uma lista
# O método append() adiciona um item ao final da lista
print(names)
names.append("Eduardo")
print(names)

# Removendo itens de uma lista
# O método pop() remove o último item da lista
print(names)
print(names.pop())
print(names)

# O método pop() pode receber um índice como argumento
print(names)
print(names.pop(1))
print(names)

# O método remove() remove o primeiro item da lista que corresponde ao argumento
print(names)
names.remove("Carlos")
print(names)

# O método del remove um item da lista pelo índice
print(names)
del names[0]
print(names)

names.append("Ana")
names.append("Bia")
names.append("Carlos")
names.append("Daniel")
names.append("Eduardo")

# Limpar uma lista
# O método clear() remove todos os itens da lista
print(names)
print(names.clear())
print(names)

# Ordenar uma lista
# O método sort() ordena os itens de uma lista
numbers = [5, 3, 2, 4, 1]
print(numbers)
numbers.sort()
print(numbers)

# O método sort() pode receber o argumento reverse=True para ordenar a lista em ordem decrescente
numbers.sort(reverse=True)
print(numbers)

# O método sort() não funciona com listas que contém tipos diferentes
mixed.sort()
print(mixed)