# Educational AI Suite

A comprehensive suite of AI-powered educational tools for teachers and students, featuring three integrated applications: **Professor AI** (student chatbot), **Question Paper Generator**, and **Advanced Assignment Grader**.

## Overview
The **Educational AI Suite** combines three powerful AI-based applications designed to enhance teaching and learning:

- **Professor AI**: A virtual teaching assistant chatbot for students.
- **Question Paper Generator**: An automated question creation tool for teachers.
- **Advanced Assignment Grader**: An intelligent assessment evaluation system.

These applications work together to create a seamless educational experience from content creation to student interaction to assessment evaluation.

## Applications
### 1. Professor AI - Educational Chatbot
A conversational AI assistant that helps students learn concepts and solve academic problems.

#### Key Features:
- Intuitive chat interface with realistic typing animation.
- Persistent chat history during sessions.
- Educational focus for clear, concise explanations.
- Helps students build intuition for problem-solving.

### 2. Question Paper Generator
A tool that creates customized sets of educational questions on any topic.

#### Key Features:
- Generate multiple-choice and text questions on any subject.
- Customize question count and type.
- Export questions as downloadable files.
- Access history of previously generated question sets.

### 3. Advanced Assignment Grader
An assessment creation and evaluation system with powerful analytics.

#### Key Features:
- Create customized assessments with various question types.
- Automatically evaluate student responses using NLP techniques.
- Generate visual analytics of student performance.
- Download templates and results for easy distribution.

## Technology Stack
### Frontend:
- **Streamlit** for Professor AI and Question Paper Generator.
- **HTML/CSS/JS with Bootstrap** for Advanced Assignment Grader.

### Backend:
- **Python with Flask** for web server functionality.
- **Google's Gemini 1.5 Flash model** for AI capabilities.

### Data Processing:
- **Pandas and NumPy** for data handling.
- **Scikit-learn** for text processing and similarity analysis.
- **Matplotlib and Seaborn** for data visualization.

## Installation
### Clone the repository:
```sh
 git clone https://github.com/Kaustubh2904/soln-backend.git
```

### Create a virtual environment:
```sh
 python -m venv venv
 source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Install dependencies for all applications:
```sh
 pip install -r requirements.txt
```

### Create a `.env` file in the project root with your Google API key:
```sh
 GOOGLE_API_KEY=your_api_key_here
```

## Usage
### Running Professor AI (Student Chatbot)
```sh
 streamlit run student_chatbot/main.py
```
Access at: [http://localhost:8501](http://localhost:8501)

### Running Question Paper Generator
```sh
 streamlit run qpm_bot/main.py
```
Access at: [http://localhost:8501](http://localhost:8501)

### Running Advanced Assignment Grader
```sh
 python auto_grader/graderv2.py
```
Access at: [http://localhost:5000](http://localhost:5000)

## Project Structure
```
educational-ai-suite/
├── student_chatbot/             # Professor AI - Educational Chatbot
│   ├── main.py                  # Streamlit application
│   ├── llm_logic.py             # Gemini AI integration
│   ├── Readme.md                # Documentation
│   └── requirements.txt         # Dependencies
│
├── qpm_bot/                     # Question Paper Generator
│   ├── main.py                  # Streamlit application
│   ├── qpm_logic.py             # Question generation logic
│   ├── Readme.md                # Documentation
│   └── requirements.txt         # Dependencies
│
├── auto_grader/                 # Advanced Assignment Grader
│   ├── graderv2.py              # Flask application
│   ├── requirements.txt         # Dependencies
│   ├── templates/               # Web interface templates
│   │   └── index2.html          # Main interface
│   └── README.md                # Documentation
│
└── README.md                    # Main project documentation
```

## Integration Possibilities
These applications can work together for a complete educational workflow:

1. **Create Questions**: Use the Question Paper Generator to create assessment materials.
2. **Student Learning**: Students interact with Professor AI to learn concepts.
3. **Assessment**: Deploy questions via Advanced Assignment Grader.
4. **Evaluation**: Auto-grade responses and analyze performance metrics.
5. **Targeted Learning**: Direct students back to Professor AI for areas needing improvement.

## Future Enhancements
- **Cross-Application Integration**: Direct data sharing between applications.
- **User Authentication**: Single sign-on across all tools.
- **Expanded AI Capabilities**: Enhanced reasoning and explanation abilities.
- **Mobile Application**: Native mobile apps for student interaction.
- **LMS Integration**: Connect with popular Learning Management Systems.

## Requirements
- **Python 3.8+**
- **Internet connection** (for Gemini API access)
- **Modern web browser**
- **Google API key** with Gemini access

---
This project is designed to revolutionize AI-powered education. 🚀

For detailed documentation, refer to the individual Readme files in each application directory.