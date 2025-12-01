def compter_lettres_chiffres(chaine):
    lettres = 0
    chiffres = 0

    for caractere in chaine:
        if caractere.isalpha():
            lettres += 1
        elif caractere.isdigit():
            chiffres += 1

    return lettres, chiffres

chaine = "IPSSI69007"
lettres, chiffres = compter_lettres_chiffres(chaine)
print(f"Lettres {lettres}")
print(f"Chiffres {chiffres}")
