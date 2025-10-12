def fibonacci(n):
    # returns fibonacci series in a list
    a, b = 0, 1
    fib = []
    while a < n :
        fib.append(a)
        a, b = b, a+b

    return fib


def classer(classeur, nombre):
    # class nombre dans dictionnaire selon le signe
    if nombre >0:
        classeur['positif'].append(nombre)
    else:
        classeur['negatif'].append(nombre)
    
    return classer