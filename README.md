# resume-extraction-summarization
Converts the pdf files uploaded into a HTML Resume

# Resume PDF Extraction and Summarization Tool

This project is a web-based application that extracts text from a PDF resume, identifies key sections like contact information, education, professional summary, key skills, and work experience, and uses Google’s Gemini API to summarize the text from each section. It is built with Python (Flask) on the backend and a simple HTML/JavaScript frontend.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [How I Approached and Solved the Problem](#how-i-approached-and-solved-the-problem)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- Extract text from PDF resumes using PyPDF2.
- Automatically detect and divide sections: Contact Information, Education, Professional Summary, Key Skills, Work Experience.
- Summarize each section using Google's Gemini API.
- Simple user interface to upload PDF files and display the summarized output.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **APIs**:
  - Google Generative AI (Gemini) API for summarization

## How I Approached and Solved the Problem

1. **Problem Understanding**: 
   The goal was to extract structured information from a PDF resume and return summarized content from specific sections using AI. The challenge was to reliably extract text from PDF files, identify and separate sections, and then summarize them using an AI model.

2. **Text Extraction with OCR**: 
   I used the PyPDF2 to extract raw text from the PDF. OCR technology allowed us to handle unstructured data by converting PDF content into plain text. After receiving the raw text, I needed to process it to separate different sections of the resume.

3. **Section Identification**: 
   Resumes usually follow a fairly standard format. Based on this, I used keywords like "Education," "Professional Summary," and "Work Experience" to divide the extracted text into corresponding sections. To handle edge cases where some resumes may not follow this structure exactly, I implemented error handling and safe string splitting methods.

4. **Summarization with Gemini API**: 
   Once the sections were identified, I used Google’s Gemini API to summarize each section. The Gemini API provided high-quality summarization by simply passing the raw text from each section, making the summarized text concise and easier to understand.

5. **Frontend Development**: 
   I built a simple HTML/JavaScript frontend for file upload and interaction with the Flask backend. The user can upload a PDF file, provide optional context, and view the extracted and summarized resume sections.

6. **Error Handling and User Feedback**: 
   I incorporated error handling for scenarios such as invalid PDF files, missing sections, and issues with API responses. User feedback was provided on the frontend to inform the user of the current status (e.g., file upload errors, successful extraction, or processing errors).

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/resume-extraction-summarization.git
cd resume-extraction-summarization
