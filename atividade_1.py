#imprimir todos os números exceto o 13( laço for in rage)
for i in range(1,21):
    if i == 13:
        continue
    print(i)

 # imprimir todos os números exceto o 13( laço while)
    i = 1
    while i < 21:
        if i == 13:
            i += 1
            continue
        print(i)
        i += 1

# imprimir todos os números exceto o 13( em ordem descrescente)

for i in range(20, 0, -1):
        if i == 13:
          continue
        print(i)



