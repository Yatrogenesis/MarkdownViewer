# Markdown Viewer & Editor

Visor y editor de Markdown ligero con exportación a PDF, DOCX y HTML.

## 🚀 Características

- **Vista Dual**: Editor de texto y preview en tiempo real
- **Exportación**: PDF, DOCX, HTML con formato preservado
- **Interfaz Limpia**: Similar a Google Colab con secciones editables/visibles
- **Formato Markdown Completo**: Encabezados, listas, tablas, código, imágenes, enlaces
- **Atajos de Teclado**: Ctrl+B (negrita), Ctrl+I (cursiva), Ctrl+K (código), etc.
- **Auto-guardado**: Guarda automáticamente cada 60 segundos
- **Persistente**: Aplicación de escritorio nativa (no web-UI)

## 📦 Instalación

### Requisitos Previos
- Python 3.8 o superior
- Windows (con adaptaciones funciona en Linux/Mac)

### Pasos de Instalación

1. **Ejecutar instalador automático**:
   ```bash
   install.bat
   ```

2. **Instalación manual** (alternativa):
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Para exportación PDF fiel al preview**: asegúrate de tener instalado `PyQt6-WebEngine` (se instala con `pip install -r requirements.txt`). Si no está disponible, se usará el método nativo con ReportLab.

## 🎯 Uso

### Ejecutar la Aplicación

**Opción 1 - Doble clic**:
- Ejecutar `run.bat`

**Opción 2 - Consola**:
```bash
venv\Scripts\activate
python MarkdownViewer.py
```

### Funcionalidades Principales

#### Menú Archivo
- **Nuevo** (Ctrl+N): Crear nuevo documento
- **Abrir** (Ctrl+O): Abrir archivo .md existente
- **Guardar** (Ctrl+S): Guardar documento actual
- **Guardar como** (Ctrl+Shift+S): Guardar con nuevo nombre
- **Exportar**: PDF, DOCX, HTML

#### Menú Edición
- **Deshacer** (Ctrl+Z)
- **Rehacer** (Ctrl+Y)
- **Fuente**: Cambiar fuente del editor

#### Menú Formato
- **Encabezados**: H1 a H6
- **Negrita** (Ctrl+B): `**texto**`
- **Cursiva** (Ctrl+I): `*texto*`
- **Código inline** (Ctrl+K): `` `código` ``
- **Listas**: Desordenadas y ordenadas
- **Enlaces** (Ctrl+L): `[texto](url)`
- **Imágenes**: `![alt](ruta)`
- **Tablas**: Insertar tabla Markdown
- **Bloques de código**: ` ```lenguaje ```

#### Menú Vista
- **Alternar modo** (F5): Cambiar entre edición/vista
- **Vista dividida** (F6): Editor + preview
- **Solo editor**: Ocultar preview
- **Solo preview**: Ocultar editor

### Modos de Vista

1. **Vista Dividida** (predeterminado):
   - Editor a la izquierda
   - Preview en tiempo real a la derecha

2. **Solo Editor**:
   - Para escribir sin distracciones

3. **Solo Preview**:
   - Para presentar el documento formateado

### Atajos de Teclado

| Atajo | Acción |
|-------|--------|
| Ctrl+N | Nuevo archivo |
| Ctrl+O | Abrir archivo |
| Ctrl+S | Guardar |
| Ctrl+Shift+S | Guardar como |
| Ctrl+Q | Salir |
| Ctrl+Z | Deshacer |
| Ctrl+Y | Rehacer |
| Ctrl+B | Negrita |
| Ctrl+I | Cursiva |
| Ctrl+K | Código inline |
| Ctrl+L | Insertar enlace |
| F5 | Alternar edición/vista |
| F6 | Vista dividida |

## 📄 Exportación

### PDF\r\n1. Menú: **Archivo → Exportar → Exportar a PDF**\r\n2. Métodos de exportación:\r\n   - Preferente: Qt WebEngine `printToPdf` (fiel al preview HTML)\r\n   - Alternativo: nativo ReportLab (sin dependencias externas)\r\n3. Recomendado: usar PyQt6-WebEngine para preservar estilos del preview.\r\n\r\n### DOCX
1. Menú: **Archivo → Exportar → Exportar a DOCX**
2. Compatible con Microsoft Word
3. Convierte encabezados a estilos Word
4. Preserva listas y formato básico

### HTML
1. Menú: **Archivo → Exportar → Exportar a HTML**
2. HTML completo con CSS incluido
3. Puede abrirse en cualquier navegador

## 🎨 Personalización

### Cambiar Fuente del Editor
- **Menú → Edición → Fuente**
- Elige fuente, tamaño y estilo

### Estilo del Preview
- Edita el método `markdown_to_html()` en `MarkdownViewer.py`
- Modifica la sección `<style>` para personalizar colores, fuentes, etc.

## 🔧 Solución de Problemas

### Error al Exportar PDF\r\n**Problema**: Falla la exportación por WebEngine o no está instalado.\r\n\r\n**Solución**:\r\n1. Verifica que `PyQt6-WebEngine` esté instalado (reinstala `requirements.txt`).\r\n2. Si el método WebEngine falla, la aplicación usará automáticamente el exportador nativo ReportLab.\r\n3. Reintenta con un archivo de salida distinto si el PDF está bloqueado por otro proceso.\r\npython
     config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
     pdfkit.from_string(html, file_path, options=options, configuration=config)
     ```

### La aplicación no inicia
**Solución**:
```bash
# Reinstalar dependencias
venv\Scripts\activate
pip install --force-reinstall -r requirements.txt
```

### Preview no se actualiza
**Solución**:
- El preview se actualiza automáticamente 500ms después de dejar de escribir
- Si no funciona, presiona F5 para alternar vista

## 📚 Ejemplos de Markdown

```markdown
# Encabezado 1
## Encabezado 2
### Encabezado 3

**Texto en negrita**
*Texto en cursiva*
`código inline`

- Lista item 1
- Lista item 2
  - Subitem

1. Lista ordenada 1
2. Lista ordenada 2

[Enlace](https://ejemplo.com)
![Imagen](ruta/imagen.png)

| Columna 1 | Columna 2 |
|-----------|-----------|
| Dato 1    | Dato 2    |

\```python
def hello():
    print("Hola Mundo")
\```
```

## 🏗️ Estructura del Proyecto

```
MarkdownViewer/
├── MarkdownViewer.py    # Aplicación principal
├── requirements.txt     # Dependencias Python
├── install.bat         # Instalador automático
├── run.bat             # Ejecutador
├── README.md           # Documentación
└── venv/               # Entorno virtual (creado al instalar)
```

## 🤝 Contribuciones

Mejoras sugeridas:
- [ ] Syntax highlighting en bloques de código
- [ ] Búsqueda y reemplazo
- [ ] Temas oscuro/claro
- [ ] Panel de tabla de contenidos
- [ ] Exportación a otros formatos (ODT, RTF)

## 📝 Licencia

MIT License - Uso libre

## 🙏 Agradecimientos

- PyQt6 para la interfaz gráfica
- Python-Markdown para parsing
- python-docx para exportación Word
- ReportLab / Qt WebEngine para exportación PDF

