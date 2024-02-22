# Operadores de comparação / relacionais

# Igual a: ==
# Diferente de: !=
# Maior que: >
# Menor que: <
# Maior ou igual a: >=
# Menor ou igual a: <=

a = 3
b = 3

print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")


age = 150

print(age)
if age < 18 and age > 0:
    print("Menor de idade")
elif age >= 18 and age < 150:
    print("Maior de idade")
else:
    print("Idade não encontrada")