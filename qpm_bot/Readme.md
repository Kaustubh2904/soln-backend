# Professor AI - Question Paper Generator

A web-based educational tool powered by Google's Gemini AI for generating high-quality assessment questions for teachers and educators. Create custom question sets on any topic with a few clicks, including multiple-choice, text, and combined question types.

## Features

- **AI-Generated Educational Questions:** Create customized question sets on any topic
- **Multiple Question Formats:**
  - Multiple-choice questions with plausible distractors
  - Text/short answer questions with model answers
  - Combined question types
- **User-Friendly Interface:**
  - Clean, intuitive Streamlit web application
  - Customizable question parameters
  - One-click question generation
- **Export & History Features:**
  - Download generated questions as text files
  - Access previously generated question sets
  - Quick regeneration of past topics

## Technical Stack

- **Frontend:** Streamlit web application with custom CSS styling
- **AI Backend:** Google's Gemini 1.5 Flash model
- **Key Libraries:**
  - `streamlit`: Web application framework
  - `google.generativeai`: Google Gemini API integration
  - `python-dotenv`: Environment variable management

## Setup

1. Clone the repository
2. Install dependencies
3. Create a `.env` file with your API key:
4. Launch the application:

## Usage

1. Enter a topic in the sidebar (e.g., "Machine Learning")
2. Choose your question type (multiple choice, text, or both)
3. Set the number of questions (1-10)
4. Click "Generate Questions"
5. View your questions in the main panel
6. Download questions as a text file
7. Access your question history from the expandable history section

## Customization

The application features custom CSS styling for a professional appearance. Modify the CSS in the `main.py` file to adjust the visual design to your preferences.


