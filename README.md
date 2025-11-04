# parcial_2_guillot_y_taglio
parcial 2 de programacion 1pro4 prof hualpa

## Clasificación de cartas (CSV)

He añadido CSVs en el repositorio para clasificar cartas de Clash Royale por subcategoría. Los archivos creados son:

- `terrestres.csv` — cartas de unidad terrestre.
- `aereos.csv` — cartas de unidad aérea.
- `hechizos.csv` — cartas de hechizo.

Cada CSV contiene una columna `nombre` con el nombre de la carta en cada fila. Si quieres que añada más columnas (coste de elixir, rareza, rol), dímelo y lo actualizo.

Nota: se asumió que la subcategoría correcta era `aereos` en lugar de `acuaticos`.

### Columnas nuevas

He añadido dos columnas a cada CSV: `elixir` (coste en elixir de la carta) y `rareza` (Common, Rare, Epic, Legendary). Puedes editar esos valores si prefieres otra fuente o versión del juego.

### Script de consulta

Incluí un pequeño script Python `scripts/list_cards.py` que lee los CSVs y permite filtrar por subcategoría (`terrestres`, `aereos`, `hechizos`), rareza y rango de elixir. Ejemplo de uso:

```powershell
python .\scripts\list_cards.py --subcategoria terrestres --max-elixir 4
```

Eso listará todas las cartas terrestres con coste de elixir menor o igual a 4.

