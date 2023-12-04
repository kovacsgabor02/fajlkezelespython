def negyedik():
    # beolvasas
    lista = []
    beFajl = open("fileok/dal.txt", "r", encoding="utf-8")
    for sor in beFajl:
        lista.append(sor.strip())
    beFajl.close()

    # lista kiírása
    kiFajl = open("fileok/negyedik2.txt", "w", encoding="utf-8")
    for index in range(0, len(lista), 1):
        # a sorokat eldarabolom szóközök mentén egy listába
        daraboltSor = lista[index].split(" ")
        print(daraboltSor[0], file=kiFajl)
        # kiFajl.write(lista[index])
    kiFajl.close()
