# Maths Library Functions

Esta librería ofrece funciones básicas de matemáticas que aceptan un número indefinido de argumentos.

## ➕ Suma

Suma uno o más números usando `add_nums`.

```python
>>> from maths import add_nums
>>> add_nums(2, 3, 5)
10
>>> add_nums(1, 2, 3, 4, 5)
35
```

## ➖ Resta

Resta números en secuencia usando `subtract_nums`.  
El primer número es el punto de partida, y los siguientes se van restando.

```python
>>> from maths import subtract_nums
>>> subtract_nums(100, 20, 30, 40)
10
>>> subtract_nums(50, 10, 5)
35
```

## ✖️ Multiplicación

Multiplica uno o más números usando `multiply_nums`.

```python
>>> from maths import multiply_nums
>>> multiply_nums(2, 3, 4)
24
>>> multiply_nums(1, 5, 10)
50
```

## ➗ División

Divide números en secuencia usando `divide_nums`.  
El primer número es el punto de partida, y los siguientes dividen el resultado actual.

```python
>>> from maths import divide_nums
>>> divide_nums(100, 2, 5)
10.0
>>> divide_nums(50, 2, 5)
5.0
```
