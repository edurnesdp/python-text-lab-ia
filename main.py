# main.py
# Punto de entrada principal para el análisis de texto

from modules.text_analysis import analyze_text, detect_authorship_variation, detect_emotional_tone

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Uso: python main.py \"Texto de prueba\"")
    else:
        texto = sys.argv[1]
        resultado = analyze_text(texto)
        print(resultado)
        autoriaResultado = detect_authorship_variation(texto)
        print(autoriaResultado)
        tono_emocional = detect_emotional_tone(texto)
        print(tono_emocional)