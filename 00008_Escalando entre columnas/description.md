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

> ¡Es tu turno! :glasses: Observá que `cruceristas` cuenta con una columna `total_expenses`, pero ¿informará realmente la cantidad total de gastos? ¿Habrá casos en que los gastos totales contenidos en ella no sean consistentes con la suma de los gastos detallados? :mag: Para averiguarlo, generá una columna `actual_total_expenses` con la suma de todos los gastos y respondé:  
> 
>  1. ¿En cuántas filas la diferencia entre  `actual_total_expenses` y `total_expenses` es mayor a cero?
>  1. ¿En cuántas filas la diferencia entre  estas dos columnas es, en términos absolutos, mayor a 50USD?
>  1. ¿Cuál es la mayor diferencia, en términos absolutos entre estas dos columnas?
>
> :bulb: ¿Qué conclusiones podés sacar?
