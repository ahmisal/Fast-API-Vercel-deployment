from time import time
from fastapi import FastAPI, __version__
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os
from groq import Groq

key = os.getenv("key")

client = Groq(api_key=key,)


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>FastAPI on Vercel</title>
        <link rel="icon" href="/static/favicon.ico" type="image/x-icon" />
    </head>
    <body>
        <div class="bg-gray-200 p-4 rounded-lg shadow-lg">
            <h1>Hello from FastAPI@{__version__}</h1>
            <ul>
                <li><a href="/docs">/docs</a></li>
                <li><a href="/redoc">/redoc</a></li>
            </ul>
            <p>Powered by <a href="https://vercel.com" target="_blank">Vercel</a></p>
        </div>
    </body>
</html>
"""

@app.get("/")
async def root():
    return HTMLResponse(html)

@app.get("/atomcamp")
async def atomcamp():
    return "Hello this is our experiment endpoint .............."

@app.get("/8april")
async def april():
    return "we just created a new endpoint"

@app.get("/chat/{q}")
async def groq(q):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": q,
            }
        ],
        model="llama3-8b-8192",
    )

#print(chat_completion.choices[0].message.content)
    return str(chat_completion.choices[0].message.content)

@app.get('/ping')
async def hello():
    return {'res': 'pong', 'version': __version__, "time": time()}
