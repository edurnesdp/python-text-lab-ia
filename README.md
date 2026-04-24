# python-text-lab-ia
# Python Text Lab

Proyecto de pruebas en Python para experimentar de forma práctica con análisis y procesamiento de texto.

Este repositorio forma parte de mi laboratorio personal de aprendizaje, donde desarrollo pequeñas soluciones enfocadas en código limpio, modularidad y evolución progresiva del proyecto.

---

## Objetivos

- Practicar Python de forma práctica y estructurada  
- Diseñar código modular y fácil de evolucionar  
- Experimentar con análisis de texto  
- Sentar las bases para futuras integraciones con IA o APIs  

---

## Funcionalidades iniciales

- Análisis de texto desde línea de comandos
- Detección básica de idioma
- Conteo de palabras y caracteres
- Extracción simple de palabras clave

---

## Nueva funcionalidad: Interfaz web

Ahora el proyecto incluye una interfaz web sencilla utilizando Flask. Esta permite interactuar con las funcionalidades del análisis de texto desde un navegador.

### Ejecución de la aplicación web

1. Asegúrate de tener instaladas las dependencias ejecutando:
   ```bash
   pip install -r requirements.txt
   ```
2. Inicia el servidor web con el siguiente comando:
   ```bash
   python3 app.py
   ```
3. Abre tu navegador y ve a `http://127.0.0.1:5000`.

### Funcionalidades disponibles en la interfaz web
- Análisis de texto: longitud, palabras, caracteres y detección de idioma.
- Detección de variaciones estilísticas para identificar posibles diferencias de autoría.

---

## Ejecución

```bash
python3 main.py "Texto de prueba para analizar"
```

---

## Nota

Este proyecto ha sido desarrollado con el apoyo de GitHub Copilot, una herramienta de inteligencia artificial que asiste en la programación y el desarrollo de software. Su uso ha permitido acelerar el proceso de desarrollo y mantener un enfoque en la calidad del código.
