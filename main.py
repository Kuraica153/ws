from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from templates.client import html
from services.persona import PersonaService
import yaml

app = FastAPI()


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            imc = PersonaService.get_imc(data)
            print (imc)
            await websocket.send_text(f"Message text was: {imc}")
    except Exception as e:
        print(e)
    