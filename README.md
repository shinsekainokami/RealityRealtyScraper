### README.md

# RealityRealtyScraper

**RealityRealtyScraper** es un proyecto diseñado para extraer información de anuncios del sitio web [Reality Realty PR](https://www.realityrealtypr.com). Este programa permite obtener datos de propiedades (casas y apartamentos) y guardarlos en un archivo JSON para su posterior análisis.

---

## 📋 **Descripción del Proyecto**

El programa se basa en la biblioteca [Playwright](https://playwright.dev/python/) para realizar la navegación web y la extracción de datos. Utiliza un sistema de línea de comandos para especificar el tipo de propiedad, la página de interés y la ubicación donde se guardará el archivo resultante.

---

## 🚀 **Requisitos del Sistema**

- **Python**: Versión 3.9 o superior
- **Dependencias**:
  - [Playwright](https://playwright.dev/python/) (versión 1.49.1 o superior)
- **Sistema Operativo**: Compatible con Windows, macOS y Linux

Instala las dependencias necesarias con los siguientes comandos:

```bash
python -m build
pip install .
```

Asegúrate de instalar los navegadores requeridos por Playwright ejecutando:

```bash
playwright install
```

---

## 🛠 **Cómo Usar**

### 1. **Ejecución desde la línea de comandos**

Para ejecutar el programa, utiliza el siguiente comando:

```bash
python app.py <tipo_propiedad> <n_pagina> <archivo_destino>
```

- `<tipo_propiedad>`: Define el tipo de propiedad a buscar. Opciones disponibles:
  - `HOUSE` para casas
  - `APARTMENT` para apartamentos
- `<n_pagina>`: Número de página de la cual extraer los datos (inicia desde 0).
- `<archivo_destino>`: Ruta relativa del archivo donde se guardará la información en formato JSON.

**Ejemplo de uso:**

```bash
python app.py HOUSE 0 salida.json
```

---

## 📄 **Detalles Técnicos**

### Archivos principales:

- **`app.py`**: Punto de entrada del programa que gestiona los argumentos de la línea de comandos y llama a las funciones de scraping.
- **`scraper/scraper.py`**: Contiene las funciones principales para la navegación web, extracción de datos y manejo de URLs dinámicas.

### Funciones principales:

1. **`get_property_data(property_type: str, n_page: int)`**:
   - Extrae información de las propiedades visibles en una página específica.
   - Navega a cada propiedad, obtiene los datos necesarios y regresa al listado.

2. **`scrape_data_from_property(page, title)`**:
   - Extrae detalles individuales de una propiedad, como precio, descripción, imágenes y URL del flyer.

3. **`create_realityrealty_url(property_type: str, page: int)`**:
   - Genera la URL dinámica según el tipo de propiedad y la página especificada.

---

## 📝 **Salida de Datos**

La información extraída se guarda en un archivo JSON especificado por el usuario. Ejemplo de estructura de salida:

```json
[
    {
        "url": "https://example.com/property",
        "title": "Casa de Lujo en Rio Mar",
        "city": "Rio Grande",
        "price": "$1,200,000",
        "description": "Experimente el pináculo del lujo en el exclusivo Foursome Village...",
        "images": [
            "https://example.com/image1.jpg",
            "https://example.com/image2.jpg"
        ],
        "flyer": "https://example.com/flyer"
    }
]
```

---

## 📚 **Notas Adicionales**

- Asegúrate de que la URL generada esté disponible y que los datos visibles en el sitio web correspondan a las expectativas del programa.
- El programa está diseñado para páginas estáticas o dinámicas compatibles con Playwright.

---

## 🧑‍💻 **Contribuciones**

¡Contribuciones son bienvenidas! Si encuentras un error o deseas agregar nuevas funcionalidades, no dudes en abrir un [issue](https://github.com/) o realizar un fork del proyecto.

---

## 📞 **Contacto**

Para dudas o consultas, puedes comunicarte con el autor:

- **Nombre**: Christian Munoz
- **Correo**: clcardenas8@gmail.com
