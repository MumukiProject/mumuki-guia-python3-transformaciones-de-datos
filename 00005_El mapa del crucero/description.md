La primera forma que vamos a conocer para crear columnas es a partir de la transformación de una columna actual utilizando `map` 🗺️. Si por ejemplo quisiéramos distinguir en nuestro lote los cines públicos, privados y comunitarios e independientes en una nueva columna `sector_type` podríamos hacer esto:

```python
cines["sector_type"] = cines["sector"].map({
    "Público municipal": "Público", 
    "Público provincial": "Público", 
    "Público nacional": "Público", 
    "Privado comercial": "Privado", 
    "Otros": "Comunitarios e Independientes",
    "Privado independiente": "Comunitarios e Independientes",
    "Privado comunitario": "Comunitarios e Independientes"})
```

En caso que no hayamos contemplado algún valor de entrada tendremos `nan` en la columna. Por ejemplo, si omitíamos `"Público nacional"` en nuestro `map`, el `sector_type` quedaría como `nan` en las filas correspondientes a ese sector. 

> ¡Probémoslo! Escribí una expresión que te permita crear la columna `region` en nuestro `DataFrame`  con el valor `"Nacional"` para los cruceros de Uruguay 🇺🇾 y  `"Regional"` para aquellos de Argentina 🇦🇷 y Brasil 🇧🇷. No nos vamos a preocupar por el resto de países por ahora. 
