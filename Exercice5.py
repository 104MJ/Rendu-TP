
resultats = []


for x in range(1500, 2701):
    if x % 7 == 0 and x % 5 == 0:
        resultats.append(x)


for i in range(len(resultats)):

    if i > 0 and i % 12 == 0:
        print() 
    print(resultats[i], end=', ' if i < len(resultats) - 1 else '')

print()