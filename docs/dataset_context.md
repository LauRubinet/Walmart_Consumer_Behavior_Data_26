# Dataset Context & Reference / Contexto y Referencia del Dataset

## English

### What is Consumer Behavior Data?
Consumer behavior data captures purchasing patterns and lifestyle choices, helping businesses understand consumer trends. It is collected and analyzed around individuals’ actions, preferences, and decision-making processes as consumers. Businesses use this data to understand and predict consumer behavior, tailor marketing strategies, improve products and services, and enhance customer experiences.

### Examples of Consumer Behavior Data
Examples of consumer behavior data include datasets offering insights into customer actions and preferences:
* **Purchase History:** Records of past purchases, including product type, frequency, and spending amount.
* **Browsing Patterns:** Pages visited, time spent on each page, and navigation paths on websites.
* **Product Preferences:** Frequently viewed or saved products, brands, or categories.
* **Engagement Level:** Interactions with emails, ads, or content, including clicks and shares.
* **In-Store Behavior:** Foot traffic patterns, time spent in-store, and areas visited.
* **Device Usage:** Types of devices used for shopping or browsing (e.g., mobile, desktop).
* **Loyalty Program Activity:** Points earned, rewards redeemed, and purchase frequency among loyal customers.

### Data Source & Portfolio Adaptation
* **Schema Reference:** Adapted from the *Omnichannel Consumer Journeys (1st-Party, 3B+ Events)* product specification by MFour on Datarade:  
  https://datarade.ai/data-products/omnichannel-consumer-journeys-1st-party-3b-events-verifi-mfour
* **Mexico Localization (`incom_tier_mx`):** To reflect the Mexican retail market alongside US records, a custom column (`incom_tier_mx`) was added, mapping Mexican socioeconomic levels (AMAI: `A/B`, `C+`, `C`, `C-`, `D+`, `D`, `E`) to estimated monthly household income in MXN, while leaving US records empty (`NULL`/`NaN`) to avoid mixing currencies and periodicities.

---

## Español

### ¿Qué son los Datos de Comportamiento del Consumidor (*Consumer Behavior Data*)?
Los datos de comportamiento del consumidor capturan patrones de compra y elecciones de estilo de vida, ayudando a las empresas a comprender las tendencias de consumo. Se recopilan y analizan en torno a las acciones, preferencias y procesos de toma de decisiones de las personas como consumidores. Las empresas utilizan esta información para comprender y predecir el comportamiento del consumidor, adaptar estrategias de marketing, mejorar productos y servicios y optimizar la experiencia del cliente.

### Ejemplos de Datos de Comportamiento del Consumidor
Entre los principales conjuntos de datos que ofrecen información sobre las acciones y preferencias de los clientes se encuentran:
* **Historial de compras (*Purchase History*):** registros de compras pasadas, incluyendo tipo de producto, frecuencia y monto gastado.
* **Patrones de navegación (*Browsing Patterns*):** páginas visitadas, tiempo invertido en cada página y rutas de navegación en sitios web.
* **Preferencias de producto (*Product Preferences*):** productos, marcas o categorías vistos o guardados con frecuencia.
* **Nivel de interacción (*Engagement Level*):** interacciones con correos electrónicos, anuncios o contenido, incluyendo clics y compartidos.
* **Comportamiento en tienda física (*In-Store Behavior*):** patrones de tráfico peatonal, tiempo de permanencia en tienda y áreas visitadas.
* **Uso de dispositivos (*Device Usage*):** tipos de dispositivos utilizados para comprar o navegar (por ejemplo, móvil o computadora de escritorio).
* **Actividad en programas de lealtad (*Loyalty Program Activity*):** puntos acumulados, recompensas canjeadas y frecuencia de compra entre clientes leales.

### Fuente de Referencia y Adaptación para el Portafolio
* **Referencia de esquema:** adaptado de la ficha técnica *Omnichannel Consumer Journeys (1st-Party, 3B+ Events)* de MFour publicada en Datarade:  
  https://datarade.ai/data-products/omnichannel-consumer-journeys-1st-party-3b-events-verifi-mfour
* **Adaptación para México (`incom_tier_mx`):** para integrar registros de México junto con los de Estados Unidos, se añadió la columna `incom_tier_mx`, mapeando los niveles socioeconómicos en México (AMAI: `A/B`, `C+`, `C`, `C-`, `D+`, `D`, `E`) a ingresos mensuales estimados en pesos mexicanos (MXN), dejando vacíos (`NULL`/`NaN`) los registros de EE. UU. para no mezclar monedas ni periodicidades.