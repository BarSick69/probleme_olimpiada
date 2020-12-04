x=int(input("dati numarul total de pasari: "))
g=x//2
r=g//4
gas=x-g-r
if(g>0 and r >0 and gas>0):
    print(f"sunt {g} gaini,{r} rate si {gas} gaste")
else:
    print("nu sunt destule pasari")