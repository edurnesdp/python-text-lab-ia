# text_analysis.py
# Módulo para análisis de texto

from langdetect import detect, DetectorFactory
from collections import Counter
from textblob import TextBlob
from textblob.exceptions import NotTranslated

# Aseguramos resultados consistentes
DetectorFactory.seed = 0

def analyze_text(text):
    return {
        "longitud": len(text),
        "palabras": len(text.split()),
        "caracteres": len([c for c in text if c.isalpha()]),
        "idioma": detect(text)  # Detección automática de idioma
    }

def detect_authorship_variation(text):
    """
    Analiza si un texto podría haber sido escrito por diferentes personas
    basado en características estilísticas simples.
    """
    # Dividimos el texto en segmentos (por ejemplo, párrafos)
    segments = text.split("\n\n")

    # Calculamos características estilísticas para cada segmento
    segment_features = []
    for segment in segments:
        words = segment.split()
        char_count = len([c for c in segment if c.isalpha()])
        avg_word_length = char_count / len(words) if words else 0
        punctuation_count = sum(1 for c in segment if c in ".,;:!?")
        segment_features.append({
            "avg_word_length": avg_word_length,
            "punctuation_count": punctuation_count,
            "word_count": len(words),
        })

    # Comparamos las características entre segmentos
    variations = {
        "avg_word_length": max(f["avg_word_length"] for f in segment_features) - min(f["avg_word_length"] for f in segment_features),
        "punctuation_count": max(f["punctuation_count"] for f in segment_features) - min(f["punctuation_count"] for f in segment_features),
        "word_count": max(f["word_count"] for f in segment_features) - min(f["word_count"] for f in segment_features),
    }

    # Determinamos si hay variaciones significativas
    threshold = 5  # Umbral arbitrario para detectar diferencias
    significant_variations = {k: v for k, v in variations.items() if v > threshold}

    return {
        "segment_features": segment_features,
        "variations": variations,
        "significant_variations": significant_variations,
    }

def detect_emotional_tone(text):
    """
    Detecta el tono emocional del texto (positivo, negativo o neutral)
    utilizando la polaridad de TextBlob. Traduce automáticamente al inglés si es necesario.
    """
    blob = TextBlob(text)

    # Detectar el idioma con langdetect
    try:
        if detect(text) != 'en':
            blob = blob.translate(to='en')
    except Exception:
        pass  # Si no se puede traducir, continuar con el texto original

    polarity = blob.sentiment.polarity

    if polarity > 0:
        tone = "positivo"
    elif polarity < 0:
        tone = "negativo"
    else:
        tone = "neutral"

    return {
        "polarity": polarity,
        "tone": tone
    }