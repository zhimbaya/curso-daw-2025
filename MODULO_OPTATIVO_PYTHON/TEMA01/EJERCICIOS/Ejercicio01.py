hola_mundo = "¡Hola, Mundo!"
print(hola_mundo)
#################
'''
| Característica            | `list` (Lista)      | `tuple` (Tupla)      | `set` (Conjunto)     | `dict` (Diccionario)         |
|---------------------------|---------------------|----------------------|----------------------|-------------------------------|
| **Ordenado**              | ✅ Sí               | ✅ Sí                | ❌ No                | ✅ Sí (desde Python 3.7)      |
| **Mutable**               | ✅ Sí               | ❌ No                | ✅ Sí                | ✅ Sí                         |
| **Permite duplicados**    | ✅ Sí               | ✅ Sí                | ❌ No                | ❌ No (claves únicas)         |
| **Indexable**             | ✅ Por posición     | ✅ Por posición      | ❌ No                | ✅ Por clave                  |
| **Sintaxis**              | `[1, 2, 3]`         | `(1, 2, 3)`          | `{1, 2, 3}`          | `{"a": 1, "b": 2}`            |
| **Acceso rápido**         | Por índice          | Por índice           | Por valor (no orden) | Por clave                     |
| **Uso típico**            | Listas dinámicas    | Datos constantes     | Agrupar únicos       | Asociar claves con valores    |
| **Iteración**             | ✅ Sí               | ✅ Sí                | ✅ Sí                | ✅ Sí                         |
| **Aplicaciones comunes**  | Pilas, colas, arrays| Coordenadas, config. | Eliminación de duplicados | JSON, bases de datos, APIs |
'''