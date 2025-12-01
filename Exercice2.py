def mediane(a,b,c):
    if(a>=b and a<=c) or (a<=b and a>=c):
        return a
    elif(b>=a and b<=c) or (b<=a and b>=c):
        return b
    else:
        return c


nombre_1 = int(input("Entrez le premier nombre:"))
nombre_2 = int(input("Entrez le second:"))
nombre_3 = int(input("Entrez le dernier:"""))

trouver_median = mediane(nombre_1, nombre_2, nombre_3)
print(f"le nombre median est : {trouver_median}")
