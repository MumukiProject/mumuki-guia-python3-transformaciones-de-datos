Otro problema muy común a la hora de trabajar con datos (y programando en general) es el de formatos y tipos de fechas. Si bien existen tipos de datos específicos para fechas, frecuentemente se almacenan como strings. Por suerte, una vez más, `pandas` tiene la solución con `to_datetime`. ¿Te imaginás que hace?

> Respondé qué afirmaciones son correctas luego de probar en en tu cuaderno las siguientes expresiones en orden:
>
```python
cruceros.info()
```
>
```python
cruceros["date"] = pd.to_datetime(cruceros["date"])
```
>
```python
cruceros.info()
```

* Antes de hacer `to_datetime`, los valores de la columna `date` eran de tipo `object`.
* Antes de hacer `to_datetime`, los valores de la columna `date` eran de tipo `datetime64`.
* Luego de hacer `to_datetime`, los valores de la columna `date` son de tipo `object`.
* Luego de hacer `to_datetime`, los valores de la columna `date` son de tipo `datetime64`.
