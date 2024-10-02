from fastapi import WebSocket

class WebSocketConnectionModel:
    client_id: str
    socket: WebSocket