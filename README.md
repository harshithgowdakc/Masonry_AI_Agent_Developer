# Web Research Agent for Masonry AI

An AI-powered agent that searches the web, extracts content, and creates research reports based on user queries.

## Features
- 🔍 Web Search - Uses SerpAPI
- 📑 Content Extraction - Uses BeautifulSoup
- 📰 News Aggregation - Finds recent articles
- 🧠 Information Synthesis - Uses Google Gemini
- ⚡ Error Handling - Recovers from failures

## Installation
```
# Clone repo
git clone https://github.com/harshithgowdakc/Masonry_AI_Agent_Developer.git

# Setup environment (Windows)
python -m venv env
env\Scripts\activate

# Setup environment (Mac/Linux)
python -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with:
SERPAPI_API_KEY=your_key
GEMINI_API_KEY=your_key
```

## Usage

### Command Line:
```
python main.py
# Enter your research query when prompted
```

### API:
```
# Start server
python app.py

# Make request
curl -X POST "http://localhost:8000/research?query=your_question"
```

## Project Files
- `agent.py` - Core research logic
- `app.py` - FastAPI server
- `main.py` - CLI interface
- `test_agent.py` - Unit tests
- `flowchart.png` - System architecture

## How It Works
The agent follows these steps:
1. User enters a research query
2. Agent searches the web using SerpAPI
3. Agent scrapes content from top results
4. Agent collects related news articles
5. Agent uses Gemini AI to create a final report