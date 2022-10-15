A lo largo de esta lección ya modificamos muchos `DataFrame`s ¡pero aún no creamos uno desde cero! Para eso, escribiremos `pd.DataFrame()`` y luego le iremos agregando las columnas que queremos. 

Por ejemplo, con el siguiente código:

```python
publicos = cines[cines["sector"] == "Público"]
privados = cines[cines["sector"] == "Privado"]
privados_vs_publicos = pd.DataFrame()
privados_vs_publicos["privados"] = pd.value_counts(privados.screens)
privados_vs_publicos["publicos"] = pd.value_counts(publicos.screens)
privados_vs_publicos
```

Obtendríamos un `DataFrame` de este estilo:

||privados|públicos|
---|---|---|
1|91|66|
2|43|5|
3|21|2|
4|14|NaN|
5|15|NaN|
(..)|(..)|(..)

Que nos permite comparar fácilmente la cantidad de pantallas de cines privados y públicos. En este caso podemos decir que tenemos 91 cines privados y 66 públicos con 1 pantalla. También que no tenemos cines públicos con 4 o 5 pantallas. 

¡Ahora te toca a vos!

> A partir del lote de datos sobre el distrito tecnológico de uenos Aires que podés encontrar [acá](https://docs.google.com/spreadsheets/d/e/2PACX-1vRSa9oM9fC-QlT7VOeGhZQtrWnlNSTsk3U8DWGTOXUWtPH6u9o5O5eZ0kTg8mFTwAn9vMdGRK7o2SPB/pub?gid=1178503202&single=true&output=csv), creá en tu cuaderno un `DataFrame` que contenga cuántas empresas de software y cuántas de hardware iniciaron sus actividades por año.
>
> Luego contestá las siguientes preguntas:
