# Conversor de Videos de YouTube a Texto

## Descripción

Aplicación web que convierte videos de YouTube a texto utilizando Flask para el backend y HTML/CSS para la interfaz de usuario. Permite copiar la transcripción al portapapeles y enviarla a ChatGPT para su análisis.

## Características

- **Formulario de Entrada**: Ingresa la URL de un video de YouTube.
- **Transcripción de Videos**: Muestra el texto transcrito del video.
- **Interacción del Usuario**: 
  - Copia la transcripción al portapapeles.
  - Envía la transcripción a ChatGPT.
- **Notificaciones**: Mensajes de error o éxito.

## Tecnologías Utilizadas

- Flask
- HTML/CSS
- JavaScript

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/juliotoribio/Youtube_Speech_to_Text
    cd tu_repositorio
    ```

2. Crea un entorno virtual e instala las dependencias:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Ejecuta la aplicación:
    ```bash
    flask run
    ```

## Uso

1. Abre `http://127.0.0.1:5000` en tu navegador.
2. Ingresa la URL de un video de YouTube y presiona "Obtener Texto".
3. Visualiza y copia la transcripción o envíala a ChatGPT.

## Contribuciones

Las contribuciones son bienvenidas. Abre un issue o pull request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
