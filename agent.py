# agent.py
import os
import requests
import google.generativeai as genai
from bs4 import BeautifulSoup
from dotenv import load_dotenv

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

    def synthesize(self, query, sources):
        docs = [f"Source {i+1}:\n{content[:2000]}" for i, content in enumerate(sources)]
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
