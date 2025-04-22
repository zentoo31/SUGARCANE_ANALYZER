# 🧪 Proyecto: Análisis de Cañas de Azúcar

Este proyecto analiza imágenes de cañas de azúcar sobre una hoja blanca para calcular su **largo**, contar el **número de nudos** y estimar el **grosor de cada nudo**, utilizando procesamiento de imágenes con OpenCV y una API construida con FastAPI.

---

## 🚀 Instrucciones para inicializar el proyecto

### 1. Clona el repositorio

```bash
git clone https://github.com/tuusuario/sugarcane_analyzer.git
cd sugarcane_analyzer
```

### 2. Crea el entorno virtual
```bash
python -m venv venv
```

### 3. Ingresa al entorno virtual
```bash
venv\Scripts\activate
```

### 4. Instala los requerimientos
```bash
venv\Scripts\activate
```

### 5. Inicializa las carpetas del proyecto
```bash
python initializer.py
```

### 6. Ejecuta la api
```bash
uvicorn main:app --reload
```

### 6. Estructura del proyecto
```bash
sugarcane_analyzer/
├── images/               # Imágenes de entrada
├── output/               # Resultados y visualizaciones
├── debugs/               # Depuración de filtros e imágenes intermedias
├── xdxd/                 # Carpeta donde se guardan imágenes subidas por API
│
├── preprocessing.py      # Recorte automático de la hoja blanca
├── measurement.py        # Medición de largo, nudos y grosor
├── analyzer.py           # Lógica completa de análisis de una imagen
├── utils.py              # Funciones auxiliares
├── main.py               # Archivo que lanza la API con FastAPI
├── setup_directories.py  # Script que asegura que existan las carpetas necesarias
├── requirements.txt      # Librerías necesarias
```