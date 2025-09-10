from fastapi import FastAPI, File, UploadFile, Form
from pydantic import BaseModel
from typing import List
from backend.ner_extraction import extract_named_entities


app = FastAPI(title="AI Health Assistant")

class EntitiesResponse(BaseModel):
    entities: List[dict]

@app.post("/extract_entities", response_model=EntitiesResponse)
async def extract_text_entities(text: str = Form(...)):
    entities = extract_named_entities(text)
    return {"entities": entities}