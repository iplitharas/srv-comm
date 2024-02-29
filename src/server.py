"""
This module contains the `FastAPI` application that will be used to run the service B.
"""
import http

from fastapi import FastAPI, Response
from pydantic import BaseModel

from src.services.srv_b import ServiceB

app = FastAPI(tile="Service B")


class RequestModel(BaseModel):
    """
    Payload to be sent to the server.
    """

    message: str


class ResponseModel(BaseModel):
    """
    Response from the server.
    """

    message: str


@app.post("/greet/", status_code=http.HTTPStatus.ACCEPTED)
def greet(payload: RequestModel, response: Response) -> ResponseModel:
    """
    Greet the client with a message if Service B is available, otherwise
    return a 503 status code.
    """
    srv_b = ServiceB()
    if srv_b.accept_message():
        response.status_code = http.HTTPStatus.ACCEPTED
        return ResponseModel(message=f"{payload.message} {srv_b.render_response()}")

    response.status_code = http.HTTPStatus.SERVICE_UNAVAILABLE
    return ResponseModel(message="Service B is not available at the moment")
