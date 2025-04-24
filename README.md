# Web Research Agent

An AI-powered web research assistant that can automatically search the web, extract information from websites, and compile comprehensive research reports.

## Features

- Web search using SerpAPI
- Content extraction with BeautifulSoup
- Information synthesis using Google Gemini
- Automatic report generation
- Error handling for failed requests

## Setup Instructions

1. Clone this repository:
    git clone https://github.com/harshithgowdakc/Masonry_AI_Agent_Developer.git 

2. Create and activate a virtual environment:
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate


3. Install dependencies:
    pip install -r requirements.txt


4. Create a .env file with your API keys:
    SERPAPI_API_KEY=your_serpapi_key_here
    GEMINI_API_KEY=your_gemini_key_here