# Web Research Agent for Masonry AI

An autonomous AI agent that performs web research by searching, scraping, and synthesizing information into comprehensive reports.

## Features

🔍 **Web Search** - Uses SerpAPI to find relevant sources  
📑 **Content Extraction** - Scrapes key information using BeautifulSoup  
🧠 **Information Synthesis** - Generates reports with Google Gemini  
⚡ **Error Handling** - Robust failure recovery for web operations  
📊 **Structured Output** - Well-formatted reports with citations  

## Installation (Windows)

1. **Clone the repository**:
   cmd
   git clone https://github.com/harshithgowdakc/Masonry_AI_Agent_Developer.git


2. **Set up virtual environment**:
    cmd
    python -m venv env
    env\Scripts\activate

3. **Install dependencies**:
    cmd
    pip install -r requirements.txt

4. Configure API keys:
    Create .env file with:
    SERPAPI_API_KEY=your_serpapi_key
    GEMINI_API_KEY=your_gemini_key

5. Usage
    cmd
    python main.py
    Enter your research question when prompted.

6. Example:

    Enter your research query: What are the latest advancements in AI in 2025?
    [Agent will display progress and output report]


**Project Structure**
├── agent.py          # Core agent logic
├── main.py           # CLI interface
├── test_agent.py     # Unit tests
├── requirements.txt  # Dependencies
└── .env              # API configuration