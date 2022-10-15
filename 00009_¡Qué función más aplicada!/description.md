En caso de que queramos utilizar operaciones más complejas en nuestras columnas contamos con `apply`, que aplica una función a cada valor de nuestro `Series`. ¡Eso nos va a permitir generar columnas más interesantes! 

Por ejemplo, si tenemos el siguiente lote...

name|birth_date|
---|---|
Dani|08/03/1991|
Umi|05/11/1982|
Feli|04/06/1957|

...almacenado en una variable `personas` y hacemos...

```python
personas["age"] = personas["birth_date"].apply(get_decade)
```

...`personas` quedaría así:

name|birth_date|decade
---|---|---|
Dani|08/03/1991|1990|
Umi|05/11/1982|1980|
Feli|04/06/1957|1950|

¡Pongámoslo a prueba!


> Utilizando `apply` y la función `get_continent` crea una columna `continent`. La función `get_continent` ya la definimos por vos y retorna un continente a partir de un país:
>
>```python
get_continent("Brasil")
"América"
>
get_continent("China")
"Asia"
> 
> 
