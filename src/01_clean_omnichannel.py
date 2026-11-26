import io
import pandas as pd
from google.colab import files

# 1. Cargar el archivo CSV en Google Colab (si ya está en /content/, ajusta la ruta)
uploaded = files.upload()
filename = next(iter(uploaded))
df = pd.read_csv(io.BytesIO(uploaded[filename]))

# 2. Información base de la tabla
print("=== DIMENSIONES Y ESTRUCTURA ===")
print(f"Archivo: {filename}")
print(f"Filas: {df.shape[0]} | Columnas: {df.shape[1]}\n")

print("=== NOMBRES Y TIPOS DE DATOS (INFO) ===")
df.info()

# 3. Información clave de calidad y contenido
print("\n=== VALORES NULOS / FALTANTES POR COLUMNA ===")
nulls = pd.DataFrame({
    "nulos": df.isna().sum(),
    "pct_nulos": (df.isna().mean() * 100).round(2),
    "dtype": df.dtypes,
    "valores_unicos": df.nunique(dropna=True)
})
display(nulls)

print("\n=== PRIMERAS 5 FILAS ===")
display(df.head())

print("\n=== RESUMEN ESTADÍSTICO (NUMÉRICAS Y CATEGÓRICAS) ===")
display(df.describe(include="all").T)