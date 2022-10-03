Otra forma de crear columnas es a partir de operaciones escalares aplicadas a cada uno de sus valores. Veámoslo con un ejemplo; asumamos que:

*  todas las entradas al cine salen 200 pesos;
* por día tenemos 4 funciones por sala;
* queremos una columna que nos permita saber la recaudación máxima total por día.

Podríamos generar la columna `max_daily_income` de la siguiente manera:

```python
cines["max_daily_income"] = cines["seats"] * 200 * 4
```

> ¡Veamos si se entendió! Escribí la expresión que te permita agregar a `cruceros` la columna `shopping_discount`. El valor en cada fila está determinado por el 10% del valor de `shopping_expenses`.
