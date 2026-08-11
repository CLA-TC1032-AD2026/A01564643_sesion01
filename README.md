# Sesión 1: Introducción a la arquitectura de computadoras y sistemas numéricos

## Objetivos de aprendizaje

Al finalizar esta sesión serás capaz de:

- Ubicar la evolución histórica de las computadoras por generaciones tecnológicas.
- Identificar los componentes básicos de una computadora y su función.
- Convertir números entre las bases decimal, binaria y hexadecimal, manualmente y en Python.

## 1. Evolución de las computadoras

La evolución de las computadoras suele dividirse en generaciones, definidas por el cambio en la tecnología con la que se construyen sus componentes:

| Generación | Tecnología | Periodo aproximado | Ejemplo |
|---|---|---|---|
| 1ª | Bulbos / tubos de vacío | 1940s–1950s | ENIAC |
| 2ª | Transistores | 1950s–1960s | IBM 7090 |
| 3ª | Circuitos integrados (SSI/MSI) | 1960s–1970s | IBM System/360 |
| 4ª | Microprocesadores (VLSI) | 1970s–presente | Intel 4004, PC modernas |
| 5ª (en discusión) | Múltiples núcleos, IA, computación cuántica | 2000s–presente | CPUs multi-core actuales |

Cada generación redujo el tamaño y costo, y aumentó la velocidad y confiabilidad de los sistemas, lo que permitió pasar de máquinas del tamaño de un cuarto a los procesadores multinúcleo que hoy caben en un teléfono.

## 2. Componentes básicos de la computadora

Toda computadora, sin importar su tamaño, está compuesta por cuatro subsistemas funcionales:

- **Unidad Central de Procesamiento (CPU):** ejecuta instrucciones. Contiene la Unidad Aritmético-Lógica (ALU), la Unidad de Control (UC) y un conjunto de registros.
- **Memoria:** almacena instrucciones y datos, tanto de forma temporal (memoria principal, RAM) como permanente (memoria secundaria, discos).
- **Entrada/Salida (E/S):** permite la comunicación con el exterior (teclado, pantalla, red, almacenamiento).
- **Buses:** canales de comunicación entre los componentes anteriores. Se distinguen tres tipos: bus de datos, bus de direcciones y bus de control.

Este esquema de cuatro bloques es la base de la arquitectura de Von Neumann, que se estudiará a detalle en la Sesión 3.

## 3. Sistemas numéricos y conversión de bases

Una computadora representa toda la información, ya sean números, texto o imágenes, usando el sistema **binario** (base 2), porque sus componentes electrónicos solo distinguen dos estados (encendido/apagado). Sin embargo, para que los humanos trabajemos más cómodo, usamos también la base **decimal** (base 10) y la base **hexadecimal** (base 16).

### 3.1 Notación posicional

En un sistema posicional de base *b*, un número se representa como una secuencia de dígitos donde cada posición tiene un peso *b^i*:

```
(d_n d_{n-1} ... d_1 d_0)_b = d_n·b^n + d_{n-1}·b^{n-1} + ... + d_1·b^1 + d_0·b^0
```

### 3.2 Conversión decimal → binario / hexadecimal (divisiones sucesivas)

Se divide el número entre la base destino, se registra el residuo, y se repite con el cociente hasta llegar a 0. El número resultante se lee de abajo hacia arriba (del último residuo al primero).

**Ejemplo:** convertir 156 (decimal) a binario.

```
156 ÷ 2 = 78  residuo 0
 78 ÷ 2 = 39  residuo 0
 39 ÷ 2 = 19  residuo 1
 19 ÷ 2 =  9  residuo 1
  9 ÷ 2 =  4  residuo 1
  4 ÷ 2 =  2  residuo 0
  2 ÷ 2 =  1  residuo 0
  1 ÷ 2 =  0  residuo 1
```

Leyendo los residuos de abajo hacia arriba: **156 = 10011100₂**

### 3.3 Conversión binario ↔ hexadecimal (agrupación de bits)

Como 16 = 2⁴, cada dígito hexadecimal corresponde exactamente a 4 bits. Para convertir binario a hexadecimal, se agrupan los bits de 4 en 4 desde el punto (o desde la derecha si es entero), y se traduce cada grupo:

```
10011100₂ = 1001 1100 = 9   C  → 9C₁₆
```

**Aplicación cotidiana: colores en HTML/CSS**

Los colores en HTML y CSS se escriben en hexadecimal con el formato `#RRGGBB`, donde cada par de dígitos hex representa un byte (8 bits) para un canal de color: rojo, verde y azul, con valores de 00 a FF (0 a 255 en decimal).

```
#FF5733
  FF → rojo   = 255
  57 → verde  =  87
  33 → azul   =  51
```

Cada canal ocupa exactamente 2 dígitos hexadecimales porque 2 dígitos hex = 8 bits = 1 byte, el mismo principio de agrupación que se usó arriba con 9C₁₆.

### 3.4 Conversión base → decimal

Se suma cada dígito multiplicado por el peso de su posición:

```
9C₁₆ = 9·16¹ + 12·16⁰ = 144 + 12 = 156₁₀
```

## 4. Ejercicios manuales (entregar procedimiento completo)

1. Convierte 214 (decimal) a binario y a hexadecimal, mostrando el procedimiento de divisiones sucesivas.
2. Convierte 11010110₂ a decimal y a hexadecimal.
3. Convierte 2F₁₆ a decimal y a binario.
4. Explica, en tus propias palabras, por qué la agrupación de 4 bits funciona para convertir entre binario y hexadecimal, pero no funcionaría directamente para convertir entre binario y decimal.

## 5. Práctica en Python (GitHub Codespaces)

En este repositorio trabajarás dentro de un Codespace. Abre una terminal y crea un archivo `sesion01.py`. La idea de esta práctica es programar **tú mismo** el algoritmo de conversión, sin usar las funciones nativas `bin()` o `hex()` (esas solo se usan para verificar tu resultado).

```python
def a_binario(n: int) -> str:
    """Convierte un entero no negativo a su representación binaria (str), sin usar bin()."""
    # TODO: implementar usando divisiones sucesivas
    pass

def a_hexadecimal(n: int) -> str:
    """Convierte un entero no negativo a su representación hexadecimal (str), sin usar hex()."""
    # TODO: implementar usando divisiones sucesivas
    pass

if __name__ == "__main__":
    n = 156
    print(f"{n} en binario: {a_binario(n)}  (verificación: {bin(n)})")
    print(f"{n} en hexadecimal: {a_hexadecimal(n)}  (verificación: {hex(n)})")
```

### Ejercicios en Python

5. Completa las funciones `a_binario(n)` y `a_hexadecimal(n)` del archivo `sesion01.py` sin usar `bin()`/`hex()` en la lógica de conversión (solo para verificar el resultado final).
6. Agrega una función `a_decimal(cadena: str, base: int) -> int` que reciba un número representado como cadena en una base dada (2, 8 o 16) y regrese su valor decimal. Prueba tu función con al menos 3 casos.


## Recursos

- Tanenbaum, A. S., *Structured computer organization*, 6ª ed., Capítulo 1 (introducción) y Apéndice B (sistemas numéricos).

## Próxima sesión

Sesión 2: complementos, enteros con signo y aritmética binaria.
