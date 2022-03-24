from fastapi import FastAPI
from scraper import Scraper

app = FastAPI()

@app.get("/{cat}")
async def read_item(cat):
  return quotes.scrapdata(cat)