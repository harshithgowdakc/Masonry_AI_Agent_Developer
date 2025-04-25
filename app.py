# app.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from agent import WebResearchAgent
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env variables

app = FastAPI(title="Masonry Web Research Agent")

@app.get("/")
def home():
    return {"message": "Masonry Web Research Agent", "docs": "/docs"}

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)

agent = WebResearchAgent()

@app.post("/research")
async def conduct_research(query: str):
    try:
        results = agent.search(query)
        sources = []
        
        for r in results[:3]:  # Top 3 results only
            content = agent.scrape(r['link'])
            sources.append({
                "title": r['title'],
                "url": r['link'],
                "content": content[:1000] + "..." if len(content) > 1000 else content
            })
        
        # Get recent news articles
        news_data = agent.get_news(query)
            
        report = agent.synthesize(query, [s['content'] for s in sources], news_data)
        
        return {
            "query": query,
            "sources": sources,
            "news": news_data,
            "report": report,
            "public_url": os.getenv("NGROK_URL", "Not configured")
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    # Start Ngrok tunnel if URL exists in .env
    if os.getenv("NGROK_URL"):
        print(f"\n🔗 Public URL: {os.getenv('NGROK_URL')}/research")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)