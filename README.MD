# Walmart Omnichannel, SEO & AEO Data Analytics Portfolio (US & MX)

desarrollado por Laura Rubi alias Rubinet
Proyecto de portafolio de **Data Analytics** enfocado en el ecosistema retail de **Walmart (México y Estados Unidos)**. Integra tres enfoques analíticos clave:
1. **Exploratory Data Analysis (EDA):** comportamiento omnicanal (App, Web y visitas físicas a tiendas/POI) y perfil socioeconómico.
2. **Fullstack Data Analysis:** arquitectura reproducible por etapas (Raw $\rightarrow$ Interim $\rightarrow$ Processed) y modelado relacional ligero sin depender de servidores externos.
3. **Funnel & AEO Analysis:** análisis del recorrido hacia la conversión y visibilidad de marca frente a competidores en motores de búsqueda tradicionales y respuestas de IA (*Answer Engine Optimization*).

---

## Alcance y Transparencia de Datos

Dado que este es un proyecto de portafolio independiente **sin acceso a servidores internos, Google Search Console** tomo como base **M Four Omni Traffic Data Schema de Walmart** publicado en Datarade (https://datarade.ai/data-products/omnichannel-consumer-journeys-1st-party-3b-events-verifi-mfour), la arquitectura opera de forma local/portable con los primeros registros del Dataset (CSV + SQLite en memoria/archivo) combinando:
* **Datos estructurados de muestra verificada para USA / y simulados para México:** dataset omnicanal de 30 registros (15 US / 15 MX) basado en esquemas de medición *first-party* (App, Web, POI y exposición publicitaria) y eventos simulados de embudo.
* **Datos públicos y observaciones propias:** referencias de tendencias de búsqueda en México (Google Trends) y auditorías manuales de visibilidad en motores de IA (ChatGPT, Gemini, Perplexity y HubSpot).

---
## 🛠️ Stack tecnológico

| Tecnología | Uso |
| :--- | :--- |
| Git & GitHub | Control de versiones, estructura por etapas y publicación del portafolio |
| Google Colab / Python (`pandas`, `numpy`) | Limpieza de datos, homologación de campos y análisis exploratorio (EDA) |
| CSV (`data/raw`, `interim`, `processed`) | Almacenamiento portable por etapas sin servidor ni base de datos externa |
| SQLite (`sqlite3`) / SQL | Modelado relacional ligero en memoria/archivo y consultas de embudo/AEO |
| Google Trends & Motores de IA (AEO) | Tendencias de búsqueda en MX y auditoría de visibilidad frente a competidores |
| HubSpot AI Search Grader (AEO Grader) | Evaluación de visibilidad, menciones y desempeño de marca en motores de búsqueda con IA (AEO) |
---
📁 Estructura del proyecto

```text
walmart-omnichannel-aeo-portfolio/
├── data/
├── docs/
├── notebooks/
├── outputs/
├── sql/
└── src/
```

---

## Estado Actual del Proyecto y Estructura de Archivos

Siguiendo buenas prácticas de gestión de datos (separación estricta entre datos crudos, intermedios y procesados), esta tabla muestra el avance actual de cada componente:

| Carpeta / Archivo | Etapa del Flujo | Descripción | Estado |
| :--- | :--- | :--- | :--- |
| `README.md` | Documentación | Visión general del caso de negocio, alcance y estado de avance. | Completado |
| `data/raw/omnichannel_us_mx_30.csv` | Datos Crudos (*Raw*) | Dataset original de 30 registros (US y MX) intacto, sin modificaciones manuales. | Completado |
| `data/interim/lookup_nse_mx.csv` | Datos Intermedios (*Interim*) | Tabla de referencia de niveles socioeconómicos en México (AMAI / ENIGH: `A/B` a `E`) para homologación. | Completado |
| `data/processed/omnichannel_clean.csv` | Datos Procesados (*Processed*) | Dataset limpio con la columna `incom_tier_mx` mapeada, tipos validados y nulos auditados. | Pendiente (en análisis local) |
| `notebooks/walmart_seo_aeo_portfolio.ipynb` | Análisis y Modelado | Cuaderno principal en Google Colab (EDA, modelo estrella en SQLite, Funnel y AEO). | Pendiente (en desarrollo en Google Colab) |
| `src/01_clean_omnichannel.py` | Procesamiento / ETL | Script modular para automatizar la limpieza y creación de columnas desde `raw/` hacia `processed/`. | Pendiente |
| `sql/funnel_and_aeo_queries.sql` | Consultas Analíticas | Consultas SQL sobre esquema estrella ligero (`fact_trends_mx`, `fact_aeo_visibility`, `fact_funnel_simulated`). | Pendiente |
| `docs/dataset_context.md` | Documentación | Contexto bilingüe (EN/ES) de *Consumer Behavior Data*, referencia a Datarade/MFour y adaptación de `incom_tier_mx`. | Completado |
| `docs/data_dictionary.md` | Documentación | Diccionario formal de variables, monedas (USD vs. MXN) y reglas de valores nulos. | Pendiente |
| `outputs/` | Entregables | Gráficos exportados (`.png`) y tablas resumen para presentación ejecutivo. | Pendiente |

---

## Modelo de Datos Propuesto (Esquema Estrella Ligero)

Para evitar duplicidad de métricas al cruzar distintas granularidades (búsquedas por fecha, comportamiento omnicanal y etapas de embudo) sin infraestructura en la nube, el proyecto se diseña para correr sobre **SQLite (`sqlite3`) / DuckDB**:

* **Tablas de Hechos (*Facts*):**
  * `fact_omnichannel_events`: eventos de usuario por país, plataforma (`iOS`/`Android`), punto de contacto (`App`, `Web`, `POI`), exposición publicitaria y conversión.
  * `fact_trends_mx`: evolución de interés de búsqueda en México y variación porcentual.
  * `fact_aeo_visibility`: menciones y citas de Walmart vs. competidores en respuestas de motores de IA.
  * `fact_funnel_simulated`: recorrido simulado (`Visit` $\rightarrow$ `Product_View` $\rightarrow$ `Add_to_Cart` $\rightarrow$ `Checkout` $\rightarrow$ `Purchase`).
* **Tablas de Dimensiones (*Dimensions*):** `dim_date`, `dim_brand_competitor` y `dim_category`.

---

## Próximos Pasos
- [ ] Exportar y subir el notebook terminado desde Google Colab a `notebooks/`.
- [ ] Modularizar las reglas de limpieza en `src/01_clean_omnichannel.py`.
- [ ] Completar `docs/data_dictionary.md` con las reglas de homologación entre ingresos anuales (US) y mensuales estimados (MX).
- [ ] Generar visualizaciones clave del embudo y comparativa US vs. MX en `outputs/figures/`.