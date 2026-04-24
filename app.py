from flask import Flask, request, render_template
from modules.text_analysis import analyze_text, detect_authorship_variation, detect_emotional_tone

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    analysis = analyze_text(text)
    authorship = detect_authorship_variation(text)
    emotional_tone = detect_emotional_tone(text)
    return render_template('result.html', analysis=analysis, authorship=authorship, emotional_tone=emotional_tone)

if __name__ == '__main__':
    app.run(debug=True)