"""
Carta de Amor Digital Interactiva
=================================
Versión con slideshow de fotos (lado a lado en PC)

1. Pon tus fotos en:  static/fotos/
2. Edita la lista FOTOS más abajo
3. Ejecuta: python app.py
"""

from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Carpeta donde vive app.py: así las rutas funcionan sin importar desde dónde ejecutes el programa
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
#                  CONFIGURACIÓN (EDITA AQUÍ)
# ============================================================
TEXTO_CARTA = """Mi amor,

Hay algo en ti que me desarma por completo.  
Esa sonrisa tuya, esa forma en la que miras, ese cabello que cae con tanta gracia…  
todo en ti me parece hermoso.

Cada vez que te veo, siento que el mundo se detiene un segundo.  
No necesitas hacer nada especial para ser la persona más brillante del lugar.  
Solo con existir ya llenas todo de luz.

Me encanta cómo te ves cuando estás tranquila, cuando sonríes sin darte cuenta,  
cuando simplemente eres tú.  
Eres de esas personas que dejan huella sin esfuerzo,  
de las que uno no olvida fácilmente.

Gracias por existir, por tu dulzura, por esa energía tan linda que tienes.  
Gracias por dejarme conocerte y por regalarme momentos que guardo con mucho cariño.

Quiero que sepas que eres importante para mí.  
Que me haces bien.  
Que contigo todo se siente más bonito y más ligero.

No sé cómo explicarlo del todo,  
pero cada día me doy cuenta de que me gustas más.  
No solo por cómo te ves, sino por cómo eres.  
Por lo especial que resultas siendo simplemente tú.

Te pienso más de lo que imaginas.  
Y cada vez que lo hago, sonrío.

Con todo mi corazón,  
siempre tuyo ❤️"""

COLOR_SOBRE = "#e74c3c"

# Nombres exactos de tus fotos (las muy pesadas las dejé comentadas)
FOTOS = [
    "1.jpeg",
    "2.png",
    "3.png",
    "4.png",
    "5.png",
    "6.jpeg",
    "7.jpeg",
    "12.jpeg",
    "13.jpeg",
    "14.jpeg",
    "15.jpeg",
    "16.jpeg",
    "17.jpeg",
]

MUSICA = "cancion.mp3"    # Si no existe, se usa automáticamente el primer .mp3 de static/musica

# ============================================================
#              NO TOCAR DE AQUÍ PARA ABAJO
# ============================================================

def encontrar_musica():
    """Devuelve el nombre del mp3 a usar, o None si no hay ninguno."""
    carpeta = os.path.join(BASE_DIR, "static", "musica")
    if MUSICA and os.path.exists(os.path.join(carpeta, MUSICA)):
        return MUSICA
    if os.path.isdir(carpeta):
        for archivo in sorted(os.listdir(carpeta)):
            if archivo.lower().endswith(".mp3"):
                return archivo   # p. ej. "canción.mp3" (con tilde)
    return None


def limpiar_texto(texto):
    """Quita los espacios sobrantes al final de cada línea (descentran el texto)."""
    return "\n".join(linea.rstrip() for linea in texto.splitlines())


@app.route("/")
def index():
    fotos_existentes = []
    for foto in FOTOS:
        if os.path.exists(os.path.join(BASE_DIR, "static", "fotos", foto)):
            fotos_existentes.append(foto)

    return render_template(
        "index.html",
        texto=limpiar_texto(TEXTO_CARTA),
        color_sobre=COLOR_SOBRE,
        fotos=fotos_existentes,
        musica=encontrar_musica()
    )


@app.route("/fotos/<path:filename>")
def servir_fotos(filename):
    return send_from_directory(os.path.join(BASE_DIR, "static", "fotos"), filename)


@app.route("/musica/<path:filename>")
def servir_musica(filename):
    return send_from_directory(os.path.join(BASE_DIR, "static", "musica"), filename)


if __name__ == "__main__":
    print("\n" + "=" * 55)
    print("  Carta de Amor lista!")
    print("  Abre en tu navegador: http://127.0.0.1:5000")
    print("  Musica encontrada: " + str(encontrar_musica()))
    print("=" * 55 + "\n")
    app.run(debug=True, port=5000)