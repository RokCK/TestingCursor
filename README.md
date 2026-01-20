# TestingCursor

Repositorio utilizado para testing de Cursor desde SSH.

**Autor:** @rokck

## Descripción

Este repositorio contiene una aplicación web minimalista del juego del Gato (Tic Tac Toe) desarrollada en Python con Flask. La aplicación está diseñada para ejecutarse dentro de un contenedor Docker y ser accesible remotamente a través del puerto 80.

## Contenido del Repositorio

- **`app.py`** - Aplicación Flask principal que maneja la lógica del juego, incluyendo:
  - Gestión del estado del juego
  - Endpoints REST API para movimientos y reinicio
  - Detección de ganador y empates
  
- **`templates/index.html`** - Interfaz web minimalista con:
  - Diseño responsive a pantalla completa
  - Tablero interactivo de 3x3
  - Indicadores de turno y mensajes de victoria/empate
  - Favicon personalizado de gato
  
- **`requirements.txt`** - Dependencias de Python (Flask)

- **`Dockerfile`** - Configuración para construir la imagen Docker con Python 3.11

- **`docker-compose.yml`** - Configuración de Docker Compose para facilitar el despliegue

- **`.dockerignore`** - Archivos excluidos del build de Docker

## Juego del Gato (Tic Tac Toe)

Aplicación web minimalista del juego del Gato ejecutándose en un contenedor Docker.

### Configuración con Docker

#### Opción 1: Usando Docker Compose (Recomendado)
```bash
# Construir y ejecutar el contenedor
sudo docker compose up -d --build

# Ver logs
sudo docker compose logs -f

# Detener el contenedor
sudo docker compose down
```

**Nota:** Si tu usuario está en el grupo `docker`, puedes omitir `sudo`. Para agregar tu usuario al grupo docker:
```bash
sudo usermod -aG docker $USER
# Luego cierra sesión y vuelve a entrar
```

#### Opción 2: Usando Docker directamente
```bash
# Construir la imagen
sudo docker build -t gato-app .

# Ejecutar el contenedor con volumen montado
sudo docker run -d \
  --name gato \
  -p 80:80 \
  -v $(pwd):/app \
  --restart unless-stopped \
  gato-app
```

### Acceso
La aplicación estará disponible en:
- `http://localhost` (desde el servidor)
- `http://<IP_DEL_SERVIDOR>` (desde cualquier dispositivo en la red)

### Gestión del contenedor
```bash
# Ver logs
sudo docker logs -f gato

# Detener el contenedor
sudo docker stop gato

# Iniciar el contenedor
sudo docker start gato

# Eliminar el contenedor
sudo docker rm -f gato
```

### Notas
- El directorio `TestingCursor` está montado como volumen, por lo que los cambios en los archivos se reflejarán automáticamente (puede requerir reinicio del contenedor para cambios en Python)
- El puerto 80 del contenedor está mapeado al puerto 80 del host
