from fastapi import FastAPI
from translate import translate
import uvicorn

app = FastAPI(
    title = "Korean 2 English Translator",
    description = "Korean to English translator using huggingface transformer.",
    version = "0.1"
)

@app.get("/translate/")
async def translator(input: str):
    en = translate(input)
    return {"output" : en}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host='0.0.0.0')