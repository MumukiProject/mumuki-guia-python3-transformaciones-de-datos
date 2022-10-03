¡Impecable! 👏

En este caso que solo tenemos números enteros en nuestra columna también podríamos hacer:

```python
cruceros["total_people"] = cruceros["total_people"].astype(int)
```
Es importante tener en cuenta que esta opción transforma nuestros datos a `int` y no nos serviría si tenemos strings con números decimales. 

[Acá](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html) podés encontrar la documentación por si querés saber más sobre `astype`.
