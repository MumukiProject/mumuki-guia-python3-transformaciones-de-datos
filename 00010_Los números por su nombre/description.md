Ahora que ya tenemos columnas nuevas vamos a modificar algunas de las preexistentes. Los lotes de datos pueden ser tramposos y nos puede ocurrir que una columna que contiene números los tenga almacenados como strings. Por suerte, `pandas` nos provee `to_numeric` que transforma un string de un número en... ¡un número!

```python
pd.to_numeric("97")
97
```

¡Y también funciona a nivel columna!

```python
cines["floor"] = pd.to_numeric(cines["floor"])
```
> Sabiendo esto, corrijamos la columna `total_people` para que tenga números en vez de strings.
