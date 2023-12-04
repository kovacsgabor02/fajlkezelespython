def hetedik():
    lista = []
    beFajl = open("fileok/forditott.txt", "r", encoding="utf-8")
    for sor in beFajl:
        lista.append(sor.strip())
    beFajl.close()

    # lista kiírása
    kiFajl = open("fileok/negyedik2.txt", "w", encoding="utf-8")
    for index in range(0, len(lista),-1, -1, -1):
        print(lista[index])
        print(lista[index], file=kiFajl)
        # a sorokat eldarabolom szóközök mentén egy listába
