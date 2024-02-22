# admin, user, guest

rule = input("Digite seu cargo: ")

if rule == "admin":
    print("Acesso total")
elif rule == "user":
    print("Acesso limitado")
elif rule == "guest":
    print("Acesso mínimo")
else:
    print("Acesso negado")