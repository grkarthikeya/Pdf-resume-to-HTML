import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import PyPDF2

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes

# Replace with your Gemini API key
GEMINI_API_KEY = 'AIzaSyDJTkI7QJYIVGcuUgYq03LjRQGa6J7oqyE'

# Configure Gemini API key
genai.configure(api_key=GEMINI_API_KEY)

# Function to extract text from PDF using PyPDF2
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    extracted_text = ""

    for page in range(len(pdf_reader.pages)):
        extracted_text += pdf_reader.pages[page].extract_text()

    return extracted_text

# Function to summarize text for a specific section using the Gemini API
def summarize_section_with_gemini(extracted_text, section):
    prompt = f"Precisely Summarize the following {section} section:\n\nText: {extracted_text}"
    
    # Instantiate the Gemini model
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Generate content using Gemini
    response = model.generate_content(prompt)
    
    # Handle response
    if response and hasattr(response, 'text'):
        return response.text
    else:
        return "No summary available."

# Function to divide text into sections based on typical resume structure
def divide_resume_into_sections(extracted_text):
    sections = {
        'Contact Information': '',
        'Education': '',
        'Professional Summary': '',
        'Key Skills': '',
        'Work Experience': ''
    }

    # Helper function to safely split text
    def safe_split(text, delimiter):
        parts = text.split(delimiter, 1)  # Split into at most 2 parts
        if len(parts) == 2:
            return parts[0], parts[1]
        else:
            return text, ''

    # Split the text into sections based on typical resume structure
    contact_end, remainder = safe_split(extracted_text, 'Education')
    sections['Contact Information'] = contact_end

    education_end, remainder = safe_split(remainder, 'Professional Summary')
    sections['Education'] = education_end

    summary_end, remainder = safe_split(remainder, 'Key Skills')
    sections['Professional Summary'] = summary_end

    skills_end, remainder = safe_split(remainder, 'Work Experience')
    sections['Key Skills'] = skills_end

    sections['Work Experience'] = remainder

    return sections

# Route to handle PDF file upload and summarization
@app.route('/api/extract-text', methods=['POST'])
def extract_text():
    if 'pdf' not in request.files:
        return jsonify({'error': 'No PDF file uploaded'}), 400

    pdf_file = request.files['pdf']

    # Extract text from the uploaded PDF
    extracted_text = extract_text_from_pdf(pdf_file)

    # Divide the extracted text into sections
    sections = divide_resume_into_sections(extracted_text)

    # Summarize each section using the Gemini API
    summarized_sections = {}
    for section, text in sections.items():
        summarized_sections[section] = summarize_section_with_gemini(extracted_text, section)

    return jsonify(summarized_sections)

if __name__ == '__main__':
    app.run(debug=True)
