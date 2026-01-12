import geopandas as gpd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
SHAPEFILE = BASE_DIR / "data" / "shapefiles" / "Departamento_INEI_2017.shp"
OUTPUT_DIR = BASE_DIR / "static" / "maps"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "peru_departments.png"

# =========================
# LOAD DATA
# =========================
peru = gpd.read_file(SHAPEFILE)
peru = peru.to_crs(epsg=4326)

# =========================
# PLOT
# =========================
fig, ax = plt.subplots(figsize=(8, 10))

peru.plot(
    ax=ax,
    edgecolor="black",
    facecolor="none",
    linewidth=0.6
)

ax.set_title(
    "Mapa del Perú – División Departamental",
    fontsize=14
)

ax.axis("off")
plt.tight_layout()

# =========================
# SAVE
# =========================
plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches="tight")
plt.close()

print(f"Mapa generado en: {OUTPUT_FILE}")