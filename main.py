# main.py
from agent import WebResearchAgent

def run():
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

    print("\n🧠 Synthesizing response...")
    final_report = agent.synthesize(query, sources)

    print("\n📘 Final Report:\n")
    print(final_report)

if __name__ == "__main__":
    run()
