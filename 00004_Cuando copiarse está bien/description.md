Ya estuvimos eliminando columnas y renombrando otras, ¡ahora vamos a aprender a agregar nuevas!

Sin embargo, antes de pasar a eso vamos a enseñarte a hacer una copia de un `DataFrame`. Si te preguntas para qué, la respuesta es que a veces nos puede interesar preservar un estado particular de un `DataFrame` y hacer modificaciones en una copia del mismo. 

> Para hacerlo pegá el siguiente código en tu cuaderno y luego embarquémonos al siguiente ejercicio 🚢:
>
```python
import pandas as pd
cruceros_originales = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRSa9oM9fC-QlT7VOeGhZQtrWnlNSTsk3U8DWGTOXUWtPH6u9o5O5eZ0kTg8mFTwAn9vMdGRK7o2SPB/pub?gid=751983160&single=true&output=csv")
cruceros = cruceros_originales.copy()
```
