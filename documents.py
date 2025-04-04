from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from frontend

@app.route('/analyze', methods=['POST'])
def analyze_document():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400

    text = file.read().decode('utf-8', errors='ignore')  # Simple text extraction
    summary = summarize_contract(text)
    
    return jsonify({'summary': summary})

# Dummy summarization function (you'll replace with real AI logic)
def summarize_contract(text):
    # TODO: Replace with NLP/transformer model
    return text[:500] + '... [summary truncated]'  # Dummy: just truncates text

if __name__ == '__main__':
    app.run(debug=True)