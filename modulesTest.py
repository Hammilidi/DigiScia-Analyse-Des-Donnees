PI = 3.14


def addition(number1, number2):
    result = number1+number2
    return result

def soustraction(number1, number2):
    result = number1- number2
    return result

def produit(number1, number2):
    result = number1*number2
    return result

def division(number1, number2):
    if number2 == 0:
        print("Division par 0 impossible")
    else:
        result = number1/number2
        return result