def devolver_distintos(num1,num2,num3):

    numeros = [num1,num2,num3]

    if sum(numeros) > 15:
        return max(numeros)
    elif sum(numeros) < 10:
        return min(numeros)  
    elif sum(numeros) >= 10 and sum(numeros) <= 15:
        numeros.sort()
        return numeros[1]

print(devolver_distintos(3,2,4))