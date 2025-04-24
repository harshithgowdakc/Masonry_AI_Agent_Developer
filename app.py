# app.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from agent import WebResearchAgent
import uvicorn

app = FastAPI(title="Masonry Web Research Agent")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

agent = WebResearchAgent()

@app.post("/research")
async def conduct_research(query: str):
    try:
        # Search
        results = agent.search(query)
        
        # Scrape top 3 results
        sources = []
        for r in results[:3]:
            content = agent.scrape(r['link'])
            sources.append({
                "title": r['title'],
                "url": r['link'],
                "content": content[:1000] + "..." if len(content) > 1000 else content
            })
        
        # Generate report
        report = agent.synthesize(query, [s['content'] for s in sources])
        
        return {
            "query": query,
            "sources": sources,
            "report": report
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)