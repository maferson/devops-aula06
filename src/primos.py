# Programa em python

def ehprimo(primo):
    for i in range(2, primo+1):
        if i != primo:
            i = primo % i
            if i == 0:
                return False
                break
        else:
            return True
            break


def test():
    N = int(input("Digite um valor: "))
    cont = 0
    num = 2
    a = ""
    while cont <= N:
        if ehprimo(num) is True:
            a = a + str(num)+","
            cont += 1
        num = num + 1
    return a


print(test())
