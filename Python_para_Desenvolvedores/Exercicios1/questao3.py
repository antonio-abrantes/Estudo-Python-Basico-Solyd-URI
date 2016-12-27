def retornaLista(lista):
    if isinstance(lista, list):
        ls = []

        for item in lista:
            ls = ls + retornaLista(item)
        return ls
    else:
        return [lista]

l = [[1, [2]], [3, 4], [[5, 6], 7]]

print(retornaLista(l))

