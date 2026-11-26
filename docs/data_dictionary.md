# Diccionario de Datos (`omnichannel_consumer_behavior_us_mx_30.csv`)

## 1. Descripción General del Dataset
* **Archivo:** `omnichannel_consumer_behavior_us_mx_30.csv`
* **Naturaleza de los datos:** Dataset ficticio de **30 registros** (15 de Estados Unidos y 15 de México) estructurado bajo el esquema de comportamiento omnicanal (*App*, *Web*, *POI* y exposición publicitaria) e integrado con niveles socioeconómicos de México.
* **Granularidad:** Un registro por evento registrado de un panelista (`panelist_id`) en una marca de tiempo específica (`event_timestamp_utc`).

---

## 2. Definición de Columnas

| Orden | Nombre de Columna | Tipo de Dato | Valores Observados / Formato | Regla de Valores Nulos / Vacíos | Descripción y Reglas de Negocio |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `panelist_id` | Texto / Entero (`string`/`int`) | Ej. `2033037`, `9010001` (7 dígitos) | No admite nulos (presente en los 30 registros). | Identificador único del panelista en el dataset. |
| 2 | `country` | Texto (`string`) | `US`, `MX` | No admite nulos (15 registros `US` y 15 registros `MX`). | Código del país al que pertenece el registro. |
| 3 | `state` | Texto (`string`) | **US:** `CA`, `TX`, `NY`, `FL`, `IL`, `WA`, `OH`, `GA`, `AZ`, `NC`, `MI`, `PA`, `CO`, `VA`, `MA`<br>**MX:** `CDMX`, `Nuevo León`, `Jalisco`, `Estado de México`, `Puebla`, `Querétaro`, `Guanajuato`, `Yucatán`, `Baja California`, `Chihuahua`, `Veracruz` | No admite nulos. | Estado o entidad federativa del evento (abreviatura de 2 letras en US; nombre completo en MX). |
| 4 | `region` | Texto (`string`) | **US:** `WEST`, `SOUTH`, `NORTHEAST`, `MIDWEST`<br>**MX:** `CENTRO`, `NORTE`, `OCCIDENTE`, `BAJIO`, `SURESTE`, `GOLFO` | No admite nulos. | Región geográfica correspondiente al estado dentro de cada país. |
| 5 | `dma` | Texto (`string`) | **US:** códigos numéricos de 3 dígitos (`803`, `623`, `501`, etc.)<br>**MX:** códigos con prefijo `MX-` (`MX-CMX`, `MX-MTY`, `MX-GDL`, `MX-PUE`, `MX-QRO`, `MX-BJX`, `MX-MID`, `MX-TIJ`, `MX-CUU`, `MX-VER`) | No admite nulos. | Área de mercado designada (*Designated Market Area* / plaza geográfica). |
| 6 | `platform` | Texto (`string`) | `iOS`, `Android` | No admite nulos. | Sistema operativo del dispositivo móvil del panelista. |
| 7 | `os_version` | Texto (`string`) | **iOS:** `16.5`, `16.6`, `16.7`, `17.1`, `17.2`, `17.3`, `17.4`, `17.5`<br>**Android:** `11`, `12`, `13`, `14` | No admite nulos. | Versión del sistema operativo del dispositivo. |
| 8 | `device_manufacturer` | Texto (`string`) | `Apple`, `samsung`, `Google`, `LGE`, `Motorola`, `Xiaomi` | No admite nulos. | Fabricante del dispositivo móvil (se conserva la capitalización original del dataset, ej. `samsung`). |
| 9 | `device_model` | Texto (`string`) | Ej. `iPhone 15`, `SM-N970U`, `Pixel 7`, `Moto G84`, `Redmi Note 12` | No admite nulos. | Modelo específico o código de modelo del dispositivo móvil. |
| 10 | `age_group` | Texto (`string`) | `18-24`, `25-34`, `35-44`, `45-54`, `55+` | No admite nulos. | Rango de edad demográfico del panelista. |
| 11 | `gender` | Texto (`string`) | `F`, `M` | No admite nulos. | Género registrado del panelista (`F` = Femenino, `M` = Masculino). |
| 12 | `income_tier` | Texto (`string`) | **US (USD):** `$25,000-$49,999`, `$50,000-$74,999`, `$75,000-$99,999`, `$100,000+`<br>**MX (NSE AMAI):** `A/B`, `C+`, `C`, `C-`, `D+`, `D`, `E` | No admite nulos. | Nivel de ingreso o nivel socioeconómico original. Contiene dos escalas distintas según `country`: rangos en dólares estadounidenses para `US` y niveles socioeconómicos AMAI para `MX`. |
| 13 | `incom_tier_mx` | Texto / Moneda (`string`) | `$56,550`, `$36,200`, `$28,630`, `$22,130`, `$17,450`, `$13,110`, `$8,680` | **Vacío (`NaN` / `NULL`) cuando `country == 'US'`**. Presente en los 15 registros de `MX`. | Columna derivada mediante mapeo desde `income_tier` para registros de México, correspondiente al ingreso mensual promedio estimado en pesos mexicanos (MXN) según la tabla de referencia ENIGH 2024 / Regla AMAI 2026. |
| 14 | `touchpoint_type` | Texto (`string`) | `App`, `Web`, `POI` | No admite nulos. | Tipo de punto de contacto omnicanal del evento: aplicación móvil (`App`), navegación web (`Web`) o visita física a punto de interés (`POI`). |
| 15 | `app_or_domain` | Texto (`string`) | **Apps:** `Walmart App`, `YouTube Music`, `TikTok`, `Kroger`, `Walmart México`, `Sam's Club México`, `Spotify`, `Rappi`<br>**Web:** `target.com`, `amazon.com`, `costco.com`, `walmart.com`, `sephora.com`, `mercadolibre.com.mx`, `amazon.com.mx`, `walmart.com.mx`, `soriana.com` | **Vacío (`NaN` / `NULL`) cuando `touchpoint_type == 'POI'`**. | Nombre de la aplicación móvil o dominio web visitado en eventos digitales (`App` o `Web`). |
| 16 | `poi_name` | Texto (`string`) | Ej. `Walmart Supercenter #1422`, `Starbucks #881`, `Whole Foods #304`, `Best Buy #512`, `Walmart Express Valle`, `Bodega Aurrera Ecatepec`, `OXXO León Centro`, `Liverpool Polanco`, `Starbucks Reforma 222` | **Vacío (`NaN` / `NULL`) cuando `touchpoint_type` es `App` o `Web`**. | Nombre específico de la tienda o establecimiento físico (*Point of Interest*) visitado. |
| 17 | `poi_category` | Texto (`string`) | `Big Box Store`, `QSR / Coffee`, `Big Box Store Grocery Store`, `Supermarket`, `Electronics`, `Discount Retail`, `Convenience`, `Department Store` | **Vacío (`NaN` / `NULL`) cuando `touchpoint_type` es `App` o `Web`**. | Categoría comercial del punto de interés físico visitado. |
| 18 | `ad_exposure_channel` | Texto (`string`) | `In-App Audio`, `Social Ad`, `In-App Media` | **Vacío (`NaN` / `NULL`) cuando no hubo exposición publicitaria asociada al evento** (5 registros en el dataset). | Canal publicitario al que estuvo expuesto el panelista previo o durante el evento. |
| 19 | `advertiser_name` | Texto (`string`) | Ej. `Walmart`, `Target`, `Huggies`, `Starbucks`, `Costco`, `PepsiCo`, `Amazon`, `Best Buy`, `Sephora`, `Walmart México`, `Walmart Express`, `Mercado Libre`, `Amazon México`, `Sam's Club`, `Coca-Cola`, `Bodega Aurrera`, `Liverpool`, `Soriana`, `Starbucks México` | **Vacío (`NaN` / `NULL`) cuando `ad_exposure_channel` es vacío**. | Marca o anunciante asociado al impacto publicitario registrado. |
| 20 | `duration_sec` | Entero (`int`) | Rango observado: `180` a `3200` | No admite nulos. | Duración del evento o estancia medida en segundos. |
| 21 | `event_type` | Texto (`string`) | `Browse`, `Visit`, `Purchase`, `Stream`, `Ad_View` | No admite nulos. | Clasificación de la acción realizada en el punto de contacto (`Visit` en `POI`; `Browse`, `Purchase`, `Stream`, `Ad_View` en `App`/`Web`). |
| 22 | `event_timestamp_utc` | Fecha y Hora (`datetime` / `string`) | Formato `YYYY-MM-DD HH:MM:SS` (ej. `2026-11-20 14:12:05` a `2026-11-21 16:48:35`) | No admite nulos. | Marca de tiempo del evento registrada en tiempo universal coordinado (UTC). |

---

## 3. Regla de Mapeo Aplicada en `incom_tier_mx`

La columna `incom_tier_mx_est` se construyó exclusivamente a partir de los valores de `income_tier ` correspondientes a México (`country == 'MX'`), tomando como referencia la tabla proporcionada `lookup_nse_mx.csv` (*Ingreso mensual promedio estimado* / ENIGH 2024 / Regla 2026):
is_approximate = True o estimate_type = "approx_monthly_mean", y documenta que por ejemplo 36200 es un valor aproximado de referencia (~$36,200 en la fuente) y no un ingreso real medido del panelista.
DEBE tratarse como variable proxi

| `income_tier` (Nivel Socioeconómico MX) | `incom_tier_mx_est` (Ingreso mensual promedio estimado) |
| :--- | :--- |
| `A/B` | `$56,550` |
| `C+` | `$36,200` |
| `C` | `$28,630` |
| `C-` | `$22,130` |
| `D+` | `$17,450` |
| `D` | `$13,110` |
| `E` | `$8,680` |
| *Valores de `US` (`$25,000-$49,999`, etc.)* | *Vacío (`NaN` / `NULL`)* |