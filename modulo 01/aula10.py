# Funções
#
# Funções são blocos de código que realizam uma tarefa específica.
# Funções podem receber argumentos e retornar valores.
# Funções são definidas pela palavra-chave def.

# Exemplo de função super usada: print()
print("Olá, mundo!")

# Função soma()
def soma():
    return 10 + 10

print(soma())

# Função soma() com argumentos
def soma(a, b):
    return a + b

print(soma(10, 100))

# Função soma() com argumentos padrão
def soma(a=10, b=10):
    return a + b

print(soma())
print(soma(100))
print(soma(100, 100))
print(soma(b=200))

print("--------------------")

# Escopo de variáveis

a = 10 # Variável global

def multiply():
    return a * 5

print(multiply())
print(a)

def divide():
    a = 5 # Variável local
    return a / 2

print(divide())
print(a)