cadenas = input() .split()
resultado =[]
    
for i in range(0,len(cadenas),2):
        if len(cadenas[i]) >= 5:
              resultado += [cadenas[i]]
print(resultado)