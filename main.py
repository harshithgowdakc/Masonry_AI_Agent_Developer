# main.py (updated)
from agent import WebResearchAgent
import time

def run_cli():
    agent = WebResearchAgent()
    query = input("Enter your research query: ")

    print("\n🔍 Searching Google...")
    results = agent.search(query)

    print("\n📄 Scraping pages...")
    sources = []
    for r in results[:3]:  # top 3 only
        print(f"- {r['title']}")
        content = agent.scrape(r['link'])
        sources.append(content)

    print("\n📰 Finding recent news...")
    news_data = agent.get_news(query)
    if news_data:
        print(f"Found {len(news_data)} relevant news articles")
    else:
        print("No relevant news articles found")

    print("\n🧠 Synthesizing response...")
    final_report = agent.synthesize(query, sources, news_data)

    print("\n📘 Final Report:\n")
    print(final_report)

if __name__ == "__main__":
    run_cli()