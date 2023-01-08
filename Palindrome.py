

num = int(input("Ingrese un palindromo: "))
rev = int(str(num)[::-1])
i = 0

while i == 0:
    if num == rev:
        i = 1
    else:
        num = int(input("Ese no era un palindromo: "))
        rev = int(str(num)[::-1])

print("Felicidades, usted  ha ingresado un palindromo")

num += 1
rev = int(str(num)[::-1])

while num != rev:
    num += 1
    rev = int(str(num)[::-1])

print(f"El palindromo más cercano es {num}")