from fastapi import FastAPI
from typing import List
from fastapi import HTTPException
from pydantic import BaseModel
from textblob import TextBlob


class MoodInput(BaseModel):
    mood:List[str]

app = FastAPI()
@app.post('/')
def analyze_moods(input:MoodInput):
    if not input.mood:
        raise HTTPException(status_code=400,detail="Uh-oh.. Looks like you forgot to enter data")
    results = []
    for mood in input.mood:  
        sentiment = TextBlob(mood).sentiment.polarity
        if sentiment > 0:
                results.append({"mood": mood, "sentiment": "Positive"})
        elif sentiment < 0:
                results.append({"mood": mood, "sentiment": "Negative"})
        else:
                results.append({"mood": mood, "sentiment": "Neutral"})
    return {"results":results}


