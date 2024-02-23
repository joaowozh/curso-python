# Estrutura de Dados - Dicionários

# Dicionários

# Dicionários são coleções de itens em uma ordem específica. Cada item é composto por um par chave-valor.
# A chave é um identificador único e o valor é o item associado à chave.

# Dicionários são definidos por chaves {} e os itens são separados por vírgula.
# Cada item é composto por uma chave e um valor, separados por dois pontos :

# Dicionários são mutáveis, ou seja, os itens podem ser alterados, adicionados ou removidos.

# Dicionários podem conter qualquer tipo de dado, inclusive outros dicionários.

empty_dict = {}
print(empty_dict)

# Dicionário de números, onde as chaves são números inteiros e os valores são strings
numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
print(numbers)

# Dicionário de strings, onde as chaves são strings e os valores são números inteiros
names = {"Ana": 1, "Bia": 2, "Carlos": 3, "Daniel": 4}
print(names)

user = {"name": "Ana", "age": 25, "email": "ana@mail.com", "phone": "123456789"}
print(user)
print(user["name"])
print(user["age"])

# Adicionando itens a um dicionário
# Basta atribuir um valor a uma chave que não existe
print(user)
user["city"] = "São Paulo"
print(user)

# Modificar um valor de um dicionário
# Basta atribuir um novo valor a uma chave que já existe
print(user)
user["age"] = 26
print(user)

# Removendo itens de um dicionário
# O método pop() remove o item associado a uma chave
print(user)
print(user.pop("age"))
print(user)

# O método pop() pode receber um segundo argumento, que é retornado caso a chave não exista
print(user)
print(user.pop("age", "Chave não existe"))
print(user)

# O método popitem() remove o último item do dicionário
print(user)
print(user.popitem())
print(user)