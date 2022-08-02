from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

from helper_funcs import get_html

html = get_html('websocket_app.html')
app = FastAPI()


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message: {data}")
