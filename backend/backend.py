import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# --- SETUP ---
app = Flask(__name__)
CORS(app)

# --- API KEY SETUP ---
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Google API key not found. Make sure it's set in your .env file.")
genai.configure(api_key=api_key)


# --- THE CORE AI LOGIC ---
def get_ai_analysis(text):
    """
    Sends text to the Google Gemini API for a detailed analysis.
    """
    # --- NEW, MORE DETAILED PROMPT ---
    # This prompt asks for a much more structured and detailed JSON output.
    system_prompt = """
    You are an expert misinformation analyst. Your task is to analyze the provided text and identify specific rhetorical devices, logical fallacies, and cognitive biases.

    Your response MUST be a single, valid JSON object with the following structure and nothing else. Do not include markdown formatting like ```json.
    {
      "score": <an integer from 0 (very trustworthy) to 10 (very misleading)>,
      "summary": "<A one-sentence overall summary of the analysis>",
      "analysis": {
        "fallacies": [
          {
            "type": "<Name of the logical fallacy, e.g., 'Appeal to Emotion' or 'Strawman'>",
            "explanation": "<A brief explanation of how this fallacy is used in the text>",
            "evidence": ["<list of specific quotes from the text that demonstrate the fallacy>"]
          }
        ],
        "biases": [
          {
            "type": "<Name of the cognitive bias, e.g., 'Confirmation Bias'>",
            "explanation": "<A brief explanation of how this bias is being appealed to>",
            "evidence": ["<list of specific quotes from the text that demonstrate the bias>"]
          }
        ]
      }
    }
    If no fallacies or biases are found, return an empty list [] for the respective key.
    """

    # Configure the model
    model = genai.GenerativeModel('gemini-2.5-flash')

    try:
        full_prompt = f"{system_prompt}\n\nAnalyze this text:\n---\n{text}"
        response = model.generate_content(full_prompt)

        # Clean the response to ensure it's a valid JSON string
        analysis_json_string = response.text.strip()

        # Convert the JSON string into a Python dictionary
        analysis_dict = json.loads(analysis_json_string)

        return analysis_dict

    except Exception as e:
        print(f"An error occurred with the Google Gemini API or JSON parsing: {e}")
        # Return a structured error message that the frontend can handle
        return {
            "score": "Error",
            "summary": f"Could not analyze text due to an API error: {e}",
            "analysis": {"fallacies": [], "biases": []}
        }


# --- API ENDPOINT ---
@app.route("/api/analyze", methods=['POST'])
def analyze_text():
    data = request.get_json()
    text_to_analyze = data.get('text')

    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400

    print(f"Received text for detailed analysis: {text_to_analyze}")
    analysis_result = get_ai_analysis(text_to_analyze)
    return jsonify(analysis_result)


# --- RUN THE APP ---
if __name__ == "__main__":
    app.run(debug=True, port=5000)
