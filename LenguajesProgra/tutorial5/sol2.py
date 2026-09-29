w = input().split()
resultado = []

for ele in w:
    if len(ele) <= 4:
        resultado += [ele]

print(resultado)