En caso de que queramos utilizar operaciones más complejas en nuestras columnas contamos con `apply`, que aplica una función a cada valor de nuestro `Series`. ¡Eso nos va a permitir generar columnas más interesantes! 

Por ejemplo, si tenemos el siguiente lote...

name|birth_date|
---|---|
Gustavo|08/03/1992|
Graciela|05/11/1959|
Jorge|04/06/1957|

...almacenado en una variable `personas` y hacemos...

```python
personas["age"] = personas["birth_date"].apply(get_zodiac_sign)
```

...`personas` quedaría así:

name|birth_date|zodiac_sign
---|---|---|
Gustavo|08/03/1992|Pisces|
Graciela|05/11/1959|Scorpius|
Jorge|04/06/1957|Gemini|

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
