# Caña de azúcar analyzer project

### Comando para inicializar el api:

uvicorn main:app --reload

### Estructura del proyecto
sugarcane_analyzer/
├── images/               # Tus 300 imágenes originales
├── output/               # Donde se guardarán resultados, recortes, debug, 
etc.
├── debugs/
├── xdxd/
├── preprocessing.py      # Recorte automático a la hoja
├── measurement.py        # Medición de largo y nudos
├── utils.py              # Funciones auxiliares
├── main.py               # Script principal que ejecuta todo
