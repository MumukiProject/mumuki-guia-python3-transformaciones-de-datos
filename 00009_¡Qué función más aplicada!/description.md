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


> ¡Tu turno! Queremos estimar cuánto dinero se ingresó al país a través de cruceristas procedentes del extranjero. El mismo lo calcularemos como: 
>
>  * 0, para cruceristas provenientes de Uruguay
>  * la cantidad de personas en el grupo de cada crucerista (`total_people`), multiplicado por el gasto total (`total_expenses`), en cualquier otro caso
> 
> Agregá a `cruceristas` una columna `estimated_foreign_income` con esta estimación.
