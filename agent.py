# agent.py
import os
import requests
import google.generativeai as genai
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

class WebResearchAgent:
    def __init__(self):
        self.serp_api_key = os.getenv("SERPAPI_API_KEY")
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=self.gemini_api_key)
        self.model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

    def search(self, query):
        params = {
            "q": query,
            "api_key": self.serp_api_key,
            "engine": "google"
        }
        res = requests.get("https://serpapi.com/search", params=params)
        res.raise_for_status()
        return res.json()["organic_results"][:5]

    def scrape(self, url):
        try:
            html = requests.get(url, timeout=5).text
            soup = BeautifulSoup(html, "html.parser")
            for tag in soup(["script", "style", "header", "footer", "nav", "aside"]):
                tag.decompose()
            text = soup.get_text(separator="\n")
            blocks = [block.strip() for block in text.split("\n") if len(block.split()) > 20]
            return "\n\n".join(blocks)[:10000]
        except Exception as e:
            return f"Failed to scrape {url}: {e}"

    def get_news(self, query, days=7):
        """
        Find recent news articles related to the query.
        
        Args:
            query (str): The search query
            days (int): How many days back to search for news
            
        Returns:
            list: List of news article data
        """
        try:
            # Calculate date range (last X days)
            end_date = datetime.now().strftime('%Y-%m-%d')
            start_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
            
            # Use SerpAPI's news search
            params = {
                "q": query,
                "api_key": self.serp_api_key,
                "engine": "google",
                "tbm": "nws",  # News search
                "tbs": f"cdr:1,cd_min:{start_date},cd_max:{end_date}"  # Date range
            }
            
            res = requests.get("https://serpapi.com/search", params=params)
            res.raise_for_status()
            
            # Extract news results
            news_results = res.json().get("news_results", [])
            if not news_results and "organic_results" in res.json():
                # Fallback to organic results if no specific news results
                news_results = res.json()["organic_results"][:3]
                
            # Format news data
            news_data = []
            for item in news_results[:3]:  # Top 3 news items
                news_data.append({
                    "title": item.get("title", ""),
                    "source": item.get("source", ""),
                    "date": item.get("date", ""),
                    "link": item.get("link", ""),
                    "snippet": item.get("snippet", "")
                })
                
            return news_data
        except Exception as e:
            print(f"News aggregation error: {e}")
            return []  # Return empty list on error

    def synthesize(self, query, sources, news_data=None):
        docs = [f"Source {i+1}:\n{content[:2000]}" for i, content in enumerate(sources)]
        
        # Add news data if available
        if news_data and len(news_data) > 0:
            news_text = "Recent News:\n"
            for i, item in enumerate(news_data):
                news_text += f"News {i+1}: {item['title']} ({item['source']}, {item['date']})\n"
                news_text += f"{item['snippet']}\n\n"
            docs.append(news_text)
        
        prompt = f"""You are an expert research assistant.
Answer this question: {query}

Based on the sources below, write a detailed, well-cited report. Include:
- Key Findings
- Supporting Evidence
- Conclusion

{"".join(docs)}
"""
        response = self.model.generate_content(prompt)
        return response.text