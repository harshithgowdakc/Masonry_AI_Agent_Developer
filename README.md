# Web Research Agent for Masonry AI  
An autonomous AI agent that performs web research by searching, scraping, and synthesizing information into comprehensive reports.  

## Features  
🔍 **Web Search** - Uses SerpAPI  
📑 **Content Extraction** - Uses BeautifulSoup  
🧠 **Information Synthesis** - Uses Google Gemini  
⚡ **Error Handling** - Robust failure recovery  
📊 **Structured Output** - Formatted reports  

## Installation (Windows)  

1. Clone repository:  
`git clone https://github.com/harshithgowdakc/Masonry_AI_Agent_Developer.git`  

2. Setup environment:  
`python -m venv env`  
`env\Scripts\activate`  

3. Install dependencies:  
`pip install -r requirements.txt`  

4. Configure API keys:  
Create `.env` file with:  
`SERPAPI_API_KEY=your_serpapi_key`  
`GEMINI_API_KEY=your_gemini_key`  

## Usage  
Run: `python main.py`  
Example:  
`Enter your research query: What are AI advancements in 2025?`  
`[Agent displays progress and outputs report]`  

## Project Structure  
`agent.py` - Core logic  
`main.py` - CLI interface  
`test_agent.py` - Unit tests  
`requirements.txt` - Dependencies  
`.env` - API config  