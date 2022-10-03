`pandas` también nos permite operar entre columnas para generar nuevos `Series` de forma muy similar a lo que aprendimos en el ejercicio anterior. Si quisiéramos una columna que refleje la cantidad de butacas promedio por sala podríamos hacer esto:

```python
cines["average_seats_per_screen"] = cines["seats"] / cines["screens"] 
```

Al operar entre columnas lo que sucede es que se van operando los valores de cada una por fila, lo que nos deja como resultado algo así:

seats|screens|average_seats_per_screen|
---|---|---|
1000|4|250|
1500|3|500|
800|2|400|

> ¡Es tu turno! Generá la columna `total_expenses` que sea la suma de todas las columnas de gastos de nuestro `DataFrame`.
