from fastapi import FastAPI
from translate import translate
import uvicorn
from pydantic import BaseModel

class Input(BaseModel):
    text: str

app = FastAPI(
    title = "Korean 2 English Translator",
    description = "Korean to English translator using huggingface transformer.",
    version = "0.1"
)
@app.get("/")
def read_root():
    return {"message": "Welcome to Korean to English Translator!"}

@app.post('/translate')
def translator(input: Input):
    en = translate(input.text)
    return {"English Translation" : en}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host='0.0.0.0')