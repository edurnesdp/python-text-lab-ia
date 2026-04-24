import unittest
from modules.text_analysis import analyze_text, detect_authorship_variation, detect_emotional_tone

class TestTextAnalysis(unittest.TestCase):

    def test_analyze_text(self):
        text = "Hola mundo. Esto es una prueba."
        result = analyze_text(text)
        self.assertEqual(result["longitud"], len(text))
        self.assertEqual(result["palabras"], 6)
        self.assertEqual(result["caracteres"], 24)
        self.assertEqual(result["idioma"], "es")

    def test_detect_authorship_variation(self):
        text = "Hola mundo. Esto es una prueba.\n\nOtro párrafo diferente."
        result = detect_authorship_variation(text)
        self.assertIn("segment_features", result)
        self.assertIn("variations", result)
        self.assertIn("significant_variations", result)

    def test_detect_emotional_tone_positive(self):
        text = "Soy Feliz."
        result = detect_emotional_tone(text)
        self.assertEqual(result["tone"], "neutral")

    def test_detect_emotional_tone_negative(self):
        text = "Esto es terrible."
        result = detect_emotional_tone(text)
        self.assertEqual(result["tone"], "negativo")

    def test_detect_emotional_tone_neutral(self):
        text = "Esto es un texto."
        result = detect_emotional_tone(text)
        self.assertEqual(result["tone"], "neutral")

if __name__ == "__main__":
    unittest.main()