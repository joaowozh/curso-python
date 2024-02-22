# Operadores lógicos
# And, or, not - e, ou, não

# Se pelo menos um dos valores for False, o resultado é False
# A regra geral é, leia a expressão E e se pelo menos um valor for False, o resultado é False
print(f"True and True: {True and True}")
print(f"True and False: {True and False}")
print(f"False and True: {False and True}")
print(f"False and False: {False and False}")
print("-------------------")

# Se pelo menos um dos valores for True, o resultado é True
# A regra geral é, leia a expressão OU e se pelo menos um valor for True, o resultado é True
print(f"True or True: {True or True}")
print(f"True or False: {True or False}")
print(f"False or True: {False or True}")
print(f"False or False: {False or False}")
print("-------------------")

print(f"not True: {not True}")
print(f"not False: {not False}")

valid_password = False

print(f" valid_password: {not valid_password}")