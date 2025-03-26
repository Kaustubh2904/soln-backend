# Professor AI - Educational Assistant Chatbot

## Overview
Professor AI is an educational chatbot application built with Streamlit that serves as a virtual teaching assistant for students. Using Google's Gemini 1.5 Flash model, it provides concise, accurate responses to academic questions across various subjects.

## Features
- **Interactive Chat Interface**: Clean and intuitive UI powered by Streamlit
- **Persistent Chat History**: Maintains conversation context during user sessions
- **Realistic Typing Animation**: Response text appears incrementally for a more natural interaction
- **Educational Focus**: Specifically designed to explain concepts and build intuition for problem-solving

## Technology Stack
- [Streamlit](https://streamlit.io/): Frontend web application framework
- [Google Generative AI](https://ai.google.dev/): Gemini 1.5 Flash model for generating responses
- Python 3.x with dotenv for environment management

## Setup Instructions

### Prerequisites
- Python 3.x
- Google API key for Gemini AI

### Installation
1. Clone the repository
2. Install the required packages:
```
pip install streamlit google-generativeai python-dotenv
```
3. Create a `.env` file in the project root with your Google API key:
```
GOOGLE_API_KEY=your_api_key_here
```
4. Run the application:
```
streamlit run main.py
```

## How It Works
The application follows a simple workflow:
1. User submits a question through the Streamlit chat interface
2. The question is processed by the `llm_logic.py` module
3. The Gemini model generates a response with specific educational instructions
4. The response is displayed in the chat with a realistic typing animation effect

## Project Structure
- `main.py`: Contains the Streamlit application and UI logic
- `llm_logic.py`: Handles interactions with the Gemini AI model
- `requirements.txt`: Lists project dependencies
- `README.md`: Project documentation

## Use Cases
- Explaining complex academic concepts
- Providing homework assistance
- Answering subject-specific questions
- Offering concise explanations tailored to student understanding

## Future Enhancements
- Subject-specific modes
- Support for image uploads for visual problems
- Customizable response length
- User authentication for personalized learning experiences
