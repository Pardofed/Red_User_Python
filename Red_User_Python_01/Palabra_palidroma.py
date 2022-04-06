Cadena1 = input("Introducir una cadena: ")
Cadena_al_reves = Cadena1[: :-1]
print(Cadena_al_reves)
if (Cadena_al_reves == Cadena1):
    print("Es una palabra palindromo")
else:
    print("No es palindromo")