
# Web Research Agent for Masonry AI  
An autonomous AI agent that performs web research by searching, scraping, and synthesizing information into comprehensive reports.  

## Features  
🔍 **Web Search** - Uses SerpAPI  
📑 **Content Extraction** - Uses BeautifulSoup  
🧠 **Information Synthesis** - Uses Google Gemini  
⚡ **Error Handling** - Robust failure recovery  
📊 **Structured Output** - Formatted reports  

## Installation (Windows)  

## Setup  
1. Clone:  
`git clone https://github.com/harshithgowdakc/Masonry_AI_Agent_Developer.git`  

2. Environment:  
`python -m venv env && env\Scripts\activate`  

3. Install:  
`pip install -r requirements.txt`  

4. Add `.env`:  
`SERPAPI_API_KEY=your_key`  
`GEMINI_API_KEY=your_key`  

## Usage  
**CLI**:  
`python main.py` (Enter query when prompted)  

**API**:  
1. Start: `python app.py`  
2. Query:  
`curl -X POST "http://localhost:8000/research?query=your_question"`  

## Files  
`agent.py` - Logic 
`app.py` - API 
`main.py` - CLI  
`test_agent.py` - Tests
`.env` - Config  