def a_binario(n: int) -> str:
    binario = ""
    while (n != 0):
        residuo = n % 2
        binario += str(residuo)
        n = n // 2
    return binario[::-1]

def binario_a_decimal(binario: str) -> int:
    sum = 0
    binario = binario[::-1]
    for i in range(len(binario)):
       digito = int(binario[i])
       if digito == 1:
        sum += 2**i
    return sum
    
def a_hexadecimal(n: int) -> str:
    digitos_hexadecimales = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    hexadecimal = ""
    while (n != 0):
        residuo = n % 16
        hexadecimal += digitos_hexadecimales[residuo]
        n = n // 16
    return hexadecimal[::-1]

def hexadecimal_a_decimal(hexadecimal: str) -> int:
    digitos_hexadecimales = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    sum = 0
    hexadecimal = hexadecimal[::-1]
    for i in range(len(hexadecimal)):
        digito = digitos_hexadecimales[hexadecimal[i]]
        sum += digito*16**i
    return sum

def a_decimal(n: str, base: int):
    if base != 2 and base != 16:
        raise ValueError("a_decimal: solo bases 2 y 16 permitidas")

    if base == 2:
        return binario_a_decimal(n)
    else:
        return hexadecimal_a_decimal(n)
    
if __name__ == "__main__":
    n = 16
    binario = a_binario(n)
    hexadecimal = a_hexadecimal(n)
    print(binario)
    print(a_decimal(binario, 2))
    print(hexadecimal)
    print(a_decimal(hexadecimal, 16))
