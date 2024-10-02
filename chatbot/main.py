
import os
from pathlib import Path
from fastapi import FastAPI, Request, HTTPException
from fastapi import WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from connection_manager import ConnectionManager, WebSocketConnectionModel

BASE_DIR = Path(__file__).resolve().parent

server = FastAPI()
server.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
server.mount("/chatbot/static", StaticFiles(directory=str(Path(BASE_DIR, 'static'))), name="static")

templates = Jinja2Templates(directory=str(Path(BASE_DIR, "templates")))

manager = ConnectionManager()

profile = os.environ["PROFILE"]
ws_host = os.environ["WS_HOST"]

def process_message(self, data, client_id):
    print(data)

@server.get("/chatbot")
async def home(request: Request):
    print("Starting chatbot...")
    return templates.TemplateResponse(
        request = request, name = "index.html", context = {
            "src" : "chatbot/static",
            "profile" : profile,
            "ws_host" : ws_host,
            "soeid" : "nl0000"
        }
    )

@server.websocket("/communicate")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket, client_id)

    try:
        while True:
            data = await websocket.receive_json()
            print(f"Processing message: '{data}' for user = '{client_id}'")
            response = process_message(data, client_id)
            bot_response = manager.create_json_response(response, "bot")
            await manager.send_personal_message(bot_response, client_id)
    except WebSocketDisconnect as web_ex:
        connection = WebSocketConnectionModel()
        connection.client_id = client_id
        connection.socket = websocket
        manager.disconnect(connection)

        if web_ex.code == 1000:
            print("Session finished")
        else:
            print("Error in Session")
    except Exception as ex:
        print(f"An error has occured while trying to establish WS connection:{ex}")



async def app(scope, receive, send):
    assert scope['type'] == 'http'

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })
    await send({
        'type': 'http.response.body',
        'body': b'Hello, world! Great me!',
    })