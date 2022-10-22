`pandas` también nos permite operar entre columnas para generar nuevos `Series` de forma muy similar a lo que aprendimos en el ejercicio anterior. Por ejemplo, si a partir de nuestra hipotética tabla de paises....


|country|population|area|
|---|---|---|
|Argentina|39921833|2780400|
|Bolivia|8989046|1098581|
|Brazil|188078227|8515770|
|Chile|16134219|756102|
|Colombia|43593035|1141748|
|Mexico|107449525|1964375|

...quisiéramos generar una columna de densidad poblacional (expresada en habitantes/km²), podríamos hacer lo siguiente:

```python
paises["population_density"] = paises["population"] / cines["area"] 
```

|country|population|area|
|---|---|---|
|Argentina|39921833|2780400|
|Bolivia|8989046|1098581|
|Brazil|188078227|8515770|
|Chile|16134219|756102|
|Colombia|43593035|1141748|
|Mexico|107449525|1964375|


> ¡Es tu turno! Generá la columna `total_expenses` que sea la suma de todas las columnas de gastos de nuestro `DataFrame`.
